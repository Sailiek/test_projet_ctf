from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# On récupère les valeurs du .env (injectées par Docker)
USER_REQUIRED = os.getenv('CHALLENGE_USER')
PASS_REQUIRED = os.getenv('CHALLENGE_PASSWORD')
FLAG = os.getenv('CHALLENGE_FLAG')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == USER_REQUIRED and password == PASS_REQUIRED:
        return jsonify({"success": True, "message": f"Correct ! Voici le flag : {FLAG}"})
    else:
        return jsonify({"success": False, "message": "Identifiants incorrects."}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)