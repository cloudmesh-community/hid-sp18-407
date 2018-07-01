from flask import Flask, jsonify

from flasgger import Swagger
import os
from os import path

#

def files_in_dir(extra_dirs=['.',]):
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    return extra_files

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Clusters API',
    'uiversion': 2
}
Swagger(app, template_file='cluster.yaml')


@app.route('/clusters/<server>/')
def get_clusters(server):

    all_clusters = {
        'green': ['green00', 'green01', 'green02', 'green04'],
        'red': ['red00', 'red01', 'red02']
    }
    if server == 'all':
        result = all_clusters
    else:
        result = {server: all_clusters[server]}

    return jsonify(result)

if __name__ == "__main__":

    app.run(debug=True,
            extra_files=files_in_dir())
