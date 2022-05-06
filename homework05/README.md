# Flask & Redis Servers

In this file we extend our usage of flask servers and add a new server, called a Redis server. We explore the capabilities of both Flask and Redis.

## Description
Starting from our folder in isp02, we pull the redis:6 image and install it.
```
docker pull redis:6
```

We start our redis server, making sure to run it in the background using the -d tag/

```
docker run -p 6410:6379 dilipyy-redis redis:6
```
6410:6379 is the connection of our port to the default redis port.
Note that 6410 is my assigned port so yours might be different

To mount a folder to the /data folder that saves 1 bit of  data to the backup every second we call:
```
docker run -d -p 6410:6379 -v $(pwd)/data:/data:rw --name=dilipyy-redis redis:6 --save 1 1
``` 
In the second part of the file, we use flask to interact with the redis server.

To do this, we make sure to import redis in our flask file. We then create a file that reads in data from a json file to a redis server for POST requests, and reads out data from a redis server for GET requests.

To test this, in another terminal section, we open a flask server from our app.py file for the redis server to interact with.

```
Flask run -p 5010
```
Then from the unused terminal we can call commands to either POST or GET from the Flask server which will followup accordingly with the Redis server.

For example
```
curl -x POST localhost:5010/data
```

will result in the Flask object reading in data from ML_Data_Sample.json to the redis server.

Likewise, a GET request,
```
curl localhost:5010
```
will result in the Flask object reading from the redis server and outputting the data in json format. This is accomplished using jsonify.

All of this can then be put into the Dockerfile(the calls for the redis server are within app.py) which then allows the set of files to run separately.

### Dependencies

* Running these files requires: python3, pytest, Redis, Flask, GitHub, and Docker
### Installing

* To install redis type:
```
pip3 install --user redis
```
in the commandline (requires python3)
* redis:6 can be pulled with docker using:
```
docker pull redis:6
```
* Meteorite Sampling Data
[ML_Data_Sample.json](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json)


### Executing program

* To run this file, log into the isp02.tacc.utexas.edu server. It is much easier to complete the tasks in the remote server. Then follow the steps in the description
```
ssh taccid@isp02.tacc.utexas.edu
```