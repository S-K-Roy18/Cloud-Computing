from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cloud Computing Lab 8</title>
</head>
<body>
    <h1>Cloud Computing Lab 8</h1>
    <p>Application successfully implemented using Google App Engine.</p>
    <p>This application demonstrates Platform as a Service (PaaS).</p>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
