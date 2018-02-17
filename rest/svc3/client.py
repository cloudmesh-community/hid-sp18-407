import requests
import json

def get_all():
	response = requests.get("http://127.0.0.1:5000/computer")
	print json.dumps(response.json(), indent=4, sort_keys=True)

def save_record():
	headers = {
		'Content-Type': 'application/json',
	}

	data = '{"RAM":"16GB","memory":"1TB","time":"1s"}'

	response = requests.post('http://localhost:5000/computer/',
				headers=headers,
				data=data)

	print(response.json())

#save_record()
get_all()
