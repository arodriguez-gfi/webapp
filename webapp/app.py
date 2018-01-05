from flask import Flask

app = Flask(__name__)

def suma(a,b):
	return a+b

@app.route('/')
def hello():
    res = suma (2,3)
    return 'Hello world! %s' % (res)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=5000)
