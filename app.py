from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
# 
    # the colors that are displayed as an ovelay (Baidu JS API object) 
    colors = ['#F14722', '#E67E22', '#F4D03F', '#27AE60']

    # There are over 20 data collection points we to collect the number of cars passing through each point and the average speed.

    #create list n_car to save the number of cars passing through each intersection.     
    n_car=[]
    for i in range(10):
        n_car.append(randint(0,50))

    #create array avg_speed save the average speed of cars passing through each intersection. 

    avg_speed=[]
    for i in range(10):
        avg_speed.append(randint(10,60))

    return render_template('index.html', colors=colors, n_car=n_car, avg_speed=avg_speed)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
