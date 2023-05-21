from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time



def track_ride():
    # Create a new tkinter window
    window = tk.Tk()
    window.title("Ride Tracking")
    window.geometry("400x200")

    # Create labels to display ride information
    distance_label = tk.Label(window, text=f"Distance: {5} miles")
    distance_label.pack()

    source_label = tk.Label(window, text=f"Source: alaama stret")
    source_label.pack()

    destination_label = tk.Label(window, text=f"Destination: university")
    destination_label.pack()

    # Create a label to display the current location
    location_label = tk.Label(window, text="Current Location: ")
    location_label.pack()

    print(f"Ride distance: {5} miles")
    print("Tracking ride in real-time...\n")

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

name_label = Label(window, text="You are in ")
name_label.pack()
name_entry = Entry(window)
name_entry.insert(0, ["name"])  # Populate with the existing name
name_entry.pack()

# Example usage:

track_ride()
