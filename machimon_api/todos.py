from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
import json, time

app = Flask(__name__)
api = Api(app)

ITEMS = {
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in ITEMS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return ITEMS[todo_id]

    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204
    #
    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return ITEMS

    def post(self):
        try:
            data = json.loads(request.data)
        except json.JSONDecodeError:
            abort(400, message="Invalid JSON body")

        #args = parser.parse_args()
        rec_id = int(time.time()*1000000)
#        todo_id = int(max(ITEMS.keys()).lstrip('todo')) + 1
#        todo_id = 'todo%i' % todo_id
        ITEMS[rec_id] = data
        return ITEMS[rec_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)