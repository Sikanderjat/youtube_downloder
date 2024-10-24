from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("home.html")

@app.route("/downloded", methods=["POST"])
def downloded():
    url = request.form.get("url")
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=False).first()
        stream.download(output_path="C:/Users/sikan/Downloads/Sikander")
        return render_template("downloded.html", message="Video downloaded successfully!")
    except Exception as e:
        return render_template("downloded.html", message=f"Error: {str(e)}")
    


# app.run(debug=True, host="localhost", port=5500)