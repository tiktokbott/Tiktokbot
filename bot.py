
import sys
import time

def like_comment(video_url, comment_username):
    print(f"🔗 Video: {video_url}")
    print(f"❤️ Mencari komentar dari: {comment_username}")
    print("🔄 Menjalankan proses auto-like...")

    # Simulasi proses bot
    time.sleep(3)
    print("✅ Komentar ditemukan dan sudah di-LIKE!")
    print("🔁 Selesai")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bot.py <video_url> <comment_username>")
        sys.exit(1)

    video_url = sys.argv[1]
    comment_username = sys.argv[2]
    like_comment(video_url, comment_username)
