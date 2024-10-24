from flask import Flask, render_template, request
# from pytube import YouTube
import yt_dlp

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("home.html")

@app.route("/downloded", methods=["POST"])
def downloded():
    url = request.form.get("url")
    # url = "https://www.youtube.com/watch?v=J---aiyznGQ"
    try:
        yt={
            'formate':'best',
            'outtmpl':'C:/Users/sikan/Videos/sikander/%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(yt) as ydl:
            ydl.download([url])
        return render_template("downloded.html", message="Video downloaded successfully!")
    except Exception as e:
        return render_template("downloded.html", message=f"Error: {str(e)}")
    


#app.run(debug=True, host="localhost", port=5500)
