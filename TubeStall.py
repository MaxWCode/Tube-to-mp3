import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def youtube_to_mp3(video_url, output_directory, output_filename):
    command = ["yt-dlp", "-f", "bestaudio", "-x", "--audio-format", "mp3", video_url, "-o", output_directory + "/" + output_filename]
    subprocess.run(command, check=True)
    return output_directory + "/" + output_filename

def download_mp3():
    video_url = url_entry.get()
    output_directory = "/Users/maxwardle/Downloads"
    output_filename = filename_entry.get()

    try:
        mp3_file_path = youtube_to_mp3(video_url, output_directory, output_filename)
        messagebox.showinfo("Success", f"The MP3 file has been downloaded to:\n{mp3_file_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", "An error occurred while downloading the video. Please check the URL and try again.")

# Create the main application window
app = tk.Tk()
app.title("YouTube to MP3 Converter")

# Set the window size
window_width = 400
window_height = 300

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window size and position
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and configure the URL entry field
url_label = ttk.Label(app, text="Enter the YouTube video URL:")
url_label.pack(pady=10)
url_entry = ttk.Entry(app, width=40)
url_entry.pack(pady=10)

# Create and configure the filename entry fielda
filename_label = ttk.Label(app, text="Enter the filename for the MP3 file:")
filename_label.pack(pady=10)
filename_entry = ttk.Entry(app, width=40)
filename_entry.pack(pady=10)

# Create and configure the download button
download_button = ttk.Button(app, text="Download MP3", command=download_mp3)
download_button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
