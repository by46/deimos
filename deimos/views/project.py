from flask_restful import Resource

from deimos.db import DataAccess


class Projects(Resource):
    @staticmethod
    def get():
        return DataAccess.get_projects()


class Project(Resource):
    @staticmethod
    def delete(project_slug):
        DataAccess.delete_projects(project_slug)
        return dict(project=project_slug)
