import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib  # Importing a custom video library module
import font_manager as fonts  # Importing a custom font manager module

# Function to set text in a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear the text area
    text_area.insert(1.0, content)  # Insert the new content

# Class to create a GUI for checking videos
class CheckVideos:
    def __init__(self, window):
        self.configure_window(window)  # Configure the window settings
        self.create_widgets(window)  # Create the widgets (buttons, labels, etc.)
        self.list_videos_clicked()  # Automatically list videos on startup

    # Configure the main window's geometry and title
    def configure_window(self, window):
        window.geometry("750x350")
        window.title("Check Videos")

    # Create and arrange all the widgets in the window
    def create_widgets(self, window):
        # Buttons
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Button to list all videos

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Button to check a specific video

        # Label for the entry field
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry field to input video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # ScrolledText area to display the list of videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to display details of a selected video
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Status label to display messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    # Function called when the "Check Video" button is clicked
    def check_video_clicked(self):
        key = self.input_txt.get()  # Get the video number from the entry field
        name = lib.get_name(key)  # Fetch the video name using the video library
        if name:
            # If the video is found, fetch additional details
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)  # Display the details in the text area
        else:
            # If the video is not found, display a message
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status label

    # Function called when the "List All Videos" button is clicked
    def list_videos_clicked(self):
        video_list = lib.list_all()  # Fetch the list of all videos
        set_text(self.list_txt, video_list)  # Display the list in the ScrolledText area
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label

# Main function to run the Tkinter application
if __name__ == "__main__":
    window = tk.Tk()  # Create the main window
    fonts.configure()  # Configure fonts using the custom font manager module
    CheckVideos(window)  # Instantiate the CheckVideos class with the main window
    window.mainloop()  # Run the Tkinter event loop
