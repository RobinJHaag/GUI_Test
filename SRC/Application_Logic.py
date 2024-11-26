import pandas as pd
from tkinter import filedialog


def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx;*.xls")]
    )
    return file_path


def load_data(file_path):
    df = pd.read_excel(file_path)
    if df.columns[0] == 'Unnamed: 0':
        df = pd.read_excel(file_path, index_col=0)
    return df
