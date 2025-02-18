from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

class ExampleHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            'data': 'Hello from the server extension!'
        }))

def setup_handlers(web_app):
    print("%%%%%%%%%%%%% HAndler setup %%%%%%%%%%%%%%%%")
    host_pattern = ".*$"
    base_url = web_app.settings['base_url']
    route_pattern = url_path_join(base_url, 'myextension', 'example')
    handlers = [(route_pattern, ExampleHandler)]
    web_app.add_handlers(host_pattern, handlers)

