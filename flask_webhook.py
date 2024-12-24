from flask import Flask, request
# from apps import process_chatbot_message  # Import function from main.py

app = Flask(__name__)

# @app.route('/')
# def whatsapp_webhook():
#     return 'Hello World'


@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_message = request.form.get('Body')
    sender = request.form.get('From')

    # response = process_chatbot_message(incoming_message)  # Call your chatbot logic
    # return f"<Response><Message>{response}</Message></Response>"
    return f"<Response><Message>{incoming_message}</Message></Response>"

if __name__ == '__main__':
    app.run(port=5000)
