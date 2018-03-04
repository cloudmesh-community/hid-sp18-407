from eve import Eve
# from student import Student
import platform
import psutil
import json
from flask import Response

app = Eve()

@app.route('/times', methods=['GET'])
def times():
	times = {}
	alltimes = psutil.cpu_times('/')
	times['user'] = alltimes.user
	times['system'] = alltimes.system 
	times['idle'] = alltimes.idle

	return times

@app.route('/memory', methods=['GET'])
def memorystats():
	memory = {}
	allmem = psutil.virtual_memory('/')
	memory['totmem'] = allmem.total
	memory['availmem'] = allmem.available
	memory['usedmem'] = allmem.used
	memory['freemem'] = allmem.free
	
	return memory


if __name__ == '__main__':
	app.run()
