# Generated by Django 2.2.4 on 2019-09-02 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('bio', models.TextField(blank=True, max_length=512)),
                ('employment', models.CharField(blank=True, max_length=256)),
                ('company_role', models.CharField(blank=True, max_length=64)),
                ('seniority', models.CharField(blank=True, max_length=64)),
                ('location', models.CharField(blank=True, max_length=128)),
                ('site', models.URLField(blank=True, max_length=512)),
                ('github', models.URLField(blank=True, max_length=512)),
                ('twitter', models.URLField(blank=True, max_length=512)),
                ('facebook', models.URLField(blank=True, max_length=512)),
                ('linkedin', models.URLField(blank=True, max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
