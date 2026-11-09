import tkinter as tk
from tkinter import ttk


def configure_table_style(widget):
    style = ttk.Style(widget)

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure(
        "Treeview",
        font=("Segoe UI", 10),
        rowheight=32,
        background="#ffffff",
        foreground="#222222",
        fieldbackground="#ffffff",
        borderwidth=0,
        padding=(6, 5),
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        rowheight=36,
        padding=(8, 8),
    )

