import json
from pprint import pprint
from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado
from notebook_labeling.nlp.hybrid_workflow_old import start_pipeline_hybrid


class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server

    @tornado.web.authenticated
    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        res = start_pipeline_hybrid(data, False, True)
        pprint(res)
        self.finish(json.dumps(res, indent=4, ensure_ascii=False))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "notebook-labeling", "label-notebook")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
