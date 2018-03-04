from eve import Eve
from student import Student
import platform
import psutil
import json
from flask import Response



app = Eve()

@app.route('/student/john', methods=['GET'])

def theStudentJohn():
	
	studentInfo = Student("John", "Doe", "23", "ISE", "john@iu.edu")
	sdata = json.dumps(studentInfo.__dict__)
	response = Response()
	response.headers["status"] = 200
	response.headers["Content-Type"] = "application/json; charset=utf-8"
	response.data=sdata
	return response
	# return "My name is John"

if __name__ == '__main__':
	app.run()
