# 🎬 YouTube Downloader

A simple Python-based command-line download manager using `yt-dlp` and `ffmpeg`. Select and download YouTube videos or audio in your preferred quality with optional merging of audio and video streams.

---

## ✨ Features
- Lists all available video and audio formats from a given YouTube URL
- Option to automatically download the best available quality
- Option to manually choose video and audio format IDs
- Merges audio and video using `ffmpeg`
- Easy-to-follow command-line prompts
- Can be used as a base for GUI-based download managers

---

## 📦 Requirements

- **Python 3.10+**
- **yt-dlp** (CLI tool for downloading YouTube videos)
- **ffmpeg** (for merging video and audio streams)
- All tools must be accessible via your system **PATH**

---

## ⚙️ Setup Instructions (Windows)

### ✅ Step 1: Install Python 3.10+

- Download from: https://www.python.org/downloads/
- During installation, **check the box**: “Add Python to PATH”
- Verify:
  ```bash
  python --version

### ✅ Step 2: Install yt-dlp
- 📌 Option A: Install via pip (Recommended)
  ```bash
  pip install -U yt-dlp
- 📌 Option B: Download yt-dlp.exe
- Go to: https://github.com/yt-dlp/yt-dlp/releases/latest
- Download: yt-dlp.exe
- Move it to a folder (e.g., D:\Tools\yt-dlp\)
- Add that folder to system PATH (explained below)