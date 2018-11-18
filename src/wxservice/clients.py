# -*- coding:UTF-8

from wechatpy import WeChatClient
from wechatpy.oauth import WeChatOAuth

app_id = 'wxfc5ca4f1a07c41ff'  # In producation mode it should be in the environ
secret = '75f7862e0ee63e663a9f0288dc15ae3d'
client = WeChatClient(app_id, secret)


def web_authorize(redirect_uri):
    return WeChatOAuth(app_id, secret, redirect_uri, scope='snsapi_userinfo')


def create_menu(redirect_uri):
    ''' 创建菜单'''
    my_authorize_url = web_authorize(redirect_uri).authorize_url
    client.menu.create({
        'button': [
            {
                "type": "view",
                "name": "下单吧",
                "url": my_authorize_url
            }
        ]
    })
