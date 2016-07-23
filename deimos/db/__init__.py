import redis
from flask import g

from deimos import app


def get_db():
    if not hasattr(g, 'redis'):
        g.redis = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])

    return g.redis


PROJECTS = 'deimos:projects'


class DataAccess(object):
    @staticmethod
    def get_build_id(project_slug):
        # TODO(benjamin): add generate build id
        project_slug = project_slug.lower()
        conn = get_db()
        key = 'deimos:build:{0}'.format(project_slug)
        return conn.get(key)

    @staticmethod
    def get_next_build_id(project_slug):
        project_slug = project_slug.lower()

        conn = get_db()
        conn.sadd(PROJECTS, project_slug)
        key = 'deimos:build:{0}'.format(project_slug)
        build_id = conn.incr(key, 1)
        return build_id

    @staticmethod
    def clear_build_id(project_slug):
        project_slug = project_slug.lower()
        conn = get_db()

        key = 'deimos:build:{0}'.format(project_slug)
        conn.set(key, 0)

    @staticmethod
    def get_projects():
        conn = get_db()
        return list(conn.smembers(PROJECTS))

    @staticmethod
    def delete_projects(project_slug):
        conn = get_db()
        pipe = conn.pipeline()
        pipe.srem(PROJECTS, project_slug)
        key = 'deimos:build:{0}'.format(project_slug)
        pipe.delete(key)
        pipe.execute()
