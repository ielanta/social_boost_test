from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    bio = models.TextField(max_length=512, blank=True, null=True)
    employment = models.CharField(max_length=256, blank=True, null=True)
    company_role = models.CharField(max_length=64, blank=True, null=True)
    seniority = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    site = models.URLField(max_length=512, blank=True, null=True)
    github = models.URLField(max_length=512, blank=True, null=True)
    twitter = models.URLField(max_length=512, blank=True, null=True)
    facebook = models.URLField(max_length=512, blank=True, null=True)
    linkedin = models.URLField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
