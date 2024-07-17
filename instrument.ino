int sensorPin = A0;          // Pin for the Hall effect sensor
int ledPin = 13;             // Pin for the LED
int sensorValue = 0;         // Variable to store the sensor value
int pole = -1;               // Flag for magnet polarity (-1 for south, 1 for north)
int count = 0;               // Variable to count readings
int startButtonPin = 2;      // Pin for the start button
int startButtonState = 0;    // State of the start button (HIGH or LOW)

void setup() {
  pinMode(ledPin, OUTPUT);                  // LED pin as output
  pinMode(startButtonPin, INPUT_PULLUP);    // Start button pin with internal pull-up resistor
  Serial.begin(9600);                       // Initialize serial communication at 9600 baud
}

void loop() {
  startButtonState = digitalRead(startButtonPin);  // Read the state of the start button

  if (startButtonState == LOW) {  // If start button is pressed (LOW means grounded)
    
    sensorValue = analogRead(sensorPin);  // Read sensor value from Hall effect sensor

    // Print sensor value, pole value, and count to serial in CSV format
    Serial.print(sensorValue);  
    Serial.print(",");
    Serial.print(pole);  
    Serial.print(",");
    Serial.println(count);  

    // Determine the pole (north or south) and control the LED accordingly
    if (sensorValue > 1) {  // Adjust this threshold based on your sensor characteristics
      if (pole != 1) {   // if not already flagged 
        pole = 1;                    // Set pole flag to north
        digitalWrite(ledPin, HIGH);  // Turn LED on
      }
    } else {
      if (pole != -1) {  
        pole = -1;                   // Set pole flag to south
        digitalWrite(ledPin, LOW);   // Turn LED off
      }
    }

  } else {
    // If start button is not pressed, print default values to serial
    Serial.print(0);  
    Serial.print(",");
    Serial.print(0);  
    Serial.print(",");
    Serial.println(0);  
  }

  delay(500);  // Delay between readings
  count++;     // Increment the count for each reading
}
