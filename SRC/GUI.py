import customtkinter
import Application_Logic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_data(df, plot_type, frame):
    frame.destroy()
    frame = customtkinter.CTkFrame(master=app, corner_radius=0)
    frame.grid(row=1, column=0, sticky="nsew")

    fig, ax = plt.subplots()
    colors = plt.cm.Oranges(range(len(df.columns)))

    if plot_type == "Bar":
        df.plot(kind='bar', ax=ax, color=colors)
    elif plot_type == "Pie":
        df.iloc[0].plot(kind='pie', ax=ax, colors=colors, autopct='%1.1f%%')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def on_button_click(label, frame, plot_type):
    file_path = Application_Logic.select_file()
    if file_path:
        label.configure(text=f"Selected file: {file_path}")
        df = Application_Logic.load_data(file_path)
        plot_data(df, plot_type, frame)

def create_app():
    global app
    app = customtkinter.CTk()
    app.title("Excel Plotter")
    app.geometry("800x600")
    app.configure(bg="#3e4348")

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=0)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=0)

    top_frame = customtkinter.CTkFrame(master=app, corner_radius=0)
    top_frame.grid(row=0, column=0, sticky="nsew")

    title_label = customtkinter.CTkLabel(
        master=top_frame,
        text="Excel Plotter",
        font=("Arial", 24),
        text_color="#FF5733",
    )
    title_label.pack(pady=10)

    middle_frame = customtkinter.CTkFrame(master=app, corner_radius=0)
    middle_frame.grid(row=1, column=0, sticky="nsew")

    file_label = customtkinter.CTkLabel(
        master=middle_frame,
        text="No file selected",
        font=("Arial", 16),
        text_color="#FFFFFF",
    )
    file_label.pack(pady=20)

    bottom_frame = customtkinter.CTkFrame(master=app, corner_radius=0)
    bottom_frame.grid(row=2, column=0, sticky="nsew")

    button_style = {
        "fg_color": "#2b2e31",
        "border_color": "#FF5733",
        "hover_color": "#7B0323",
        "text_color": "#FF5733",
        "border_width": 1
    }

    select_file_button = customtkinter.CTkButton(
        master=bottom_frame,
        text="Select File",
        command=lambda: on_button_click(file_label, middle_frame, None),
        **button_style
    )
    select_file_button.pack(side="left", pady=20, padx=20)

    bar_button = customtkinter.CTkButton(

        master=bottom_frame,
        text="Bar Chart",
        command=lambda: on_button_click(file_label, middle_frame, "Bar"),
        **button_style
    )
    bar_button.pack(side="left", pady=20, padx=20)

    pie_button = customtkinter.CTkButton(
        master=bottom_frame,
        text="Pie Chart",
        command=lambda: on_button_click(file_label, middle_frame, "Pie"),
        **button_style
    )
    pie_button.pack(side="right", pady=20, padx=20)

    return app