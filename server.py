from flask import Flask, render_template ,request


app = Flask(__name__)

@app.route('/')
def blog():
    return render_template("index.html")

@app.route('/send_message', methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    return f"<h1> {name,email,phone,message}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
