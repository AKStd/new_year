import os

from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(root_dir, "templates")
static_folder = os.path.join(root_dir, 'static')

static_conf = {
    'js': os.path.join(static_folder, "js"),
    'css': os.path.join(static_folder, "css"),
    'images': os.path.join(static_folder, "images"),
}

app = Flask(__name__, template_folder=template_folder)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static/<_type>/<path:path>")
def send_static(_type, path):
    return send_from_directory(static_conf[_type], path)


if __name__ == "__main__":
    app.run(debug=True)
