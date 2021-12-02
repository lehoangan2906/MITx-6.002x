# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.

import random
def deterministicNumber():
    return 10

# Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.

def stochasticNumber():
    return random.randRange(10, 21, 2)