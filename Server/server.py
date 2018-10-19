from app import create_app

from model.Booth import BoothModel
from model.Team import TeamModel
from random import choice


app = create_app()


@app.route('/test')
def a():
    teams = TeamModel.objects(teamId__ne=-1)
    for booth in BoothModel.objects():
        t = choice(teams)
        booth.ownTeam = t
        booth.save()
    return '', 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=1234)
