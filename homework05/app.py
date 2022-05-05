from flask import Flask,request,jsonify
import redis
import json

app = Flask(__name__)

@app.route('/data', methods = ['GET','POST'])
def data():	
	r = get_redis_client()
	#input = 'ML_Data_Sample.json'
	#with open(input,'r') as f:
		#response = json.load(f)
		#data_dump = json.dumps(response)	
	if request.method == 'POST':
		r.set('value',200)
		return 'Success\n'
	if request.method == 'GET':
			#rd.set('data',response)
			#a = json.loads(rd.get('data'))
		return 'Here is your data:\n'
			#return a
		return r.get('value')

def get_redis_client():
	return redis.Redis(host='172.17.0.2', port=6379)

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
