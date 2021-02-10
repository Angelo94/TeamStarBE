from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Team(models.Model):
    name = models.CharField("team name", max_length=100)
    target_name = models.CharField("target name", max_length=100)
    target_max = models.IntegerField("target max", default=5)

    def __str__(self):
        return self.name

class UserTeamAssignment(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    is_team_admin = models.BooleanField("is team admin", default=False)
    star_counter = models.IntegerField("star counter", default=0)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    class Meta:
        unique_together = ('team', 'user',)

    def __str__(self):
        return "User {} {} in {} team".format(self.user.first_name, self.user.last_name, self.team.name)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)