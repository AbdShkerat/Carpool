from tkinter import *
import tkinter as tk

# Sample data for ride listings
rides = [
    {
        "driver": "John",
        "departure_time": "09:00 AM",
        "destination": "City Center",
        "rating": 4.5,
        "car": "Toyota Camry",
        "arrival_time": "09:30 AM",
        "price": 10
    },
    {
        "driver": "Sarah",
        "departure_time": "10:30 AM",
        "destination": "Shopping Mall",
        "rating": 4.8,
        "car": "Honda Civic",
        "arrival_time": "11:00 AM",
        "price": 8
    },
    # Add more ride listings as needed
]

def search_rides():
    pickup = pickup_entry.get()
    dropoff = dropoff_entry.get()

    # TODO: Implement search functionality based on pickup and dropoff locations

    # Display search results
    display_rides()

def display_rides():
    # Clear any previous ride listings
    ride_listbox.delete(0, END)

    # Iterate over rides and display relevant information in the ride listbox
    for ride in rides:
        ride_info = f"Driver: {ride['driver']}\n" \
                    f"Departure: {ride['departure_time']}\n" \
                    f"Destination: {ride['destination']}\n" \
                    f"Rating: {ride['rating']}\n" \
                    f"Car: {ride['car']}\n" \
                    f"Arrival: {ride['arrival_time']}\n" \
                    f"Price: ${ride['price']}\n" \
                    f"--------------------------"
        ride_listbox.insert(END, ride_info)

# Create a new tkinter window
window = Tk()
window.title("Carbool App - Home Screen")

# Load the image
image_path = "car.png"  # Replace with the actual path to your image
photo = PhotoImage(file=image_path)
width = 1000  # Desired width
height = 1000  # Desired height
# Resize the image
resized_photo = photo.subsample(1, 1)  # Adjust the subsample values as needed

# Create a label widget to display the image
image_label = Label(window, image=resized_photo)
image_label.pack()

# Create labels and entry fields for pickup and dropoff locations
pickup_label = Label(window, text="Pickup Location:")
pickup_label.pack()
pickup_entry = Entry(window)
pickup_entry.pack()

dropoff_label = Label(window, text="Dropoff Location:")
dropoff_label.pack()
dropoff_entry = Entry(window)
dropoff_entry.pack()

# Create a button to initiate the ride search
search_button = Button(window, text="Search Rides", command=search_rides)
search_button.pack()

# Create a listbox to display ride listings
ride_listbox = Listbox(window)
ride_listbox.pack()

# Display initial ride listings
display_rides()

# Start the tkinter event loop
window.mainloop()
