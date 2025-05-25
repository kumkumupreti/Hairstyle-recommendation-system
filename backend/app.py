from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route (optional)
@app.route('/')
def index():
    return "Hairstyle Recommendation API is running."

# Hairstyle database (mock data)
hairstyles_data = {
    "oval": {
        "short": [
            { "id": 1, "name": "Pixie Cut", "imageUrl": "https://i.imgur.com/QzRG2f4.png" },
            { "id": 2, "name": "Short Bob", "imageUrl": "https://i.imgur.com/I8n4jxw.png" },
            { "id": 3, "name": "Layered Fringe", "imageUrl": "https://i.imgur.com/8e4UzGa.png" }
        ],
        "medium": [
            { "id": 4, "name": "Medium Waves", "imageUrl": "https://i.imgur.com/YFgCkYJ.png" },
            { "id": 5, "name": "Medium Curls", "imageUrl": "https://i.imgur.com/U2BckMv.png" },
            { "id": 6, "name": "Classic Lob", "imageUrl": "https://i.imgur.com/YIbVmHx.png" },
            { "id": 7, "name": "Side Layered", "imageUrl": "https://i.imgur.com/L3XYFBE.png" }
        ],
        "long": [
            { "id": 8, "name": "Long Layers with Face-Framing Pieces", "imageUrl": "https://res.cloudinary.com/dgedczhkr/image/upload/v1748147983/1_dcvruf.jpg" },
            { "id": 9, "name": "V-Cut Long", "imageUrl": "https://i.imgur.com/0G65LHP.png" },
            { "id": 10, "name": "Curly Long", "imageUrl": "https://i.imgur.com/XZghS2N.png" }
        ]
    },
    "round": {
        "short": [
            { "id": 11, "name": "Pixie Cut", "imageUrl": "https://i.imgur.com/QzRG2f4.png" },
            { "id": 12, "name": "Short Bob", "imageUrl": "https://i.imgur.com/I8n4jxw.png" },
            { "id": 13, "name": "Layered Fringe", "imageUrl": "https://i.imgur.com/8e4UzGa.png" }
        ],
        "medium": [
            { "id": 14, "name": "Medium Waves", "imageUrl": "https://i.imgur.com/YFgCkYJ.png" },
            { "id": 15, "name": "Medium Curls", "imageUrl": "https://i.imgur.com/U2BckMv.png" },
            { "id": 16, "name": "Classic Lob", "imageUrl": "https://i.imgur.com/YIbVmHx.png" },
            { "id": 17, "name": "Side Layered", "imageUrl": "https://i.imgur.com/L3XYFBE.png" }
        ],
        "long": [
            { "id": 18, "name": "Straight Long", "imageUrl": "https://i.imgur.com/kW0KDLl.png" },
            { "id": 19, "name": "V-Cut Long", "imageUrl": "https://i.imgur.com/0G65LHP.png" },
            { "id": 20, "name": "Curly Long", "imageUrl": "https://i.imgur.com/XZghS2N.png" }
        ]
    },
    "long": {
        "short": [
            { "id": 21, "name": "Pixie Cut", "imageUrl": "https://i.imgur.com/QzRG2f4.png" },
            { "id": 22, "name": "Short Bob", "imageUrl": "https://i.imgur.com/I8n4jxw.png" },
            { "id": 23, "name": "Layered Fringe", "imageUrl": "https://i.imgur.com/8e4UzGa.png" }
        ],
        "medium": [
            { "id": 24, "name": "Medium Waves", "imageUrl": "https://res.cloudinary.com/dgedczhkr/image/upload/v1748147983/1_dcvruf.jpg" },
            { "id": 25, "name": "Medium Curls", "imageUrl": "https://i.imgur.com/U2BckMv.png" },
            { "id": 26, "name": "Classic Lob", "imageUrl": "https://i.imgur.com/YIbVmHx.png" },
            { "id": 27, "name": "Side Layered", "imageUrl": "https://i.imgur.com/L3XYFBE.png" }
        ],
        "long": [
            { "id": 28, "name": "Straight Long", "imageUrl": "https://i.imgur.com/kW0KDLl.png" },
            { "id": 29, "name": "V-Cut Long", "imageUrl": "https://i.imgur.com/0G65LHP.png" },
            { "id": 30, "name": "Curly Long", "imageUrl": "https://i.imgur.com/XZghS2N.png" }
        ]
    }
}
# ✅ Main API endpoint for fetching hairstyles
@app.route('/api/hairstyles')
def get_hairstyles():
    face_shape = request.args.get('faceShape', '').lower()
    length = request.args.get('length', '').lower()

    if not face_shape or not length:
        return jsonify({"error": "Missing faceShape or length parameter"}), 400

    styles = hairstyles_data.get(face_shape, {}).get(length, [])
    return jsonify({"hairstyles": styles})

if __name__ == '__main__':
    app.run(debug=True, port=5000)