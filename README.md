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
- Move it to a folder (e.g., D:\Tools\bin)
- Add that folder to system PATH (explained below)

### ✅ Step 3: Install ffmpeg
- Go to: https://www.gyan.dev/ffmpeg/builds/
- Download: ffmpeg-release-essentials.zip
- Extract to: D:\Tools\ffmpeg\
- Move it to a folder (e.g, D:\Tools\bin)
- Add that folder to system PATH (explained below)

### ✅ Step 4: Add Tools to System PATH
- Press Win + S and search: Environment Variables
- Click Environment Variables...
- Under System variables, find and edit Path
- Click New and add:
  ```Makefile
  D:\Tools\bin\
- Click OK → OK → OK
- Restart your terminal

### ✅ Step 5: Verify Installation
  ```bash
  yt-dlp --version
  ffmpeg -version
  ```
- You should see version outputs for both.

### 🧰 How It Works (Download Flow)
- This is how the script functions internally:

- 🔢 Steps
- Input the YouTube URL
- Lists all available video and audio qualities
- User selects one of two options:
    - Option 1: Automatically download best quality using bestvideo+bestaudio
    - Option 2: Manually enter desired video and audio format IDs
- Downloads selected formats
- Uses ffmpeg to merge audio and video into a final .mp4

### 💻 Example Script Execution
  ```less
  Enter YouTube URL:
  > https://www.youtube.com/watch?v=example

  Select Download Option:
  1. Download Best Video + Audio
  2. Choose video/audio IDs manually

  > 2
  Enter Video ID: 137
  Enter Audio ID: 140

  [Downloading...]
  [Merging...]
  [Saved as output.mp4]
  ```

