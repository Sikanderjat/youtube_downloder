from flask import Flask, render_template, request,send_file
import os
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
        # Download to a temporary path
        output_path = "downloads"  # create a folder named 'downloads' in your project directory
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        file_path = stream.download(output_path=output_path)
        return send_file(file_path, as_attachment=True)  # Send the file for download
    except Exception as e:
        return render_template("downloded.html", message=f"Error: {str(e)}")




# app.run(debug=True, host="localhost", port=5500)
