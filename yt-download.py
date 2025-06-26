import subprocess
import sys

def list_formats(url):
    print("\n📄 Fetching available formats...\n")
    subprocess.run(["yt", "-F", url])

def download_best(url):
    print("\n⬇️ Downloading best video and audio...")
    subprocess.run(["yt", "-f", "bestvideo+bestaudio", url])

def download_custom(url, video_id, audio_id):
    print(f"\n⬇️ Downloading video ({video_id}) and audio ({audio_id}) separately...")
    subprocess.run(["yt", "-f", f"{video_id}+{audio_id}", url])

def main():
    print("🎯 YouTube Download Manager using yt-dlp + ffmpeg\n")
    url = input("🔗 Enter the video URL: ").strip()

    list_formats(url)

    print("\nChoose download option:")
    print("1. Download best available quality")
    print("2. Choose custom video and audio formats")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        download_best(url)
    elif choice == "2":
        video_id = input("Enter video format ID: ").strip()
        audio_id = input("Enter audio format ID: ").strip()
        download_custom(url, video_id, audio_id)
    else:
        print("❌ Invalid choice. Exiting.")
        sys.exit(1)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
