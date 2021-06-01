from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/search')
def search():
  return render_template("search.html")

@app.route('/rezervesana')
def rezervesana():
  return render_template("rezervesana.html")


app.run(host='0.0.0.0', port=8080)
