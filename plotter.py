import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Initialize serial port (replace 'COM3' with your specific COM port)
ser = serial.Serial('COM3', 9600, timeout=1)

# Initialize Tkinter
root = tk.Tk()
root.title("Hall Effect Serial Data Receiver")
root.geometry("600x800")  # Set window size to 600x800 pixels

# Label for instructions
instruction_label = tk.Label(root, text="Select COM Port and Press Start Button on Instrument...")
instruction_label.pack(pady=10)

# Dropdown menu for COM ports
available_ports = serial.tools.list_ports.comports()
com_ports = ttk.Combobox(root, values=[port.device for port in available_ports])
com_ports.pack()

# Label to display status
status_label = tk.Label(root, text="STOPPED", font=("Helvetica", 18))
status_label.pack(pady=20)

# Matplotlib plot setup
fig = Figure(figsize=(5, 6), dpi=100) # Adjust figure size to fit the window
ax = fig.add_subplot(111)
ax.set_xlabel('Count')
ax.set_ylabel('Sensor Value')
ax.set_title('Hall Effect Sensor Value Plot')
ax.grid(True)  # Add grid lines
ax.axhline(y=0, color='red', linestyle='--')  # Make y=0 axis line red and dashed
line1, = ax.plot([], [], 'o-', label='Sensor Value')
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Pack canvas to fill entire window

# Initialize data lists for plotting
sensor_values = []
count_values = []

# Function to update the plot
def update_plot():
    ax.clear()  # Clear previous plot
    ax.set_xlabel('Count')
    ax.set_ylabel('Sensor Value')
    ax.set_title('Hall Effect Sensor Value Plot')
    ax.grid(True)  # Add grid lines
    ax.axhline(y=0, color='red', linestyle='--')  # Ensure y=0 axis line remains red and dashed
    ax.plot(count_values, sensor_values, 'o-', label='Sensor Value')
    ax.legend()
    canvas.draw()

# Function to update status and plot based on received data
def update_status_and_plot():
    # Check if there's data available to read from serial port
    if ser.in_waiting > 0:
        # Read the data and decode it from bytes to string
        data = ser.readline().decode('utf-8', errors='ignore').strip()
        if data:
            try:
                # Split the received data into components: sensor value, pole value, count value
                sensor_value, pole_value, count_value = map(float, data.split(','))

                # Update status label based on the received values
                if sensor_value == 0 and count_value == 0:
                    status_label.config(text="STOPPED")
                else:
                    status_label.config(text="STARTED")
                    sensor_values.append(sensor_value)
                    count_values.append(count_value)
                    update_plot()  # Update plot with new data

                # Print data to console
                print(f"{sensor_value},{pole_value},{count_value}")
                
            except ValueError:
                print(f"Invalid data: {data}")  # Handle invalid data format
        root.after(100, update_status_and_plot)  # Schedule the next update after 100ms
    else:
        root.after(100, update_status_and_plot)  # Schedule the next update after 100ms if no data yet

# Start updating status and plot
update_status_and_plot()

# Function to close the serial port and exit the program
def close_port():
    if ser.is_open:
        ser.close()  # Close the serial port
    root.destroy()  # Close the Tkinter window

# Close button to stop reading and close the program
close_button = tk.Button(root, text="Close", command=close_port)
close_button.pack(pady=10)

# Start Tkinter main loop
root.mainloop()
