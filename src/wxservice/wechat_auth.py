from django.conf import settings
from django.contrib.auth.hashers import check_password
from user.models import User
# User = settings.AUTH_USER_MODEL


class WechatOpenidAuth:
    '''
    微信openid认证登录
    '''

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request=None, openid=None, nickname=None, headimgurl=None):
        try:
            user = User.objects.get(openid=openid)
            if user is not None:
                return user
        except User.DoesNotExist:
            user = User(openid=openid, username=nickname, nickname=nickname, headimgurl=headimgurl)
            # user.is_staff = True
            user.save()
            return user

        return None
