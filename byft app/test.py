import tkinter as tk
from tkinter import messagebox
import driver

def find_driver():
    driver_origin = driver_origin_entry.get()
    driver_destination = driver_destination_entry.get()

    user_origin = user_origin_entry.get()
    user_destination = user_destination_entry.get()

    try:
        driver_roads = driver.get_street_list(driver_origin, driver_destination)

        if user_origin in driver_roads and user_destination in driver_roads:
            result_label.config(text="You have found a driver!")
        else:
            result_label.config(text="Sorry, can't find a driver for your route.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Driver Finder")

# Create entry widgets for driver's origin and destination addresses
driver_origin_label = tk.Label(root, text="Enter the driver's origin address:")
driver_origin_label.grid(row=0, column=0, padx=10, pady=5)
driver_origin_entry = tk.Entry(root)
driver_origin_entry.grid(row=0, column=1, padx=10, pady=5)

driver_destination_label = tk.Label(root, text="Enter the driver's destination address:")
driver_destination_label.grid(row=1, column=0, padx=10, pady=5)
driver_destination_entry = tk.Entry(root)
driver_destination_entry.grid(row=1, column=1, padx=10, pady=5)

# Create entry widgets for user's origin and destination addresses
user_origin_label = tk.Label(root, text="Enter your origin address:")
user_origin_label.grid(row=2, column=0, padx=10, pady=5)
user_origin_entry = tk.Entry(root)
user_origin_entry.grid(row=2, column=1, padx=10, pady=5)

user_destination_label = tk.Label(root, text="Enter your destination address:")
user_destination_label.grid(row=3, column=0, padx=10, pady=5)
user_destination_entry = tk.Entry(root)
user_destination_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a button to trigger the search for a driver
search_button = tk.Button(root, text="Find Driver", command=find_driver)
search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()




#origin = '2001 S Summit Ave, Sioux Falls, SD 57197'
#destination = '1421 Student Union Ln, Brookings, SD 57007'
    
    

