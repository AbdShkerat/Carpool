from tkinter import *

# Sample data for user profile and loyalty points
user_profile = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "payment_settings": {
        "card_number": "**** **** **** 1234",
        "expiration_date": "12/24",
        "security_code": "***"
    },
    "subscription": {
        "plan": "Gold",
        "expiry_date": "2023-12-31"
    },
    "loyalty_points": 500
}

def update_profile():
    # TODO: Implement the logic to update user profile
    profile_updated_label.config(text="Profile updated!")

def rate_driver():
    # TODO: Implement the logic to allow users to rate and review drivers
    rating_label.config(text="Driver rated!")

# Create a new tkinter window

window = Tk()
window.title("Carbool App - User Dashboard")
# window.geometry("400x400")

# Load the image
image_path = "car.png"  # Replace with the actual path to your image
photo = PhotoImage(file=image_path)
width = 800 # Desired width
height = 800  # Desired height
# Resize the image
resized_photo = photo.subsample(1, 1)  # Adjust the subsample values as needed

# Create a label widget to display the image
image_label = Label(window, image=resized_photo)
image_label.pack()

# Create labels and entry fields for user profile
name_label = Label(window, text="Name:")
name_label.pack()
name_entry = Entry(window)
name_entry.insert(0, user_profile["name"])  # Populate with the existing name
name_entry.pack()

email_label = Label(window, text="Email:")
email_label.pack()
email_entry = Entry(window)
email_entry.insert(0, user_profile["email"])  # Populate with the existing email
email_entry.pack()

payment_label = Label(window, text="Payment Settings:")
payment_label.pack()
card_label = Label(window, text="Card Number: " + user_profile["payment_settings"]["card_number"])
card_label.pack()
expiration_label = Label(window, text="Expiration Date: " + user_profile["payment_settings"]["expiration_date"])
expiration_label.pack()
security_label = Label(window, text="Security Code: " + user_profile["payment_settings"]["security_code"])
security_label.pack()

subscription_label = Label(window, text="Subscription:")
subscription_label.pack()
plan_label = Label(window, text="Plan: " + user_profile["subscription"]["plan"])
plan_label.pack()
expiry_label = Label(window, text="Expiry Date: " + user_profile["subscription"]["expiry_date"])
expiry_label.pack()

# Create buttons to update profile and rate drivers
update_button = Button(window, text="Update Profile", command=update_profile)
update_button.pack()

rating_button = Button(window, text="Rate Driver", command=rate_driver)
rating_button.pack()

# Display labels for profile update and driver rating results
profile_updated_label = Label(window, text="")
profile_updated_label.pack()

rating_label = Label(window, text="")
rating_label.pack()

# Create a label to show loyalty points
loyalty_points_label = Label(window, text="Loyalty Points: " + str(user_profile["loyalty_points"]))
loyalty_points_label.pack()

# Start the tkinter event loop
window.mainloop()
