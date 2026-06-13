import tkinter as tk
from tkinter import filedialog, messagebox
import re

def extract_emails():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        emails = re.findall(
            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
            content
        )

        result_box.delete(1.0, tk.END)

        if emails:
            for email in emails:
                result_box.insert(tk.END, email + "\n")

            count_label.config(
                text=f"Total Emails Found: {len(emails)}"
            )

            with open("extracted_emails.txt", "w") as output:
                for email in emails:
                    output.write(email + "\n")

            messagebox.showinfo(
                "Success",
                "Emails extracted and saved successfully!"
            )

        else:
            count_label.config(text="No emails found.")
            messagebox.showwarning(
                "No Emails",
                "No email addresses found in the file."
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Smart Email Extractor")
root.geometry("600x450")

title = tk.Label(
    root,
    text="Email Extractor",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

btn = tk.Button(
    root,
    text="Select Text File",
    font=("Arial", 12),
    command=extract_emails
)
btn.pack(pady=10)

count_label = tk.Label(
    root,
    text="Total Emails Found: 0",
    font=("Arial", 12)
)
count_label.pack()

result_box = tk.Text(
    root,
    width=60,
    height=15
)
result_box.pack(pady=10)

root.mainloop()
