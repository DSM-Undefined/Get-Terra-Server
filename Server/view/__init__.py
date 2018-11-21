from datetime import datetime
import os
import threading
import time

from flask import request, Flask, current_app, abort, jsonify
from flask_restful import Api


class Util:

    def reload_server(self):
        time.sleep(2)

        os.system('. ../hook.sh')

    def webhook_event_handler(self):
        if request.headers['X-GitHub-Event'] == 'push':
            threading.Thread(target=self.reload_server).start()

        return 'hello'


class Router(Util):
    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def register(self):
        self.app.add_url_rule('/hook', view_func=self.webhook_event_handler, methods=['POST'])

        from view.auth import AuthView
        self.api.add_resource(AuthView, '/auth/<int:gameKey>')

        from view.map import MapView
        self.api.add_resource(MapView, '/map')

        from view.solve import SolveView
        self.api.add_resource(SolveView, '/solve/<boothName>')

        from view.team import TeamView
        self.api.add_resource(TeamView, '/team')
