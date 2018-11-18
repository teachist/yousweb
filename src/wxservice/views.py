# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View

from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.messages import TextMessage
from wechatpy.replies import TextReply, ImageReply, VoiceReply, VideoReply, ArticlesReply, EmptyReply

from . import clients  # Wechat API client
from user.models import User
from django.contrib.auth import login, authenticate


class WxServiceView(View):
    _WEIXIN_TOKEN = 'verify'

    def get(self, request):
        # redirect_uri = f'http://{request.get_host()}{reverse("wx-login")}'
        # client = clients.create_menu(redirect_uri)
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = self._WEIXIN_TOKEN
        try:
            check_signature(token, signature, timestamp, nonce)
            return HttpResponse(echostr)
        except InvalidSignatureException:
            return HttpResponse('Invalid Signature Exception')

    @csrf_exempt
    def post(self, request):
        xml = request.body
        msg = parse_message(xml)
        if msg.type == 'text':
            # 获取文本内容
            try:
                content = msg.content
                # print(res)
                # print(json.dump(res))
                reply = TextReply(content=content, message=msg)
                r_xml = reply.render()
                # 获取唯一标记用户的openid，下文介绍获取用户信息会用到
                openid = msg.source
                # print(openid)
                return HttpResponse(r_xml)
            except Exception as e:
                # 自行处理
                return HttpResponse('success')
            # return HttpResponse('')
        elif msg.type == 'image':
            print(msg.image, msg.media_id)
            reply = ArticlesReply(message=msg)

            reply.add_article({
                'title': 'Welcome tom my channel!',
                'description': 'Finally, we meet you here,\nYou must know you are very important for us!',
                'image': msg.image,
                'url': 'https://baidu.com'
            })
            r_xml = reply.render()
            return HttpResponse(r_xml)
        elif msg.type == 'voice':
            print(msg.format, msg.recognition)
            reply = VoiceReply(media_id=msg.media_id, message=msg)
            return HttpResponse(reply.render())
        elif msg.type == 'video':
            print(msg)
            print(msg.media_id, msg.thumb_media_id)
            reply = VideoReply(media_id=msg.media_id, title='Test video', description='Description', message=msg)

            return HttpResponse(reply.render())
        elif msg.type == 'location':
            print(msg.location_x, msg.location_y, msg.scale, msg.label, msg.location)
            return HttpResponse('Success')

        elif msg.type == 'event':
            # print(msg.type)
            if msg.event == 'subscribe':
                try:
                    reply = TextReply(content='Welcome to my channel', message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'unsubscribe':
                try:
                    reply = TextReply(content='See you again!', message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'subscribe_scan':
                try:
                    print(msg.scene_id, msg.ticket)
                    reply = TextReply(content='See you again!', message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'scan':
                try:
                    print(msg.scene_id, msg.ticket)
                    reply = TextReply(content='See you again!', message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'location':
                try:
                    print(msg.latitude, msg.longitude, msg.precision)
                    reply = TextReply(content='See you again!', message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'click':
                try:
                    print(msg.key)
                    reply = TextReply(content=msg.key, message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')
            elif msg.event == 'view':
                try:
                    print(f'{msg.url}\n=========')
                    reply = TextReply(content=msg.url, message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except:
                    return HttpResponse('Success')


def login_page(request):
    if request.method == "GET" and request.GET.get("code") and not request.user.is_authenticated:
        """
        Create a new user if the user doesn't exist
        when the user in our database, just login the user
        """
        redirect_uri = f'http://{request.get_host()}{reverse("wx-login")}'
        client = clients.web_authorize(redirect_uri)

        code = request.GET.get("code", None)
        res = client.fetch_access_token(code)
        res = client.get_user_info()

        openid = res['openid']
        nickname = res['nickname']
        headimgurl = res['headimgurl']
        user = authenticate(request=request, openid=openid, nickname=nickname, headimgurl=headimgurl)

        if user is not None:
            login(request, user)
        else:
            print('You do not have permission to do this!')
            return redirect('login')
    context = {}
    return render(request, 'wxservice/profile.html', context=context)
