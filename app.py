from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def client():
    return send_from_directory("client", "index.html")

@app.route("/admin")
def admin():
    return send_from_directory("admin", "index.html")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
