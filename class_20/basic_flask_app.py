from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is my machine"


@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

@app.route("/name/<student>")
def student_name(student):
        
    return f"Hello, {student}"

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)