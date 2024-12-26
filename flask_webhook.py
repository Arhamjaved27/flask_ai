from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Variable to store the latest message (only the last one is stored)
latest_message = None
new_message_flag = False  # Flag to indicate if there's a new message

@app.route('/whatsapp', methods=['POST'])
def receive_message():
    """Endpoint to receive messages from Twilio."""
    global latest_message, new_message_flag
    try:
        data = request.form
        # Store only the latest message
        latest_message = {
            'from': data.get('From'),
            'body': data.get('Body'),
            'timestamp': datetime.now().isoformat()
        }
        new_message_flag = True  # Indicate that a new message has been received
        return "Message received", 200
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Endpoint to fetch the latest received message."""
    global new_message_flag
    new_message_flag = False  # Reset the new message flag
    if latest_message:
        return jsonify(latest_message)
    else:
        return jsonify({"message": "No messages yet"}), 200

@app.route('/api/has_new_messages', methods=['GET'])
def has_new_messages():
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
