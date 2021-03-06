import pylab
from random import normalvariate, uniform

def generate_data(n, generator_type):
    epsilon_values = []   
    for i in range(n):
        e = uniform(0, 1) if generator_type == 'U' else normalvariate(0, 1)
        epsilon_values.append(e)
    return epsilon_values

data = generate_data(100, 'U')
pylab.plot(data, 'b-')
pylab.show()
