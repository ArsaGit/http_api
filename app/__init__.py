from flask import Flask
from flask_restful import Api
from .resources import EmergencyActResource, ScheduledWorkResource, HiRes


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(EmergencyActResource, '/emergency_acts')
    api.add_resource(ScheduledWorkResource, '/scheduled_works')
    api.add_resource(HiRes, '/')

    return app


app = create_app()