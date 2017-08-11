
import flask.ext.restful as flask_restful
import flask_template.api.resources.user as user_resource
from flask import Flask

# Create app.
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = flask_restful.Api(app, catch_all_404s=True)


# Ping Resources
api.add_resource(ping_resource.PingResource, "/ping")
api.add_resource(ping_resource.PongResource, "/pong")
api.add_resource(version_resource.VersionResource, "/version")

# User Resources
api.add_resource(user_resource.UserResource, '/user/<user_id>')

if __name__ == "__main__":
    app.run(debug=True)

