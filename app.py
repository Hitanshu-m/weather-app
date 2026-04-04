from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1b9f1c5af76ff27c5827ebaff3be50c2"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if str(data["cod"]) == "200":
            weather = {
                "city": data["name"],
                "temp": round(data["main"]["temp"]),
                "feels": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "wind": data["wind"]["speed"]
            }
        else:
            weather = {"error": data.get("message")}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)