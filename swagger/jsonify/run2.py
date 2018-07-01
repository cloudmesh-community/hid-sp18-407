from eve import Eve
from flask import jsonify
import os
import getpass

app = Eve ()

@app.route('/student/gregor')
def gregors_information():
    data = {
        'firstname': 'Gregor',
        'lastname': 'von Laszewski',
        'university': 'Indiana University',
        'email': 'gregor@example.com'
        }
    try:
        data['username'] = getpass.getuser()
    except:
        data['username'] = 'not-found'
    return jsonify(**data)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
