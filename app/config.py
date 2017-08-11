#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.id import Snowflake
from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix
import os
import logging

CONFIG_NAME_MAPPER = {
    'local': 'app.local_config.LocalConfig',
    'product': 'app.local_config.ProductionConfig',
    'dev': 'app.local_config.DevelopmentConfig',
    'test': 'app.local_config.TestingConfig'
}


class BaseConfig(object):
    DEBUG = False


    TYPE_ITEM_USER = 1
    TYPE_ITEM_IMAGE = 2
    TYPE_ACTION_VIEW = 21


    DEFAULT_PAGE = 1
    DEFAULT_PER_PAGE = 10

    MAX_START = 4638873600

    HEAD_AUTHORIZATION = 'authorization'

    ARTICLE_DIR = '{}/articles/'.format(os.getcwd())


    # 输出日志文件
    METRICS_LOG_FILE = './metrics.flask.log'
    # 地址前缀

    WX_MP_APP_ID = 'wxb5ae283f932d1ae0'
    WX_MP_APP_SECRET = '720233db12f8d6dadaa9979c49418e8d'
    WX_MP_ID = 'gh_96c685096fbd'


def create_app(flask_config_name=None):
    """
    创建配置
    :return:
    """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    config_mapper_name = flask_config_name or env_flask_config_name or 'local'
    config_name = CONFIG_NAME_MAPPER[config_mapper_name]
    app.config.from_object(config_name)
    print('-------------------------init app-------------------------')
    logging.basicConfig(filename=app.config['METRICS_LOG_FILE'],
                        level=logging.ERROR)
    #日志
    logHandler = logging.FileHandler('debug-{}.log'.format(date.today().isoformat()))
    logHandler.setLevel(logging.DEBUG)
    app.logger.addHandler(logHandler)
    app.logger.setLevel(logging.DEBUG)
    return app


app = create_app()
db = SQLAlchemy(app)
snowflake = Snowflake(0)
