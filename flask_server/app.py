from flask import Flask, render_template, request

# Create app
app = Flask(__name__)


# Home page
@app.route("/", methods=['GET'])
def home():

    return "hello, world!"


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
