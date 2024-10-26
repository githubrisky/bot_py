# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Definisikan logika respon sederhana
def chatbot_response(message):
    if "hai" in message.lower():
        return "Halo! Ada yang bisa saya bantu?"
    elif "siapa namamu" in message.lower():
        return "Nama saya Chatbot Sederhana."
    elif "apa yang bisa kamu lakukan" in message.lower():
        return "Saya bisa menjawab beberapa pertanyaan dasar!"
    else:
        return "Maaf, saya tidak mengerti. Coba tanyakan sesuatu yang lain."

# Endpoint untuk menerima pesan dan mengirimkan respon
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
