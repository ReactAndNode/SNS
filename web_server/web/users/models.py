from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

SEX_CHOICE = [("M", "Male"), ("F", "Female"), ('O', "Other")]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email_confirmed = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = location = models.CharField(max_length=30, blank=True)
    last_name = location = models.CharField(max_length=30, blank=True)
    sex = models.CharField(choices=SEX_CHOICE, max_length=1, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    publisher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

