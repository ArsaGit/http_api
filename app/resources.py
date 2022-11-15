from flask_restful import Resource, reqparse, abort
import psycopg2
from .config import get_pg_url


act_parser = reqparse.RequestParser()
act_parser.add_argument("id", type=int, required=True)
act_parser.add_argument("comment", type=str)
act_parser.add_argument("accepted", type=bool)

work_parser = reqparse.RequestParser()
work_parser.add_argument("id", type=int, required=True)
work_parser.add_argument("agreed", type=bool, required=True)


db_uri = get_pg_url()


class EmergencyActResource(Resource):
    def patch(self):
        args = act_parser.parse_args()

        conn = psycopg2.connect(db_uri)
        cursor = conn.cursor()
        cursor.execute("select * from \"Emergency_acts\" where id = %s", (args['id'],))
        result = cursor.fetchone()
        if not result:
            abort(404, message="No act with such id")

        if args['comment']:
            cursor.execute("update \"Emergency_acts\" set ucomment = %s where id = %s", (args['comment'], args['id']))
        if args['accepted']:
            cursor.execute("update \"Emergency_acts\" set accepted = %s where id = %s", (args['accepted'], args['id']))
        conn.commit()
        cursor.close()
        conn.close()


class ScheduledWorkResource(Resource):
    def patch(self):
        args = act_parser.parse_args()

        conn = psycopg2.connect(db_uri)
        cursor = conn.cursor()
        cursor.execute("select * from \"Scheduled_works\" where id = %s", (args['id'],))
        result = cursor.fetchone()
        if not result:
            abort(404, message="No scheduled work with such id")

        if args['agreed']:
            cursor.execute("update \"Scheduled_works\" set agreed = %s where id = %s", (args['agreed'], args['id']))

        conn.commit()
        cursor.close()
        conn.close()


class HiRes(Resource):
    def get(self):
        return "I'm working"