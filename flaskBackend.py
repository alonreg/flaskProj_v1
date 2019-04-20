from flask import Flask, render_template
app = Flask(__name__)

myDic = [
    {
        'author': 'alon',
        'title': 'Harry Potter'
    },
    {
        'author': 'keren',
        'title': 'Noah Hararrri'        
    }
]


@app.route("/")
def home(debug=True):
    return render_template('home.html', posts=myDic)

@app.route("/getSets")
def getSets(debug=True):
    return "SETS!!!!"

if __name__=='__main__':
    app.run(debug=True)