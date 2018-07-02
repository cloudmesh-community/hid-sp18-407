from eve import Eve
from computer import Computer
import platform
import psutil
import json
from flask import Response

app = Eve()
@app.route('/times', methods=['GET'])
def times():
	timeInfo = str(psutil.cpu_times())
	#cdata = json.dumps(timeInfo.__dict)
	#response = Response()
	#response.headers["status"] = 200
	#response.headers["Content-Type"] = "application/json; charset=utf-8"
	#response.data = cdata
	return timeInfo
  
@app.route('/computer', methods=['GET','POST'])
def computerInfo():
	# "Here's my computer info"
	compInfo = Computer("24GB", "201GB", "1s")
	cdata = json.dumps(compInfo.__dict__)
	response = Response()
	response.headers["status"] = 200
	response.headers["Content-Type"] = "application/json; charset=utf-8"
	response.data=cdata
	return response

if __name__ == '__main__':
	app.run()

# computerInfo()
