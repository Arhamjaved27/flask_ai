from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for messages
messages =  None
new_message_flag = False  # Tracks if there are new messages

@app.route('/whatsapp', methods=['POST'])
def receive_message():
    """Endpoint to receive messages from Twilio."""
    global new_message_flag
    try:
        data = request.form
        message = {
            'from': data.get('From'),
            'body': data.get('Body'),
            'timestamp': datetime.now().isoformat()
        }
        messages = message
        new_message_flag = True
        return "Message received", 200
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Endpoint to fetch all received messages."""
    global new_message_flag
    new_message_flag = False  # Reset the flag
    return jsonify(messages)

@app.route('/api/has_new_messages', methods=['GET'])
def has_new_messages():
    """Check if new messages have arrived."""
    return jsonify({"new_messages": new_message_flag})

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# from flask import Flask, request, jsonify
# from datetime import datetime

# app = Flask(__name__)

# # @app.route('/')
# # def whatsapp_webhook():
# #     return 'Hello World'


# # In-memory storage for messages
# messages = []

# @app.route('/whatsapp', methods=['POST'])
# def receive_message():
#     """Endpoint to receive messages from Twilio."""
#     try:
#         data = request.form  # Twilio sends message data as form-encoded
#         message = {
#             'from': data.get('From'),
#             'body': data.get('Body'),
#             'timestamp': datetime.now().isoformat()
#         }
#         messages.append(message)
#         return "Message received", 200
#     except Exception as e:
#         return f"Error: {e}", 500


# @app.route('/api/messages', methods=['GET'])
# def get_messages():
#     """Endpoint to fetch all received messages."""
#     return jsonify(messages)


# if __name__ == '__main__':
#     app.run(port=5000)
