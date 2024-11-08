import tkinter as tk

def send_notification():
    print("Notification sent!")

def cre_main_window():
    root = tk.Tk()
    root.title("Sales Manager")
    root.geometry("400x300")

    label = tk.Label(root, text="Welcome!", font=("Arial", 16))
    label.pack(pady=10)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    button = tk.Button(root, text="Send Notification", command=send_notification)
    button.pack(pady=10)

    root.mainloop()