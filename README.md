# Hall-effect-sensor-plotter
A python code, to plot the incoming data from Hall effect instrument, provides a better way to visualize the magnetic field density

![image](https://github.com/user-attachments/assets/77198d2d-3fe8-4cc5-845c-b7cb0eb69ed3)


## Instrument Code:

- **Variables Declaration:**
  - `sensorPin`: Pin connected to the Hall effect sensor.
  - `ledPin`: Pin connected to the LED.
  - `sensorValue`: Holds the current sensor reading.
  - `pole`: Indicates the polarity of the sensor reading (-1 for south, 1 for north).
  - `count`: Counts the number of readings.
  - `startButtonPin`: Pin connected to the start button.
  - `startButtonState`: Keeps track of whether the start button is pressed or not.

- **Setup Function (`setup()`):**
  - Sets `ledPin` as output for controlling the LED.
  - Sets `startButtonPin` as input with a built-in pull-up resistor.
  - Initializes serial communication at 9600 baud rate.

- **Main Loop (`loop()`):**
  - Reads the state of `startButtonPin` to determine if the start button is pressed (`LOW`).
  - If the button is pressed, it reads the `sensorPin` to get the `sensorValue`.
  - Prints the `sensorValue`, `pole`, and `count` to serial in CSV format.
  - Determines the `pole` (north or south) based on `sensorValue` and controls the LED accordingly.
  - If the button is not pressed, it prints default values (`0,0,0`) to indicate stopped state.
  - Adds a delay of 500 milliseconds (`delay(500)`) to control the rate of readings.
  - Increments the `count` for each loop iteration.

### Adjustments:
- Adjust the `sensorValue > 1` threshold based on sensor characteristics to correctly determine north or south pole.


## Python Plotting Code

1. **Imports and Serial Initialization:**
   - Imports necessary libraries (`serial`, `tkinter`, `matplotlib`) and initializes the serial port (`ser`) with specific settings (`'COM3'` and `9600` baud rate).

2. **Tkinter GUI Setup:**
   - Creates a Tkinter window (`root`) with a title and size (`600x800` pixels).
   - Adds a label (`instruction_label`) for user instructions.
   - Sets up a dropdown menu (`com_ports`) to select COM ports.
   - Displays a status label (`status_label`) indicating the current state.

3. **Matplotlib Plot Setup:**
   - Creates a Matplotlib figure (`fig`) with a specific size and DPI.
   - Adds a subplot (`ax`) with labels and a title for the Hall Effect sensor plot.
   - Configures grid lines (`ax.grid(True)`) and a red dashed line at y=0 (`ax.axhline(...)`).
   - Initializes an empty plot (`line1`) with legend (`ax.legend()`) and embeds it into a Tkinter canvas (`canvas`).
   - `NavigationToolbar2Tk` which provides a Matplotlib toolbar, provides zoom, pan, and save functionalities,

4. **Data Handling Functions:**
   - `update_plot()`: Clears the current plot, updates it with new sensor data (`sensor_values` and `count_values`), and redraws the canvas (`canvas.draw()`).
   - `update_status_and_plot()`: Checks for incoming data from `ser`, processes it, updates the status label, adds valid data to lists for plotting, and calls `update_plot()` to refresh the plot.
   - Handles exceptions (`ValueError`) if data format is invalid and prints error messages to console.

5. **Serial Port Management and GUI Controls:**
   - `close_port()`: Closes the serial port (`ser`) if it's open and destroys the Tkinter window (`root`) to exit the application.
   - Creates a close button (`close_button`) that calls `close_port()` when clicked, allowing the user to stop reading data and close the program.

6. **Main Loop (`root.mainloop()`):**
   - Starts the Tkinter main loop to handle events and maintain the GUI application.


Certainly! Here's a revised version of the TO DO's section suitable for GitHub:


## TO DO's:

1. **Implement Ratiometric Hall Effect Sensor:**
   - Integrate a ratiometric Hall effect sensor to enhance accuracy in measuring magnetic field intensity. Hall effect sensor with a wide measurement range and high sensitivity. Ratiometric Hall effect sensors are often preferred because they provide an output voltage proportional to the magnetic field strength, making them suitable for accurate measurements across a wide range.
   - Ensure proper calibration procedures to standardize measurements for consistent results.

2. **Upgrade from 8-bit Microcontroller:**
   - Replace the current 8-bit microcontroller setup with a more capable system to handle increased sensor data resolution.
   - Enable higher precision in capturing and processing magnetic field data.

3. **Current Sensor Setup (Example):**
   - Currently using the `A3144` Hall effect sensor.
   - Provides basic detection of magnetic poles but lacks accuracy for precise measurements.

