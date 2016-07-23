import httplib

from flask_restful import Resource

from deimos.db import DataAccess


class Build(Resource):
    @staticmethod
    def get(project_slug):
        build_id = DataAccess.get_build_id(project_slug)
        if build_id is None:
            return dict(message="Project {0} not exists".format(project_slug)), httplib.NOT_FOUND
        return {'build_id': int(build_id)}

    @staticmethod
    def post(project_slug):
        build_id = DataAccess.get_next_build_id(project_slug)
        return dict(project=project_slug, build_id=build_id)

    @staticmethod
    def delete(project_slug):
        DataAccess.clear_build_id(project_slug)
        return dict(project=project_slug)
