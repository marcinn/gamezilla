# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save



MSG_STATUS = (
	('R', 'przeczytana'),
	('N', 'nieprzeczytana')
)

class MsgStatus(object):
	Read = 'R'
	Unread = 'N'
		
class Message (models.Model):
	sender = models.ForeignKey(User, related_name='sent_messages')
	adressee = models.ForeignKey(User, related_name='recived_messages')
	status = models.CharField(max_length=1, choices=MSG_STATUS, default=MsgStatus.Read)
	topic = models.CharField(max_length=255, default='')
	msg = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	
	@staticmethod
	def send_msg (sender, adressee, topic, content):
		
		msg = Message()
		msg.sender = sender
		msg.adressee = adressee
		msg.topic = topic
		msg.msg = content
		
		msg.save()
		return msg
	
	@staticmethod
	def get_messanger():
		
		messanger = None		
		try:
			messanger = User.objects.get(email='messanger@noreply.com')
		except User.DoesNotExist as e:
			
			u = User()
			u.email = 'messanger@noreply.com'
			u.first_name = 'Powiadomienia'
			u.save()
			messanger = u
		
		return messanger


INVITATIONS = (
	('I', 'Invited'),
	('A', 'Accepted'),
	('N', 'None'),
)

class Activity (models.Model):
	user = models.ForeignKey(User, related_name='activities')
	desc = models.TextField()
	type = models.CharField(max_length=1, default='G')
	date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__ (self):
		return self.user.username + " " + self.desc
	
	@staticmethod
	def add_activity (user, desc, type):
		a = Activity()
		a.user = user
		a.desc = desc
		a.type = type
		a.save()
		
		return a

	@staticmethod		
	def get_user_acivity (user):
		return Activity.objects.filter (user=user)
		
	@staticmethod		
	def count_user_acivity (user):
		return Activity.objects.filter(user=user).count()		

class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)
	games_played = models.IntegerField(default=0)
	avatar_image = models.ImageField(upload_to='images/avatars', null=True, blank=True)
	level =  models.IntegerField(default=0)
	about = models.CharField(max_length=500, default='')
	my_friends = models.ManyToManyField(User, related_name='friends', through='Friendlist')
     
	def __unicode__(self):
		return self.user.username        
	
	def is_friend (self, user):
		try:
			fr = Friendlist.objects.get (inviter=self, invited=user)
			return fr.status
		except Friendlist.DoesNotExist:
			return 'N'        
        
	def invite_friend (self, user):
		
		inv = Friendlist ()

		inv.inviter = self
		inv.invited = user
		inv.save()
			
	def remove_friend (self, user):
 		if user in my_friends.all():
			self.my_friends.remove(user)
			
	def count_firends(self):
		return self.my_friends.count()
		
	def get_invitations (self):
		return Friendlist.objects.filter (invited=self, status='I')
		
	def count_invitations (self):
		return Friendlist.objects.filter (invited=self, status='I').count()
		
	def get_friends (self):
		return Friendlist.objects.filter (invited=self, status='A')
		
	def count_friends (self):
		return Friendlist.objects.filter (invited=self, status='A').count()
		
	def count_activities (self):
		return Activity.count_user_acivity(self)
		
	def get_activities (self):
		return Activity.get_user_acivity(self)

ACTIVITY_TYPE = (
	('G', 'Game'),
	('U', 'User'),
)


		

class Friendlist (models.Model):	
	inviter = models.ForeignKey(Profile, related_name='sent_invitations')
	invited = models.ForeignKey(User, related_name='recived_invitations')
	status =  models.CharField(max_length=1, default='I')
	date = models.DateTimeField(auto_now_add=True, auto_now = True)
	
	def decline (self):
		topic = u"Użytkownik " + self.invited.username + u" odrzucił twoje zaproszenie." 		
		Message.send_msg (Message.get_messanger(), self.inviter.user, topic, "")
		self.delete()
		
	def accept (self):		
		
		if self.status =='I':
			topic = u"Użytkownik " + self.invited.username + u" zaakceptowal twoje zaproszenie."		
			Message.send_msg (Message.get_messanger(), self.inviter.user, topic, "")
			self.status = 'A'
			self.save()
			
			reverse_inv = Friendlist()
			reverse_inv.invited = self.inviter.user
			reverse_inv.inviter = self.invited.get_profile()
			reverse_inv.status = 'A'
			reverse_inv.save()
		
	def delete_friendship (self):
		Friendlist.objects.filter (inviter=self.invited.get_profile(), invited=self.inviter.user).delete()
		Friendlist.objects.filter (inviter=self.inviter, invited=self.invited).delete()
		
			
	@staticmethod		
	def del_friendship (user1, user2):
		Friendlist.objects.get(inviter=user1.get_profile(), invited=user2).delete()
		Friendlist.objects.get(inviter=user2.get_profile(), invited=user1).delete()		
		



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
