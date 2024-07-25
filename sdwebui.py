# encoding:utf-8

import io
import json
import os

import webuiapi
import langid
from bridge.bridge import Bridge
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from config import conf
from plugins import *


@plugins.register(name="test", desc="测试用", version="0.0.1", author="shiwanli")
class SDWebUI(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[SD] inited")
    def on_handle_context(self, e_context: EventContext):
        group_name = e_context['group_name']
        logger.debug("[SD] on_handle_context. content: %s" %e_context['context'].content)
        logger.info("[SD] image_query={}".format(e_context['context'].content))
    def get_help_text(self, e_context: EventContext,verbose = False, **kwargs):
        help_text += f"使用方法:\n"
        help_text += "目前可用关键词：\n"
        group_name = e_context['group_name']
        help_text += group_name
        return help_text
