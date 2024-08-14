import tkinter as tk
 
import font_manager as fonts
from check_video import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos
 
def check_video():
    CheckVideos(tk.Toplevel(main_window))
    status_label.config(text="Check Video button was clicked successfully!")
 
def create_video_list():
    CreateVideoList(tk.Toplevel(main_window))
    status_label.config(text="Create Video List button was clicked successfully!")
 
def update_videos():
    UpdateVideos(tk.Toplevel(main_window))
    status_label.config(text="Update Video button was clicked successfully!")

main_window = tk.Tk()
main_window.geometry("520x150")
main_window.title("Video Player")
 
fonts.configure()
 
header_label = tk.Label(main_window, text="Select an option by clicking one of the buttons below")
header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
 
check_video_button = tk.Button(main_window, text="Check Video", command=check_video)
check_video_button.grid(row=1, column=0, padx=10, pady=10)
 
create_video_list_button = tk.Button(main_window, text="Create Video List", command=create_video_list)
create_video_list_button.grid(row=1, column=1, padx=10, pady=10)
 
update_video_button = tk.Button(main_window, text="Update Videos", command=update_videos)
update_video_button.grid(row=1, column=2, padx=10, pady=10)
 
status_label = tk.Label(main_window, text="", font=("Helvetica", 10))
status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
 
main_window.mainloop()