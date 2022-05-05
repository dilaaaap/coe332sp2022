import random
import json
randomLat = []
randomLong = []
randomRock = []
siteid = []
dictList = []
dicts = {}
k = 'composition'
def tuple2dict(tup,di):
    for a,b in tup:
        di.setdefault(a, []).append(b)
    return di
siteHolder = 0

for i in range(0,5):
    sites = {}
    lister = []
    siteHolder = siteHolder +1
    n = ('siteid',siteHolder)
    lister.append(n)
    j = random.uniform(16.0,18.0)
    n = ('latitude',j)
    lister.append(n) 
    j = random.uniform(82.0,84.0)
    n = ('longitude',j)
    lister.append(n)
    j = random.randint(1,3)
    if j == 1:
        n = (k, 'stony')
        lister.append(n)
    elif j == 2:
        n = (k,'iron')
        lister.append(n)
 
    elif j == 3:
        n = (k,'stony-iron')
        lister.append(n)
    dictList.append(tuple2dict(lister,sites))

dicts['sites']= dictList

jsoner = json.dumps(dicts)
with open ('jsonData.json','w') as outfile:
    json.dump(dicts, outfile)
