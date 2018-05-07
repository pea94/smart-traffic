from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    colors = ['#F14722', '#E67E22', '#F4D03F', '#27AE60']
    n_car = [100, 90, 80, 50]
    avg_speed = [40, 50, 60, 70]
    return render_template('index.html', colors=colors, n_car=n_car, avg_speed=avg_speed)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
