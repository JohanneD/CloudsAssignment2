import math

def integral(lower, upper):
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

            result += f'for n={i} result={integral} \n'

        return result
    except:
        return "an error occured."
