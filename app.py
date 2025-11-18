import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp bot running!"

# Aquí añadiremos tu lógica del bot más adelante

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
