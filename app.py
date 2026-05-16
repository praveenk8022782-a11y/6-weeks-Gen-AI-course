from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (acts like database)
posts = [
    {"id": 1, "title": "First Post"},
    {"id": 2, "title": "Second Post"}
]

# ---------------------------
# HOME ROUTE
# ---------------------------
@app.route("/")
def home():
    return "Flask REST API is running"

# ---------------------------
# GET ALL POSTS
# ---------------------------
@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

# ---------------------------
# GET SINGLE POST
# ---------------------------
@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# ---------------------------
# CREATE POST (POST)
# ---------------------------
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    new_post = {
        "id": len(posts) + 1,
        "title": data["title"]
    }
    posts.append(new_post)
    return jsonify(new_post), 201

# ---------------------------
# UPDATE POST (PUT)
# ---------------------------
@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.json
    for post in posts:
        if post["id"] == post_id:
            post["title"] = data.get("title", post["title"])
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# ---------------------------
# DELETE POST
# ---------------------------
@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return jsonify({"message": "Post deleted"})

# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)