from django.db import models


class SiteUser(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=16,
                                unique=True)
    email = models.EmailField(max_length=128,
                              unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username

    def to_json(self):
        return {
            'name': self.name,
            'username': self.username,
            'email': self.email,
        }
