from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from CI/CD Pipeline deployed to Minikube!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7071)
