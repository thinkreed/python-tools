#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import itchat
from itchat.content import *


@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    match = re.search(u'高超', msg['Text']).span()
    user_dict = [u'去玩耍…', u'test']
    chatroom = itchat.search_chatrooms(userName=msg['ToUserName'])
    if match and chatroom['NickName'] in user_dict:
        itchat.send((u'pua大师在此'), msg['ToUserName'])


@itchat.msg_register([TEXT], isFriendChat=True)
def text_reply(msg):
    match = re.search(u'高超', msg['Text']).span()
    user_dict = [u'认真的苇草', u'黄哲毅', u'A·志敏.拉卡拉)', u'姜博']
    friend = itchat.search_friends(userName=msg['FromUserName'])
    if match and friend['NickName'] in user_dict:
        itchat.send((u'pua大师在此'), msg['FromUserName'])


@itchat.msg_register([PICTURE], isFriendChat=True)
def picture_reply(msg):
    user_dict = [u'黄哲毅']
    friend = itchat.search_friends(userName=msg['FromUserName'])
    if friend['NickName'] in user_dict:
        itchat.send((u'给pua大师发图干啥'), msg['FromUserName'])


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()
