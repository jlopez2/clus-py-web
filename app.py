from flask import Flask

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!!"


#if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0')

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': ‘James’}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

