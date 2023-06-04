import math
from random import randint

# Config file for n-body simulator storing objects, format (mass, x, y, vx, vy, name, colour)

# Earth, moon and object in L4 point of Earth-Moon system
EML4 = {'bodies': [[5.972*(10**24), 0, 0, 0, 0, 'Earth', 'blue'],# earth
                   [7.3479*(10**22), 384400000, 0, 0, 1022, 'Moon', 'grey'], # moon
                   [1000, 384400000+1737000+10000000, 0, 0, 1800, 'Moon orbiter', 'red'], # moon orbiter
                   [1000, 384400000 + 384400000*math.cos(math.radians(60)), 0, 0, -1022 + 384400000*math.sin(math.radians(60)), 'Object', 'red']], # object
        'frame': [-384400000, 384400000]}

# Solar system with planets and halley's comet
SS = {'bodies': [[1.989*(10**30), 0, 0, 0, 0, 'Sun', 'yellow'], # sun
                 [3.285*(10**23), 57910000000, 0, 0, 47870, 'Mercury', 'grey'], # mercury
                 [4.867*(10**24), 108200000000, 0, 0, 35020, 'Venus', 'orange'], # venus
                 [5.972*(10**24), 149600000000, 0, 0, 29780, 'Earth', 'blue'], # earth
                 [6.39*(10**23), 227900000000, 0, 0, 24130, 'Mars', 'red'], # mars
                 [1.898*(10**27), 778500000000, 0, 0, 13070, 'Jupiter', 'brown'], # jupiter
                 [5.683*(10**26), 1433000000000, 0, 0, 9690, 'Saturn', 'yellow'], # saturn
                 [8.681*(10**25), 2877000000000, 0, 0, 6810, 'Uranus', 'blue'], # uranus
                 [1.024*(10**26), 4503000000000, 0, 0, 5430, 'Neptune', 'blue'], # neptune
                 [1.309*(10**22), 5906000000000, 0, 0, 4740, 'Pluto', 'grey']], # pluto
      'frame': [-5906000000000, 5906000000000]} 


# Dust cloud with 50 asteroids and nothin else
DC = {'bodies': [],
       'frame': [-10000000000000, 10000000000000]}
for i in range(20):
    DC['bodies'].append([100000, randint(-5000000000, 5000000000), randint(-5000000000, 5000000000), 0, 0, 'Asteroid', 'grey'])

# Earth, moon and apollo 11 service module heading to moon on free return trajectory
ERT = {'bodies': [[5.972*(10**24), 0, 0, 0, 0, 'Earth', 'blue'], # earth   
                  [7.3479*(10**22), 384400000, 0, 0, 1022, 'Moon', 'grey'], # moon
                  [28800, 384400000+1737000, 0, 0, 1022+1070, 'Apollo 11', 'red']], # apollo 11
        'frame': [-384400000, 384400000]}

# Earth, moon and cloud of 20 objects in between earth and moon
EMC = {'bodies': [[5.972*(10**24), 0, 0, 0, 0, 'Earth', 'blue'], # earth
                  [7.3479*(10**22), 384400000, 0, 0, 1022, 'Moon', 'grey']], # moon
       'frame': [-384400000, 384400000]}
for i in range(20):
    EMC['bodies'].append([1000, 150000000 + randint(-100000000, 100000000), 0, 0, -2022, 'Object', 'red'])
