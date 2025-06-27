import subprocess
import sys
import os

# Set your desired download folder
DOWNLOAD_PATH = "C:/Users/uyaam/Downloads/"

def list_formats(url):
    print("\n📄 Fetching available formats...\n")
    subprocess.run(["yt-dlp", "-F", url])

def download_by_format(url, format_string, is_mp3=False):
    cmd = ["yt-dlp", "-f", format_string, "-P", DOWNLOAD_PATH]
    if is_mp3:
        cmd += ["--extract-audio", "--audio-format", "mp3"]
    cmd.append(url)

    print(f"\n⬇️ Downloading with format: {format_string}")
    subprocess.run(cmd)

def download_custom(url, video_id, audio_id):
    format_string = f"{video_id}+{audio_id}"
    download_by_format(url, format_string)

def main():
    print("🎯 YouTube Download Manager using yt-dlp + ffmpeg\n")
    url = input("🔗 Enter the video URL: ").strip()

    # Ensure the download directory exists
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    list_formats(url)

    print("\nChoose download option:")
    print("1. Best Quality")
    print("2. Medium Quality (<=720p)")
    print("3. Low Quality (<=480p)")
    print("4. MP3 Audio Only")
    print("5. Custom video/audio format IDs")
    choice = input("Enter choice [1-5]: ").strip()

    if choice == "1":
        download_by_format(url, "bestvideo+bestaudio")
    elif choice == "2":
        download_by_format(url, "bv[height<=720]+ba")
    elif choice == "3":
        download_by_format(url, "bv[height<=480]+ba")
    elif choice == "4":
        download_by_format(url, "bestaudio", is_mp3=True)
    elif choice == "5":
        video_id = input("Enter video format ID: ").strip()
        audio_id = input("Enter audio format ID: ").strip()
        download_custom(url, video_id, audio_id)
    else:
        print("❌ Invalid choice. Exiting.")
        sys.exit(1)

    print(f"\n✅ Done! Files saved to: {DOWNLOAD_PATH}")

if __name__ == "__main__":
    main()





"""import subprocess
import sys

def list_formats(url):
    print("\n📄 Fetching available formats...\n")
    subprocess.run(["yt-dlp", "-F", url])

def download_best(url):
    print("\n⬇️ Downloading best video and audio...")
    subprocess.run(["yt-dlp", "-f", "bestvideo+bestaudio", url])

def download_custom(url, video_id, audio_id):
    print(f"\n⬇️ Downloading video ({video_id}) and audio ({audio_id}) separately...")
    subprocess.run(["yt-dlp", "-f", f"{video_id}+{audio_id}", url])

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
"""