from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/health")
def health():
    # Used later by ECS / load balancers to check the container is alive
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # Local dev only. In the container we'll use gunicorn instead.
    app.run(host="0.0.0.0", port=3000, debug=True)
