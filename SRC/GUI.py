import customtkinter
from tkinter import filedialog


def on_button_click():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx;*.xls"), ("XML files", "*.xml")]
    )
    if file_path:
        print(f"Selected file: {file_path}")


def create_app():
    app = customtkinter.CTk()
    button = customtkinter.CTkButton(
        master=app,
        text="Select File",
        command=on_button_click,
        fg_color="purple",
        hover_color="blue",
        text_color="white"
    )
    button.pack(pady=20, padx=20)
    return app
