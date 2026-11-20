import tkinter as tk

def show_greeting():
    patient_name = name_entry.get().strip()
    if patient_name == "":
        patient_name = "Patient"

    workshop_date = "November 25, 2026"

    message = (
        f"Hello {patient_name},\n\n"
        f"Welcome to our Health & Wellness Workshop.\n"
        f"Date: {workshop_date}\n\n"
        f"We are glad to have you with us today. Please take a seat and relax."
    )

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)
    output_text.config(state="disabled")

root = tk.Tk()
root.title("Workshop Patient Greeting")
root.geometry("420x340")
root.config(padx=15, pady=15)

instruction_label = tk.Label(root, text="Enter the patient's name below:", font=("Arial", 10))
instruction_label.pack(anchor="w", pady=5)

name_entry = tk.Entry(root, width=35, font=("Arial", 11))
name_entry.pack(anchor="w", pady=5)

greet_button = tk.Button(root, text="Generate Greeting", command=show_greeting, font=("Arial", 10))
greet_button.pack(anchor="w", pady=10)

output_label = tk.Label(root, text="Welcome Message:", font=("Arial", 10))
output_label.pack(anchor="w", pady=5)

output_text = tk.Text(root, height=8, width=45, font=("Arial", 10), wrap="word")
output_text.pack(anchor="w")
output_text.config(state="disabled")

root.mainloop()
