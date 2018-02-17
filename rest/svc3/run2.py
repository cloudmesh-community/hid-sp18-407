from eve import Eve
from computer import Computer
import platform
import psutil
import json
from flask import Response

app = Eve()
@app.route('/computer', methods=['GET','POST'])

def computerInfo():
	
	compInfo = Computer("8GB", "201GB", "1s")
	cdata = json.dumps(compInfo.__dict__)
	response = Response()
	response.headers["status"] = 200
	response.headers["Content-Type"] = "application/json; charset=utf-8"
	response.data=cdata
	return response
	# return "My name is John"

if __name__ == '__main__':
	app.run()
