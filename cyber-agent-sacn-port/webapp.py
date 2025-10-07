from flask import Flask, render_template, jsonify
import tailer

LOG_FILE = "portscan.log"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/logs")
def get_logs():
    try:
        # Lit les 50 dernières lignes du fichier de log
        lines = tailer.tail(open(LOG_FILE), 50)
        return jsonify(lines)
    except Exception as e:
        return jsonify([f"Erreur : {e}"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
