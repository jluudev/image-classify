from flask import Flask
from predict import bp as predict_bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is not None:
        # load the test config if passed in
        app.config.update(test_config)

    app.register_blueprint(predict_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)
