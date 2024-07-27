import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
import os

# Define the path to the lyrics file
folder_path = 'twinkle_twinkle_little_star'
file_name = 'lyrics.txt'
file_path = os.path.join(folder_path, file_name)

def read_file(file_path):
    """Reads the content of the file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def display_lyrics():
    """Creates a window to display the lyrics."""
    # Create the main window
    window = tk.Tk()
    window.title("Lyrics Display")

    # Create a scrolled text widget with a custom font
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
    
    # Set font size and type
    custom_font = font.Font(family="Helvetica", size=16)  # You can change the size here
    text_area.configure(font=custom_font)
    
    text_area.pack(expand=True, fill=tk.BOTH)

    # Load and insert the lyrics into the text widget
    lyrics = read_file(file_path)
    text_area.insert(tk.END, lyrics)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    display_lyrics()
