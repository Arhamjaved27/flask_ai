from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Variable to store the latest message body
latest_message_body = None
new_message_flag = False  # Tracks if there is a new message

@app.route('/whatsapp', methods=['POST'])
def receive_message():
    """Endpoint to receive messages from Twilio."""
    global latest_message_body, new_message_flag
    try:
        data = request.form
        # Save only the message body as a string
        latest_message_body = data.get('Body')
        new_message_flag = True  # Set the flag to indicate a new message
        return "Message received", 200
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/api/messages', methods=['GET'])
def get_latest_message():
    """Endpoint to fetch the latest received message body."""
    global new_message_flag
    new_message_flag = False  # Reset the flag
    if latest_message_body:
        return jsonify({"body": latest_message_body})
    else:
        return jsonify({"message": "No messages yet"}), 200

@app.route('/api/has_new_messages', methods=['GET'])
def has_new_message():
    """Check if a new message has arrived."""
    return jsonify({"new_message": new_message_flag})

if __name__ == '__main__':
    app.run(debug=True, port=5000)








# from flask import Flask, request, jsonify
# from datetime import datetime

# app = Flask(__name__)

# # In-memory storage for messages
# message = None
# new_message_flag = False  # Tracks if there are new messages

# @app.route('/whatsapp', methods=['POST'])
# def receive_message():
#     """Endpoint to receive messages from Twilio."""
#     global new_message_flag
#     try:
#         data = request.form
#         message = {
#             'from': data.get('From'),
#             'body': data.get('Body'),
#             'timestamp': datetime.now().isoformat()
#         }
#         new_message_flag = True
#         return "Message received", 200
#     except Exception as e:
#         return f"Error: {e}", 500

# @app.route('/api/messages', methods=['GET'])
# def get_messages():
#     """Endpoint to fetch all received messages."""
#     global new_message_flag
#     new_message_flag = False  # Reset the flag
#     return jsonify(message)

# @app.route('/api/has_new_messages', methods=['GET'])
# def has_new_messages():
#     """Check if new messages have arrived."""
#     return jsonify({"new_messages": new_message_flag})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
