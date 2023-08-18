from flask import Flask, request
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Apply CORS to your app

@app.route('/hello', methods=['GET'])
def hello():
    language = request.args.get('language', 'English')
    if language == 'French':
        return 'Bonjour le monde'
    elif language == 'Hindi':
        return 'Namastey sansar'
    else:
        return 'Hello world'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

