import tkinter as tk
from tkinter import scrolledtext
import video_library as lib
import random

class CreateVideoList:
    def __init__(self, main_window):
        self.video_list = []
        self.main_window = main_window

        self.setup_ui()

    def setup_ui(self):
        self.main_window.geometry("550x450")
        self.main_window.title("Create Video List")

        # Create input frame
        input_frame = tk.Frame(self.main_window)
        input_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        tk.Label(input_frame, text="Enter Video Number").pack(side=tk.LEFT)
        self.entry_input = tk.Entry(input_frame, width=5)
        self.entry_input.pack(side=tk.LEFT)
        tk.Button(input_frame, text="Add Video to List", command=self.add_video_to_list).pack(side=tk.LEFT)
        tk.Button(input_frame, text="Play Video", command=self.play_video_list).pack(side=tk.LEFT)

        # Create button frame
        button_frame = tk.Frame(self.main_window)
        button_frame.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

        tk.Button(button_frame, text="Reset List", command=self.clear_video_list).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Randomize Video", command=self.add_random_video_to_list).pack(side=tk.LEFT)

        # Create video list display
        self.video_list_display = scrolledtext.ScrolledText(self.main_window, width=62, height=10, wrap="none")
        self.video_list_display.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        # Create status label
        self.status_label = tk.Label(self.main_window, text="", font=("Helvetica", 8))
        self.status_label.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    def add_video_to_list(self):
        video_identifier = self.entry_input.get()
        video_name = lib.get_name(video_identifier)
        if video_name:
            self.video_list.append(video_identifier)
            self.refresh_video_list_display()
            self.status_label.config(text=f"Video {video_identifier} has been added to the list!")
        else:
            self.status_label.config(text=f"Video {video_identifier} is not found!")

    def refresh_video_list_display(self):
        video_names = [lib.get_name(video_identifier) for video_identifier in self.video_list]
        self.video_list_display.delete("1.0", tk.END)
        self.video_list_display.insert("1.0", "\n".join(video_names))

    def play_video_list(self):
        if self.video_list:
            for video_identifier in self.video_list:
                lib.increment_play_count(video_identifier)
            self.status_label.config(text="Video is played! Play count has been increased.")
        else:
            self.status_label.config(text="No videos in the list to play!")

    def clear_video_list(self):
        self.video_list = []
        self.video_list_display.delete("1.0", tk.END)
        self.status_label.config(text="Video List is cleared!")

    def add_random_video_to_list(self):
        all_videos = lib.get_all_video_ids()
        if all_videos:
            random_video = random.choice(all_videos)
            self.video_list.append(random_video)
            self.refresh_video_list_display()
            self.status_label.config(text=f"Random Video {random_video} has been added to the list!")
        else:
            self.status_label.config(text="No videos available to choose from!")


if __name__ == "__main__":
    main_app = tk.Tk()
    video_list_app = CreateVideoList(main_app)
    main_app.mainloop()