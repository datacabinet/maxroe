import json
import os
import shutil
import datetime
from tornado import web
from jupyter_server.base.handlers import APIHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin
from jupyter_server.utils import url_path_join
from IPython import get_ipython
import traceback

ipython = get_ipython()
if ipython:
    ipython.magic("load_ext autoreload")
    ipython.magic("autoreload 2")


class MyHandler(APIHandler):
    async def get(self):
        try:
            response = {"message": "Hello from GET endpoint! from myhandler of server extension"}
            self.set_status(200)
            self.finish(json.dumps(response))
        except Exception as e:
            self.set_status(500)
            self.finish(json.dumps({"error": str(e)}))


def setup_handlers(app):
    base_url = app.base_url
    host_pattern = '.*$'
    app.web_app.add_handlers(host_pattern, [
        (url_path_join(base_url, 'api/maxroe'), MyHandler),
    ])


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("My extension is loading.")
    setup_handlers(nbapp)
