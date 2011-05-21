from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    games_played = models.IntegerField(default=0)
    avatar_image = models.ImageField(upload_to='images/avatars', null=True, blank=True)
    level =  models.IntegerField(default=0)
    about = models.CharField(max_length=500, default='')
    my_friends = models.ManyToManyField(User, related_name='friends')
     
    def __unicode__(self):
        return self.user.username


#######################
# Signals
######################
def create_profile(sender, **kwargs):
    # Your specific logic here
    try:
        kwargs['instance'].get_profile()
    except ObjectDoesNotExist:
	profile = Profile ()
        profile.user = kwargs['instance']
        profile.save()


post_save.connect(create_profile, sender=User)
#########################

# Create your models here.
