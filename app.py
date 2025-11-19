import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
print("DEBUG: OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()

try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": incoming_msg}],
        max_tokens=300
    )
    reply = completion.choices[0].message["content"].strip()
except Exception as e:
    # 🔹 Aquí capturamos el error real y lo mostramos en logs y WhatsApp
    print("ERROR GPT DETALLADO:", e)
    reply = f"Lo siento, hubo un error procesando tu mensaje: {e}"
    resp.message(reply)
    return str(resp), 200

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp GPT bot funcionando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
