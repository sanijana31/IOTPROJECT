import time
from flask import Flask,request,render_template,url_for
import Simulator as sim
app=Flask(__name__)
simu=sim.simulator()
@app.route('/',methods=['GET','POST'])
def index():
    data1=""
    data2=""
    data3=""
    if(request.method=="POST"):
        s=request.form["s"]
        if(s=="submit"):
            stop_threads = False
            max_res=request.form['max_res']
            min_res=request.form['min_res']
            simu.start(max_res,min_res,stop_threads)
            time.sleep(.5)
            data1=simu.live_data
            time.sleep(.5)
            data2=simu.live_data
            time.sleep(.5)
            data3=simu.live_data

        elif(s=="end"):
            stop_threads=True
            simu.stop(stop_threads)
    return render_template("index.html",data1=data1,data2=data2,data3=data3)
@app.route('/stop')
def stop():
    data=simu.live_data
    return render_template("a.html")
if __name__=="__main__":
    app.run(debug=True)