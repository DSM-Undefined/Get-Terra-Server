from flask_restful import Api


class Router:
    def __init__(self, app):
        self.app = app
        self.api = Api(app)

    def register(self):
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
