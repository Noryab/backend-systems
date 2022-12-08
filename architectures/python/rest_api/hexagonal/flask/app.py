import os

from application.v1 import blueprint as bp1
from application import create_app
from application.utilities.helpers import JsonEncoder

app = create_app(os.getenv("ENV") or "development")
app.json_encoder = JsonEncoder

app.register_blueprint(bp1, url_prefix="/v1")
app.app_context().push()


def run():
    app.run(port=8089)


if __name__ == "__main__":
    run()
