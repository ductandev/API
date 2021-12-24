from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request

# ########### INIT FLASK

app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*')
def home():
    return "Đây là home"

@app.route('/submit', methods=['POST'])
@cross_origin(origin='*')
def submit():
    # {
    #     "name" : "Sách AI",
    #     "price" : 100000,
    #     "ready" : 0
    # }
    
    request_json =request.json
    name = request_json["name"]
    price = request_json["price"]
    ready = request_json["ready"]
    
    if name is None:
        return "Thiếu name"
    if price is None:
        return "Thiếu price"
    
    # Insert vào cơ sở dữ liệu
    return "Save thành công ---- Đây là submid"

# Bật Backend ở cổng 6868
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')
