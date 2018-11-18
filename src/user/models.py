from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Using a custom user model when starting a project
    If you’re starting a new project, it’s highly recommended to set up a
    custom user model, even if the default User model is sufficient for you.
    This model behaves identically to the default user model, but you’ll be
    able to customize it in the future if the need arises:
    """
    # Store user's openid which grabed from wechat api
    openid = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="openID",
        unique=True,
        editable=False,
        error_messages={
            'unique': 'an openid is not allow to be repeated!',
        }
    )
    # Phone number could be also used to login a user
    phone = models.CharField(
        max_length=11,
        verbose_name='phone number',
        unique=True,
        null=True,
        blank=True,
    )
    # Nickname from wechat api
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name='nick name')
    # Head image from wechat api
    headimgurl = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Profile(models.Model):
    """
    Profile model extends builtin User Model
    user    OneToOne Relationship to User
    image   User Profile image
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile.'

    class Meta:
        verbose_name = '头像'
        verbose_name_plural = '头像'


class Stuff(models.Model):
    '''
    Our stuff was first define here
    extend the possibility of our User model, like normal user
    our stuff could have their count in our backend
    '''
    POSITION = (
        (0, '未指定'),
        (1, '前台'),
        (2, '设计师'),
        (3, '安装服务')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.IntegerField(choices=POSITION, default=0)

    def __str__(self):
        return f'{self.position} - {self.user.username}'

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'
