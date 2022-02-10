import json
import math
mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

with open('jsonData.json') as json_file:
    data = json.load(json_file)

speed = 10
leg = 0
totalTime = 0

holderList = data['sites']

origLat = 16.0
origLong = 84.0
latHold = 0
longHold = 0
sampleTime = 0
travelTime = 0

for i in range(0,5):
    lister = []
    holderDict = {}
    leg = leg +1
    holderDict = holderList[i]
    holderLat = holderDict['latitude']
    latVal = holderLat[0]
    holderLong = holderDict['longitude']
    longVal = holderLong[0]
    s = 'leg = '+ repr(leg)
    lister.append(s)
    print(i)
    if i == 0:
        travelTime = calc_gcd(origLat,origLong,latVal,longVal)/speed
    else:
        travelTime = calc_gcd(latHold, longHold, latVal,longVal)/speed
    t = 'travel time is ' + repr(travelTime) + ' hr'
    lister.append(t)
    comp = holderDict['composition']
    if comp[0] == 'iron':
        sampleTime = 1
    elif comp[0] == 'stony':
        sampleTime = 2
    elif comp[0] == 'stony-iron':
        sampleTime = 3
    u = 'sample time is ' + repr(sampleTime) + ' hr'
    lister.append(u)
    print(lister)
    latHold = holderDict['latitude'][0]
    longHold = holderDict['longitude'][0]
    totalTime = travelTime + sampleTime + totalTime

print('number of legs = ' + repr(leg))
print('total time elapsed = ' + repr(totalTime) + ' hr')


