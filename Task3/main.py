import math
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! Good to see you'

@app.route('/numbericalintegralservice/<lower>/<upper>')
def integral(upper, lower):
    n = [10, 100, 100, 1000, 10000, 100000, 1000000]
    result = ""
    try:
        for i in n:
            dx = (float(upper)-float(lower))/i
            integral = 0.0

            for y in range(i):
                x_i = dx*(y+0.5)
                dI = abs(math.sin(x_i))*dx
                integral+=dI

            result += f'for n={i} result={integral} </br>'

        return result
    except:
        return "an error occured."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


