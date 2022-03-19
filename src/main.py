from flask import Flask, request, jsonify
from plugins.core.plugin_manager import PluginManager


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
PluginManager(app).add_moudles()

# @app.route('/coords/<name>', methods=['GET'])
# def get_coords_from_map(name):
#     return pars_coords(name)


if __name__ == '__main__':
    app.run(debug=True)
