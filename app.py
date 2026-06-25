from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This Python app is running on Azure without VS Code."

if __name__ == "__main__":
    app.run()
