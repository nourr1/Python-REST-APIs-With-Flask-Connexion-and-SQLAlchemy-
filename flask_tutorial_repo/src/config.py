import pathlib
import connexion
from flask_marshmallow import Marshmallow

# Determining the base directory
base_directory = pathlib.Path(__file__).parent.resolve()

# Establishing the connection 
connex_app = connexion.App(__name__, specification_dir=base_directory)
app = connex_app.app


ma = Marshmallow(app)
