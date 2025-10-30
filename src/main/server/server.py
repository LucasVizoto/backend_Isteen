from flask import Flask, request, make_response
from flask_cors import CORS

from src.models.sqlite.settings.connection import db_connection_handler

#------------------ DATABASE CONNECTION -----------------------
db_connection_handler.connect_to_db()

#------------------ FRAMEWORK CONNECTION -----------------------
app = Flask(__name__)


#------------------ CORS CONFIGURATION -----------------------
CORS(
    app,
    resources={"/*": {"origins": "*"}},
    supports_credentials=False,      # deixe False se não usa cookies/sessão
    allow_headers="*",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
)

@app.before_request
def handle_options_request():
    # Intercepta qualquer OPTIONS antes de bater nas rotas
    if request.method == "OPTIONS":
        response = make_response("", 204)
        # Headers básicos de CORS
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,PATCH,DELETE,OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = request.headers.get(
            "Access-Control-Request-Headers", "*"
        )
        return response

#------------------ REGISTER BLUEPRINTS -----------------------


