"""
1. Would placing the drunk's starting location not at the origin change the distances returned?
-> No

2. If so, what line would you modify to compensate? Enter the line number (eg 17). If not, just type None.

    1. def simWalks(numSteps, numTrials, dClass):
    2.     homer = UsualDrunk()
    3.     notOrigin = Location(1, 0)
    4.     distances = []
    5.     for t in range(numTrials):
    6.         f = Field()
    7.         f.addDrunk(homer, notOrigin)
    8.         distances.append(round(walk(f, homer, numSteps), 1))
    9.     return distances
    
    -> None

2. If you were going to use random.seed in a real-life simulation instead of just when you are debugging a simulation, would you want to seed it with 0?
-> No
"""