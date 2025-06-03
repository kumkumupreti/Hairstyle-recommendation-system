from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route (optional)
@app.route('/')
def index():
    return "Hairstyle Recommendation API is running."

# Hairstyle database (mock data)
hairstyles_data ={
  "oval": {
    "short": [
      { "id": 1, "name": "Pixie Cut with Side-Swept Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748861496/592989a19ebfc385b426f27cd0474270_vnvvoq.webp" },
      { "id": 2, "name": "Classic Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748863922/678-6781758_hair-bob-png-transparent-png_jjtvlt.png" },
      { "id": 3, "name": "Layered Fringe", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748864176/Bangs-PNG-Isolated-Pic_p8209c.png" },
      { "id": 4, "name": "Blunt Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748864901/360_F_1124816167_Rx760OiW4SNlzwIKjkBDzfTE4db0U6r3_pvijwx.jpg" },
      { "id": 5, "name": "Asymmetrical Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748865010/trendy-hairs-brunette-black-colors-600nw-1953107008_brz6wr.webp" },
      { "id": 6, "name": "Textured Crop", "https://res.cloudinary.com/dppujds31/image/upload/v1748865201/textured-crop-undercut-stylish-men-hair-wig-fashionable-hairstyle-front-view-isolate-on-transparency-background-png_t9zn1x.webp": "" },
      { "id": 7, "name": "French Bob", "imageUrl": "http://res.cloudinary.com/dppujds31/image/upload/v1748866248/pngtree-illustration-of-short-bob-haircut-png-image_19497938_c2jgzl.png" },
      { "id": 8, "name": "Wavy Lob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748866399/images_acrwnt.jpg" },
      { "id": 9, "name": "Side-Parted Pixie", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748866545/images_1_dzrlc0.jpg" },
      { "id": 10, "name": "Stacked Bob", "imageUrl": "https://via.placeholder.com/150" }
    ],
    "medium": [
      { "id": 11, "name": "Shoulder-Length Waves", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867143/pngtree-elegant-waves-a-stunning-back-view-of-long-wavy-hair-png-image_15603459_dkxkee.png" },
      { "id": 12, "name": "Classic Lob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867367/istockphoto-1451376012-612x612_ptkhkv.jpg" },
      { "id": 13, "name": "Side Layered", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867457/images_2_zeqqj6.jpg" },
      { "id": 14, "name": "Curtain Bangs with Layers", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867517/images_3_eokvuj.jpg" },
      { "id": 15, "name": "Shag Cut", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867627/small-strands-till-chin-icon-260nw-1147823201_h8c63l.webp" },
      { "id": 16, "name": "Medium Curls", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748869800/curly-brown-hair-transparent-background-kr33m16320238bqn_eq2smq.png" },
      { "id": 17, "name": "Straight Lob with Middle Part", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 18, "name": "Wavy Shoulder-Length Cut", "imageUrl": "https://via.placeholder.com/150https://res.cloudinary.com/dppujds31/image/upload/v1748870149/b690b8aa77e42c8648b79553d72a5083_oyldem.jpg" },
      { "id": 19, "name": "Layered Mid-Length Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 20, "name": "Side-Swept Medium Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748870606/natural-looking-black-wig-on-260nw-2343806823_1_tifbyk.webp" }
    ],
    "long": [
      { "id": 21, "name": "Long Layers with Face-Framing Pieces", "imageUrl": "https://res.cloudinary.com/dgedczhkr/image/upload/v1748147983/1_dcvruf.jpg" },
      { "id": 22, "name": "V-Cut Long", "imageUrl": "https://i.imgur.com/0G65LHP.png" },
      { "id": 23, "name": "Curly Long", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871062/pngtree-curly-girl-hair-transparent-image-png-image_9125243_kr5egi.png" },
      { "id": 24, "name": "Straight Long with Side Part", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871206/images_4_c5qhsh.jpg" },
      { "id": 25, "name": "Beachy Waves", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871326/images_5_penxyc.jpg" },
      { "id": 26, "name": "Long Hair with Curtain Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871518/images_6_jqzfho.jpg" },
      { "id": 27, "name": "Layered Long Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871619/a31ba6b2307c8ced5d4c74f9dafa6597_bsnsi3.jpg" },
      { "id": 28, "name": "Sleek Straight Long Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871725/360_F_623263980_Sd9VzcE0gsqfmcv5PwGpeeLqRAJQfb6q_egwkcz.jpg" },
      { "id": 29, "name": "Long Hair with Side-Swept Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871837/3d-render-red-copper-medium-260nw-2582575589_antzae.webp" },
      { "id": 30, "name": "Voluminous Curls", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748873082/glamorous-dark-gray-hair-style-with-voluminous-curls-free-png_ak2zv8.png" }
    ]
  },
  "round": {
    "short": [
      { "id": 31, "name": "Side-Swept Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748940970/thick-shag-bob-5eead40867b54f898632fb215e290f8a_sfram5.jpg" },
      { "id": 32, "name": "Asymmetrical Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748865010/trendy-hairs-brunette-black-colors-600nw-1953107008_brz6wr.webp" },
      { "id": 33, "name": "Pixie Cut with Side Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748873470/1f0e067f-5451-4670-8ff6-be37303ca74c_mtudup.webp" },
      { "id": 34, "name": "Layered Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748873597/pngtree-chic-purple-bob-hairstyle-modern-layered-cut-for-a-bold-look-png-image_20323042_dkpxaq.png" },
      { "id": 35, "name": "Wavy Lob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748873760/images_7_wfmpq2.jpg" },
      { "id": 36, "name": "Choppy Pixie", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 37, "name": "Textured Crop", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874099/top-knot-stylish-men-hair-wig-fashionable-hairstyle-front-view-isolate-on-transparency-background-png_bphqf9.webp" },
      { "id": 38, "name": "Short Bob with Highlights", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874220/360_F_1455158126_Nlb3O4GJlFcuQUJ7hs26B7yyqmZ4fMUU_jq95on.png" },
      { "id": 39, "name": "Angular Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874322/2c2c1933f512d9804ad63b9c9bbc4ea4_xekzsd.jpg" },
      { "id": 40, "name": "Bixie Cut with Angled Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874548/images_2_q4h62i.jpg" }
    ],
    "medium": [
      { "id": 41, "name": "Shaggy Medium Length", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867627/small-strands-till-chin-icon-260nw-1147823201_h8c63l.webp" },
      { "id": 42, "name": "Deep Side Part", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874799/d03c0848ae518d499fe83d95397c28d1_vkyxgh.jpg" },
      { "id": 43, "name": "Face-Framing Layers", "imageUrl": "https://i.imgur.com/YIbVmHx.png" },
      { "id": 44, "name": "Medium Waves", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867143/pngtree-elegant-waves-a-stunning-back-view-of-long-wavy-hair-png-image_15603459_dkxkee.png" },
      { "id": 45, "name": "Medium Curls", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748875494/modern-stylish-men-curly-hair-wig-fashionable-hairstyle-isolate-on-transparency-background-png_aehkrl.webp" },
      { "id": 46, "name": "Classic Lob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867367/istockphoto-1451376012-612x612_ptkhkv.jpg" },
      { "id": 47, "name": "Side Layered", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867457/images_2_zeqqj6.jpg" },
      { "id": 48, "name": "Curtain Bangs with Medium Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867517/images_3_eokvuj.jpg" },
      { "id": 49, "name": "Layered Mid-Length Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 50, "name": "Side-Swept Medium Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748870606/natural-looking-black-wig-on-260nw-2343806823_1_tifbyk.webp" }
    ],
    "long": [
      { "id": 51, "name": "Long Layers", "imageUrl": "https://res.cloudinary.com/dgedczhkr/image/upload/v1748147983/1_dcvruf.jpg" },
      { "id": 52, "name": "V-Cut Long", "imageUrl": "https://i.imgur.com/0G65LHP.png" },
      { "id": 53, "name": "Curly Long", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871062/pngtree-curly-girl-hair-transparent-image-png-image_9125243_kr5egi.png" },
      { "id": 54, "name": "Straight Long", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 55, "name": "Beachy Waves", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871326/images_5_penxyc.jpg" },
      { "id": 56, "name": "Long Hair with Curtain Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871518/images_6_jqzfho.jpg" },
      { "id": 57, "name": "Layered Long Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871619/a31ba6b2307c8ced5d4c74f9dafa6597_bsnsi3.jpg" },
      { "id": 58, "name": "Sleek Straight Long Hair", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871725/360_F_623263980_Sd9VzcE0gsqfmcv5PwGpeeLqRAJQfb6q_egwkcz.jpg" },
      { "id": 59, "name": "Long Hair with Side-Swept Bangs", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871837/3d-render-red-copper-medium-260nw-2582575589_antzae.webp" },
      { "id": 60, "name": "Voluminous Curls", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748873082/glamorous-dark-gray-hair-style-with-voluminous-curls-free-png_ak2zv8.png" }
    ]
  },
  "long": {
    "short": [
      { "id": 61, "name": "Choppy Pixie with Long Bangs", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 62, "name": "Lip-Length Bob with Bangs", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 63, "name": "Blunt Middle-Parted Bob", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 64, "name": "Tousled Pixie Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 65, "name": "Side-Swept Crop Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 66, "name": "Layered Bob", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 67, "name": "Short Bob with Volume", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 68, "name": "Asymmetrical Bob", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748865010/trendy-hairs-brunette-black-colors-600nw-1953107008_brz6wr.webp" },
      { "id": 69, "name": "Textured Crop", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748874099/top-knot-stylish-men-hair-wig-fashionable-hairstyle-front-view-isolate-on-transparency-background-png_bphqf9.webp" },
      { "id": 70, "name": "Short Bob with Side Bangs", "imageUrl": "https://via.placeholder.com/150" }
    ],
    "medium": [
      { "id": 71, "name": "Shaggy Shoulder Cut", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748867143/pngtree-elegant-waves-a-stunning-back-view-of-long-wavy-hair-png-image_15603459_dkxkee.png" },
      { "id": 72, "name": "Birkin Bangs", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 73, "name": "Layered Shoulder Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 74, "name": "Medium Waves", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 75, "name": "Medium Curls", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 76, "name": "Classic Lob", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 77, "name": "Side Layered", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 78, "name": "Curtain Bangs with Medium Hair", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 79, "name": "Layered Mid-Length Cut", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 80, "name": "Side-Swept Medium Hair", "imageUrl": "https://via.placeholder.com/150" }
    ],
    "long": [
      { "id": 81, "name": "Long Layers with Face-Framing Pieces", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 82, "name": "V-Cut Long", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 83, "name": "Curly Long", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 84, "name": "Straight Long with Side Part", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 85, "name": "Beachy Waves", "imageUrl": "https://res.cloudinary.com/dppujds31/image/upload/v1748871326/images_5_penxyc.jpg" },
      { "id": 86, "name": "Long Hair with Curtain Bangs", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 87, "name": "Layered Long Hair", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 88, "name": "Sleek Straight Long Hair", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 89, "name": "Long Hair with Side-Swept Bangs", "imageUrl": "https://via.placeholder.com/150" },
      { "id": 90, "name": "Voluminous Curls", "imageUrl": "https://via.placeholder.com/150" }
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