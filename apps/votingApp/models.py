from django.db import models

# Create your models here.

class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 2:
            errors["email"] = "Email cannot be THAT short!"
        return errors

class Vote(models.Model):
    email       = models.EmailField(max_length=255)
    framework   = models.CharField(max_length=255)
    session     = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = UserManager()

    def __repr__(self):
        return f" ID: {self.id}, Count: {self.voteCount}"