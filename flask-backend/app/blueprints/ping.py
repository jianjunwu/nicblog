#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ping.py
@Time    :   2019/02/01 16:27:42
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
from flask import Blueprint, jsonify

ping_bp = Blueprint('ping', __name__)


@ping_bp.route('/ping/')
@ping_bp.route('/ping')
def ping():
    return jsonify("pong!")
