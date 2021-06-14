from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request
import requests


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per day"]
)
@app.route("/api",methods=['GET'])
@limiter.limit("5 per day")
def api():
    address = request.args['address']
    response = requests.get(f"http://lunacia.skymavis.com/game-api/clients/{address}/items/1",headers=headers)
    response=response.text
    try:
        return f"{response}"
    except KeyError:
        return "Invalid input"

