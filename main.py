from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "web site"
@app.route("/forbidden")
def forbidden():
    return "Access Denied!"
if __name__ == "__main__":
    app.run(debug=True)
