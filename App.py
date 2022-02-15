from flask import Flask,jsonify,request


app = Flask(__name__)

tasks  =  [
    {
        "id":1,
        "title":u'Buy groceries',
        "description":u'Buy milk,fruits,cheese',
        "Done":False
    },
    {
        "id":2,
        "title":u'Learn python',
        "description":u'Find a good tutorial',
        "Done":False
    }
]


@app.route("/")

def hello_world():
    return "Hello World"

@app.route("/add-data",methods = ["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Pls provide the data"
        },400)
    task = {
        "id":tasks[-1]['id'],
        "title":request.json['title'],
        "description":request.json.get('description',""),
        "Done":False
    }
    tasks.append(task)
    return jsonify({
        "status":'Success',
        "message":"task added successfully"
    })
         
@app.route("/get-data")

def get_task():
    return jsonify({
        "data":tasks
    })


if(__name__=="__main__"):
    app.run(debug = True)



