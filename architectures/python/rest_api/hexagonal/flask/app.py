import os

from application.v1 import blueprint
from application import create_app
from application.utilities.helpers import JsonEncoder

app = create_app(os.getenv("ENV") or "dev")
app.json_encoder = JsonEncoder
app.register_blueprint(blueprint, url_prefix="/v1")

app.app_context().push()


def run():
    app.run(port=8089)


if __name__ == "__main__":
    run()
