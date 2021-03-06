from app import create_app

from model.booth import BoothModel
from model.team import TeamModel
from random import choice


app = create_app()


@app.route('/test')
def a():
    teams = TeamModel.objects(teamName__ne='empty')
    for booth in BoothModel.objects():
        t = choice(teams)
        booth.own_team = t
        booth.save()
    return '', 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=1234)
