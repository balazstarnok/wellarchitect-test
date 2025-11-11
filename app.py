"""
Main Flask application with vulnerable dependencies.
This is a test application for security scanning.
"""
import requests
import flask
from urllib3 import PoolManager
import yaml
from jinja2 import Template

app = flask.Flask(__name__)


def fetch_data(url):
    """Fetch data from URL using vulnerable requests library"""
    response = requests.get(url)
    return response.json()


@app.route('/')
def home():
    """Home page that fetches external data"""
    try:
        data = fetch_data('https://api.github.com/repos/balazstarnok/wellarchitect-test')
        return flask.jsonify(data)
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


@app.route('/render')
def render_template():
    """Render user template (vulnerable to SSTI via Jinja2)"""
    template_str = flask.request.args.get('template', 'Hello World')
    template = Template(template_str)
    return template.render()


@app.route('/config')
def load_config():
    """Load YAML config (vulnerable to arbitrary code execution)"""
    config_data = """
    app_name: test-app
    version: 1.0.0
    debug: true
    """
    config = yaml.load(config_data, Loader=yaml.FullLoader)
    return flask.jsonify(config)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

