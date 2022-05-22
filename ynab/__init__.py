import os

from flask import Flask


def create_app(test_config=None):
    # create and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "ynab.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/heartbeat")
    def hello():
        return {"status": "OK"}, 200

    from . import db

    db.init_app(app)

    from . import application

    app.register_blueprint(application.bp)
    app.add_url_rule("/", endpoint="index")

    return app
