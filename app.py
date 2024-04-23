from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'data analyst',
    'location':'hyderabad',
    'salary': '2000'

  },
  {
    'id':2,
    'title':'data analyst',
    'location':'hyderabad',
    'salary': '2000'

  },
  {
    'id':3,
    'title':'data analyst',
    'location':'hyderabad',
    'salary': '2000'

  },
  {
    'id':4,
    'title':'data analyst',
    'location':'hyderabad',
    'salary': '2000'

  },
  


]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def api():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)