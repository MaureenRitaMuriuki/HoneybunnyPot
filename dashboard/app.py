with open('../logs/attack_log.txt', 'r') as f:
    logs = f.readlines()
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    with open('../logs/attack_log.txt', 'r') as f:
        logs = f.readlines()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
      app.run(debug=True, port=5001)
