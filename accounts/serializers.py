import logging
from django.contrib.auth.models import User

from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import ValidationError
from requests.exceptions import HTTPError

from integrations.clearbit import get_clearbit_data
from integrations.email_hunter import verify_email
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = Account
        fields = ['user', 'name', 'bio', 'employment', 'company_role', 'seniority', 'location', 'site', 'github',
                  'twitter', 'facebook', 'linkedin', 'id']


class UserSerializer(AccountSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data):
        email = validated_data['email']
        validation = verify_email(email)

        if validation.get('result') != 'deliverable':
            if validation.get('errors'):
                logging.error(f'Hunter.io: {validation}')
            else:
                logging.error(f'{email} is invalid. Status: {validation.get("result")}')
            raise ValidationError(validation)

        logging.info(f'{email} is valid')
        user = User.objects.create(email=email, username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        try:
            data = get_clearbit_data(email)
        except HTTPError:
            logging.error(f'Clearbit data error for {email}')
            raise ValidationError('Invalid email')

        Account.objects.create(user=user, **data)
        logging.info(f'Account for {email} was created')
        return user

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
