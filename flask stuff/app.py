from flask import Flask, render_template, request
import subprocess as sp
import os
from main import run_tim

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static')

@app.route('/', methods=["GET", "POST"])

def index():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Run Tim!') == "VALUE1":
            run_tim()
        elif request.form.get("Close Tim!") == "VALUE2":
        #     pass
        # else:
            import main
            sp.Popen.terminate(main) # closes the process
    
    elif request.method == "GET":
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tim_blush.gif')
        return render_template('index.html', user_image=full_filename)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
#app.run('0.0.0.0', port=81, debug=True)