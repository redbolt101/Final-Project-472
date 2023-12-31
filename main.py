import tkinter as tk
from tkinter import messagebox
import random
import threading
import time
from datetime import datetime

def create_fall_detection_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Fall Detection System")

    # List to keep track of fall events
    fall_log = []

    # Function to show an alert for fall detection
    def show_fall_alert():
        fall_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showwarning("Fall Detected", f"A fall has been detected at {fall_time}! Immediate assistance is required.")
        fall_log.append(fall_time)
        # For debugging, you can print the log to the console
        print(fall_log)

    # Function to simulate continuous fall monitoring (a background process)
    def monitor_falls():
        while True:
            time.sleep(5)  # Wait for 5 seconds between checks
            if random.choice([True, False]):
                # If a fall is detected, update the GUI from the main thread
                root.after(0, show_fall_alert)

    # Start the background monitoring process
    monitor_thread = threading.Thread(target=monitor_falls, daemon=True)
    monitor_thread.start()

    # Start the GUI event loop
    root.mainloop()

# Run the function to create the GUI
create_fall_detection_gui()
