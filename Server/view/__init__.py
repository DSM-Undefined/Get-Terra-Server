from datetime import datetime
import os
import threading
import time

from flask import request, Flask, current_app, abort, jsonify
from flask_restful import Api
from flask_jwt_extended.exceptions import NoAuthorizationError
from werkzeug.exceptions import HTTPException


class Util:

    def reload_server(self):
        time.sleep(2)

        os.system('. ../hook.sh')

    def webhook_event_handler(self):
        if request.headers['X-GitHub-Event'] == 'push':
            threading.Thread(target=self.reload_server).start()

        return 'hello'

    def time_check(self):
        if 'solve' in request.path or 'rank' in request.path or 'web' in request.path:
            if datetime.now() < current_app.config['START_TIME']:
                abort(406)
            if current_app.config['END_TIME'] < datetime.now():
                abort(412)

    def exception_handler(self, e):
        print(e)

        if isinstance(e, HTTPException):
            description = e.description
            code = e.code
        else:
            description = ''
            code = 500

        return jsonify({
            'msg': description
        }), code


class Router(Util):
    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def register(self):
        self.app.add_url_rule('/hook', view_func=self.webhook_event_handler, methods=['POST'])
        self.app.before_request(self.time_check)
        self.app.register_error_handler(Exception, self.exception_handler)

        from view.account.auth import Auth
        from view.account.signup import Signup
        self.api.add_resource(Auth, '/auth')
        self.api.add_resource(Signup, '/signup')

        from view.map.map import AndroidMap, WebMap
        from view.map.rank import Rank
        self.api.add_resource(AndroidMap, '/map/android')
        self.api.add_resource(WebMap, '/map/web')
        self.api.add_resource(Rank, '/rank')

        from view.solve.solve import Solve
        self.api.add_resource(Solve, '/solve/<boothName>')

        from view.team.team import Team
        self.api.add_resource(Team, '/team')

        from view.booth import Booth
        self.api.add_resource(Booth, '/booth')

        from view.init import InitGame
        self.api.add_resource(InitGame, '/init')
