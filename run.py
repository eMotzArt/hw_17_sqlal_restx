from app.app import create_app, configute_app
from app.config import Config

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configute_app(app)
    app.run(debug=True)
