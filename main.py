from flask import Flask, render_template, request, jsonify
import datetime
import webbrowser

app = Flask(__name__)

def process_command(comm):
    comm = comm.lower()
    if "open youtube" in comm:
        webbrowser.open("https://www.youtube.com")
        return "Opened YouTube"
    elif "hello jarvis" in comm:
        return "Hello! How can I assist you today?"
    elif "open google" in comm:
        webbrowser.open("https://www.google.com")
        return "Opened Google"
    elif "open linkedin" in comm:
        webbrowser.open("https://www.linkedin.com")
        return "Opened LinkedIn"
    elif "open instagram" in comm:
        webbrowser.open("https://www.instagram.com")
        return "Opened Instagram"
    elif "open facebook" in comm:
        webbrowser.open("https://www.facebook.com")
        return "Opened Facebook"
    elif "time" in comm:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"
    elif "shutdown" in comm or "exit" in comm:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    user_command = data.get("command", "")
    result = process_command(user_command)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
