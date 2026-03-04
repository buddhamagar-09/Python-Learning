# from pytube import YouTube
import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded Successfully !!")
    except Exception as e:
        print("Error:", e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder

def clean_url(url):
    if "&" in url:
        url = url.split("&")[0]
    return url.strip()


def main():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring dialog to front
    
    video_url = input("Enter the video Url:")
    video_url = clean_url(video_url)
    print("Opening folder selection dialog...")
    save_dir = open_file_dialog()

    if save_dir:
        print("Download Started.....")
        download_video(video_url, save_dir)
        print("Download completed!")
    else:
        print("Invalid Save Location.")


if __name__ == '__main__': 
    main()

