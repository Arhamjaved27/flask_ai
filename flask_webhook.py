from flask import Flask, request
app = Flask(__name__)

# @app.route('/')
# def whatsapp_webhook():
#     return 'Hello World'


# In-memory storage for messages
messages = []

@app.route('/whatsapp', methods=['POST'])
def receive_message():
    """Endpoint to receive messages from Twilio."""
    try:
        data = request.form  # Twilio sends message data as form-encoded
        message = {
            'from': data.get('From'),
            'body': data.get('Body'),
            'timestamp': datetime.now().isoformat()
        }
        messages.append(message)
        return "Message received", 200
    except Exception as e:
        return f"Error: {e}", 500


@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Endpoint to fetch all received messages."""
    return jsonify(messages)


if __name__ == '__main__':
    app.run(port=5000)
