from tkinter import *
import tkinter as tk


def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Image Display")

    # Load the image
    image_path = "car.png"  # Replace with the actual path to your image
    photo = PhotoImage(file=image_path)

    # Resize the photo
    width = 400  # Desired width
    height = 400  # Desired height
    resized_photo = photo.subsample(int(photo.width() / width), int(photo.height() / height))

    # Create a label widget to display the resized image
    label = tk.Label(window, image=resized_photo)
    label.pack()

    # Run the GUI event loop
    window.mainloop()


def register():

    # Get user input from entry fields
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # TODO: Perform validation and store user information in a database or file

    # Show a message or redirect to the next onboarding step
    registration_label.config(text="Registration successful!")

# Create a new tkinter window
# window = Tk()
# window.title("Carbool App Registration")
# window.geometry("300x200")
window = tk.Tk()
window.title("Image Display")
window.title("Carbool App Registration")

# Load the image
image_path = "logo.png"  # Replace with the actual path to your image
photo = PhotoImage(file=image_path)

# Resize the photo
width = 400  # Desired width
height = 400  # Desired height
resized_photo = photo.subsample(int(photo.width() / width), int(photo.height() / height))

# Create a label widget to display the resized image
label = tk.Label(window, image=resized_photo)
label.pack()

# Create labels and entry fields for user input
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = Entry(window)
email_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

# Create a button to initiate the registration process
register_button = tk.Button(window, text="Register", command=register)
register_button.pack()

# Display a label to show registration status
registration_label = tk.Label(window, text="")
registration_label.pack()

# Start the tkinter event loop
window.mainloop()
