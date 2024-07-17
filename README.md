# Hall-effect-sensor-plotter
A python code, to plot the incoming data from Hall effect instrument, provides a better way to visualize the magnetic field density

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
