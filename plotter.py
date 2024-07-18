import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Initialize serial port (replace 'COM3' with your specific COM port)
ser = serial.Serial('COM3', 9600, timeout=1)

# Initialize Tkinter
root = tk.Tk()
root.title("Hall Effect Serial Data Receiver")
root.geometry("600x800")  # Set window size to 600x800 pixels

# Frame for status label
label_frame = tk.Frame(root)
label_frame.pack(pady=5)

# Label for instructions
instruction_label = tk.Label(label_frame, text="Select COM Port and Press Start Button on Instrument...")
instruction_label.pack(pady=5)

# Frame for COM port selector and close button
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Dropdown menu for COM ports
available_ports = serial.tools.list_ports.comports()
com_ports = ttk.Combobox(top_frame, values=[port.device for port in available_ports])
com_ports.pack(side=tk.LEFT, padx=10)

# Close button to stop reading and close the program
def close_port():
    if ser.is_open:
        ser.close()  # Close the serial port
    root.destroy()  # Close the Tkinter window

close_button = tk.Button(top_frame, text="Close", command=close_port)
close_button.pack(side=tk.RIGHT, padx=10)

# Frame for status label
status_frame = tk.Frame(root)
status_frame.pack(pady=10)

# Label to display status
status_label = tk.Label(status_frame, text="STOPPED", font=("Helvetica", 18))
status_label.pack()

# Matplotlib plot setup
plot_frame = tk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

fig = Figure(figsize=(5, 6), dpi=100)  # Adjust figure size to fit the window
ax = fig.add_subplot(111)
ax.set_xlabel('Count')
ax.set_ylabel('Sensor Value')
ax.set_title('Hall Effect Sensor Value Plot')
ax.grid(True)  # Add grid lines
ax.axhline(y=0, color='red', linestyle='--')  # Make y=0 axis line red and dashed
line1, = ax.plot([], [], 'o-', label='Sensor Value')
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Pack canvas to fill entire window

# Add Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, plot_frame)
toolbar.update()
canvas.get_tk_widget().pack()

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
    global status_label  # Access global status_label
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

# Start Tkinter main loop
root.mainloop()
