from flask import Flask,request,jsonify
import redis
import json

app = Flask(__name__)

@app.route('/data', methods = ['GET','POST'])
def data():	
	r = get_redis_client()
	input = 'ML_Data_Sample.json'
	with open(input,'r') as f:
		response = json.load(f)
		data_dump = json.dumps(response)	
		if request.method == 'POST':
			r.set('data',data_dump)
			return 'Success\n'
		if request.method == 'GET':
			r.set('data',data_dump)
			a = json.loads(r.get('data'))
			b = jsonify(a)
			return b

def get_redis_client():
	return redis.Redis(host='172.17.0.8', port=6379)

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
