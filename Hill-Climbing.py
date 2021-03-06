# Implementation of Hill-Climbing
import random
import math

# domain for the solution
X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed

# function f(x) ****TEST FUNCTION HERE****
def f(x):
    return (6*x-2)**2 * math.sin(12*x-4)

# hill climbing loop stops when this condition is not met
def loop_condition_is_met(timeCounter, solution):
    timeLimit = 1000
    idealSolution = 15.91
    precision = 0.0001
    return timeCounter < timeLimit and\
         abs(idealSolution - f(solution)) > precision

def randomly_tweaked(solution):
    tweakRange = 0.001
    return solution + random.uniform(-tweakRange, tweakRange)

# Hill-Climbing main function
def hill_climbing():
    solution = random.uniform(X_MIN, X_MAX) # some initial candidate solution
    timeCounter = 0 # time counter that increments every loop
    # repeat until S is the ideal solution or we have run out of time
    while loop_condition_is_met(timeCounter, solution):
        randomSolution = randomly_tweaked(solution)
        if f(randomSolution) > f(solution):
            solution = randomSolution
        # increment timeCounter
        timeCounter += 1
    # print the "global" solution
    print "Hill-Climbing: " + str((round(solution, 3), round(f(solution), 3)))

# execute
hill_climbing()
