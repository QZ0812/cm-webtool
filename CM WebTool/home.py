from flask import Flask, render_template,url_for,redirect,request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/server')
def server():
    return render_template('server.html',title='Server')

@app.route('/server/production')
def production():
    from static import check_production_log
    logcommand=""
    output=check_production_log.check_log(logcommand)
    return render_template('server/production.html',title='Server',output=output)

@app.route('/server/stagingQA')
def stagingQA():
    return render_template('server/stagingQA.html',title='Server')

@app.route('/server/production/start')
def start():
    # import sys
    # import subprocess
    # python_executable = sys.executable.replace("pythonw", "python")
    # subprocess.check_call("{} -m pip install --user --upgrade --no-warn-script-location paramiko".format(python_executable))
    from static import start_production_a_server
    start_production_a_server.start_server()
    print("Just want to test if this script can run or not")
    return redirect(url_for('production'))

@app.route('/www')
def web_server():
    return render_template('www.html',title='Webserver')

@app.route('/cdn')
def CDN():
    return render_template('cdn.html',title='CDN')

@app.route('/GD')
def game_design():
    return render_template('gamedesign.html',title='GameDesign')

@app.route('/art')
def art():
    return render_template('art.html',title='Art')

@app.route('/data')
def data():
    return render_template('data.html',title='Data')

if __name__ == "__main__":
    app.run(debug=True)
    