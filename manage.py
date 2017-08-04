from flask import Flask,jsonify,send_file,send_from_directory,make_response
import os,sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/flask')
def hello_flask():
    return 'Hello flask!'



tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/task', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/download', methods=['GET'])
def get_dowload():
    print(sys.argv[0])
    path = sys.argv[0]
    directory = os.path.split(path)[0]
    filename = os.path.split(path)[1]
    print(directory)
    print(filename)
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

