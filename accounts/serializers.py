from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import ValidationError

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
        validation = verify_email(validated_data['email'])
        if validation.get('result') != 'deliverable':
            raise ValidationError(validation)

        user = User.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Account.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
