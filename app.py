import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    
    # Crear respuesta automática
    resp = MessagingResponse()
    
    if incoming_msg == "hola":
        resp.message("¡Hola! Soy tu bot funcionando 😊")
    else:
        resp.message("Recibí tu mensaje: " + incoming_msg)
    
    return str(resp), 200

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp bot running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
