from flask import Flask, render_template, url_for
from modules.screenshot import snapScreen
from modules.camera import webcamSnap
from os import chdir, path


app = Flask(__name__)
app_path = app.root_path

app_path = app.root_path
chdir(app_path)
print('Directory Changed')


@app.route('/')
def index():
    return render_template('share.html', webcam=url_for('static', filename="record/snap.png"), screen=url_for('static', filename="record/screen.png"))


@app.route('/api/record', methods=['POST'])
def record():
    # May need to change path
    snapScreen(path.join(app_path, "static/record/screen.png"))
    webcamSnap(path.join(app_path, "static/record/snap.png"))

    return 'Done'  # May need to change this too


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
