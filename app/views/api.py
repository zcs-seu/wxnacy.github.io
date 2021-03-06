#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from wwx import WXSecurity
from wwx import Message
from app.common.decorator import args_required
from app.common.decorator import response_xml
from app.config import BaseConfig
from app.config import logger
from app.models import AutoId
from app.models import User
from app.models import VisitorLog
from app.models import Article
from functools import wraps
from flask import Blueprint
from flask import request
import json

api_bp = Blueprint('api', __name__)

wxs = WXSecurity(BaseConfig.WX_TOKEN, BaseConfig.WX_ENCODING_AES_KEY)


@api_bp.route('/auto_id/<int:shard_id>/<int:item_id>', methods=['POST'])
def create_auto_id(shard_id, item_id):
    '''生成id'''
    id = AutoId.generate_id(shard_id, item_id)
    return BaseResponse.return_success({"id": id})

@api_bp.route('/visitor_log', methods=['POST'])
def create_visitor_log():
    '''生成访问记录'''
    args = request.json
    headers = request.headers
    ua = headers.get('user_agent')
    args['user_agent'] = ua
    res = VisitorLog.visit(**args)
    return BaseResponse.return_success(res.format())

@api_bp.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    '''更新文章'''
    res = Article.query_by_id(id)
    res.crawler_self()
    return BaseResponse.return_success(res.format())

@api_bp.route('/article', methods=['post'])
def crawler_article():
    '''创建'''
    args = request.json
    url = args['url']
    res = Article.crawler(url=url)
    return BaseResponse.return_success(res.format())

@api_bp.route('/login', methods=['post'])
@args_required('email', 'password')
def login():
    '''登录'''
    args = request.json
    s, item = User.login(**args)
    if s != 200:
        return BaseResponse.return_response(status=s, message=item)
    return BaseResponse.return_response(data = item, headers = {
        BaseConfig.HEAD_AUTHORIZATION: item.authorization
        })

@api_bp.route('/register', methods=['post'])
@args_required('email', 'password')
def register():
    '''注册'''
    args = request.json
    s, item = User.register(**args)
    if s != 200:
        return BaseResponse.return_response(status=s, message=item)
    return BaseResponse.return_response(data = item, headers = {
        BaseConfig.HEAD_AUTHORIZATION: item.authorization
    })

@api_bp.route('/wx/mp_callback', methods=['POST', 'GET'])
@response_xml
def wx_callback():
    '''测试'''
    method = request.method
    args = request.args
    signature = args['signature']
    timestamp = args['timestamp']
    nonce = args['nonce']

    if method == "GET":
        logger.debug('ss')
        if wxs.check_request(signature = signature,
                timestamp = timestamp, nonce = nonce):
            return args.get('echostr', 'success')
        else:
            return 'error'

    if method == "POST":
        msg_signature = args['msg_signature']
        data_json = Message.xml2dict(request.data)
        res = wxs.decrypt_security_body(data_json['xml']['Encrypt'], msg_signature,
                timestamp, nonce)
        logger.debug(f'解析结果: {res}')
        if res:
            msg = Message(res)
            if msg.is_text():
                return msg.reply_text(msg.content)
            elif msg.is_image():
                return msg.reply_image(msg.media_id)
            elif msg.is_video():
                return msg.reply_video(media_id = msg.media_id,
                    title = '视频标题', description="描述")
        else:
            return msg.reply_text(res)

    return ''

@api_bp.route('/wapi/test', methods=['POST', 'GET', 'PUT', "DELETE"])
def wapi_test():
    '''测试'''
    res = {}
    res.update(dict(path= request.path))
    res.update(dict(method= request.method))
    res.update(dict(args= request.args))
    res.update(dict(json= request.json))
    res.update(dict(form= request.form))
    res.update(dict(headers= dict(request.headers)))
    return BaseResponse.return_success(res)
