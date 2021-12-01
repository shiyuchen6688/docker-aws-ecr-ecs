from flask import Flask
import random
app = Flask(__name__)
foodList = ["pizza", "icecream", "chocolate", "chicken breast"]

@app.route("/")
def index():
    return "You should eat" + random.choice(foodList)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))