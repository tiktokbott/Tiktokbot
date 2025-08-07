# Menulis ulang file app.py karena environment telah di-reset

code = """
from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>TikTok Comment Like Bot</title>
    <style>
        body { font-family: Arial; background: #111; color: #fff; padding: 30px; text-align: center; }
        input, button { padding: 10px; margin: 10px; width: 300px; }
        button { background: #00f7ff; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h2>🤖 TikTok Comment Like Bot</h2>
    <form method="post">
        <input type="text" name="video_url" placeholder="Masukkan Link Video TikTok" required><br>
        <input type="text" name="comment_username" placeholder="Username Komentar Kamu" required><br>
        <button type="submit">Mulai Like Komentar</button>
    </form>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        comment_username = request.form.get("comment_username")

        # Jalankan bot.py dengan parameter
        subprocess.Popen(["python3", "bot.py", video_url, comment_username])

        return f"<h3 style='color:lime'>Bot sedang berjalan untuk: {comment_username}</h3><a href='/'>Kembali</a>"

    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
"""

with open("/mnt/data/app.py", "w") as f:
    f.write(code)

"/mnt/data/app.py berhasil dibuat ✅"
