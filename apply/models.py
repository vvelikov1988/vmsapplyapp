from django.db import models
from datetime import date, datetime
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class ApplicantManager(models.Manager):
    def register_validator(self, formData):
        errors = {}
        check = Applicant.objects.filter(email=formData['email'])
        if len(formData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(formData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(formData['resume']) < 15:
            errors['resume'] = "Please upload a more detailed resume."
        if len(formData['email']) < 1:
            errors['email'] = "Email address cannot be blank."
        elif not EMAIL_REGEX.match(formData['email']):
            errors['email'] = "Please enter a valid email address."
        elif check:
            errors['email'] = "Email address is already registered."
        return errors    


class Applicant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    resume = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ApplicantManager()