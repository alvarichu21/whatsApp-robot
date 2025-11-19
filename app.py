import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

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
        print("ERROR GPT:", e)
        reply = "Lo siento, hubo un error procesando tu mensaje."

    resp.message(reply)
    return str(resp), 200

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp GPT bot funcionando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)