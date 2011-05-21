from django.db.models.signals import post_save
from django.contrib.auth.models import User
from portal.models import Profile
from django.core.exceptions import ObjectDoesNotExist

def create_profile(sender, **kwargs):
    # Your specific logic here
    try:
        kwargs['instance'].get_profile()
    except ObjectDoesNotExist:
	profile = Profile ()
        profile.user = kwargs['instance']
        profile.save()


post_save.connect(create_profile, sender=django.contrib.auth.models.User)
