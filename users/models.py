from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    SECRET = 3
    ROLE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (SECRET, 'Secret'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
