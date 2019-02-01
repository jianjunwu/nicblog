#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/02/01 16:23:05
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
import os
from flask import Flask
from app.configs import config
from app.blueprints.ping import ping_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_blueprints(app)
    return app
    


def register_blueprints(app: Flask):
    app.register_blueprint(ping_bp)
