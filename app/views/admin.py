#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import BaseConfig
from app.models import User
from app.models import VisitorLog
from app.config import logger
from functools import wraps
from flask import Blueprint
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request
from flask import make_response
from flask import g

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['POST', 'GET'])
def login():
    '''登陆'''
    method = request.method
    if method.lower() == 'get':
        return render_template('login.html')

    user = User.query_by_id(68719477421)
    g.current_user = user
    logger.debug(g.current_user)
    res = make_response(render_template('index.html'))
    res.set_cookie(BaseConfig.HEAD_AUTHORIZATION, user.name)
    return res


@admin_bp.route('/index')
def index():
    args = dict(request.args) or {}
    user = User.query_by_id(68719477421)
    g.current_user = user
    logger.debug(g.current_user)
    visitors = VisitorLog.query_items(**args)
    return render_template('index.html', visitors=visitors)

@admin_bp.route('/visitor_log')
def list_visitor_log():
    args = dict(request.args) or {}
    user = User.query_by_id(68719477421)
    g.current_user = user
    logger.debug(g.current_user)
    visitors = VisitorLog.query_items(**args)
    return render_template('admin/visitor_log_list.html', visitors=visitors)
