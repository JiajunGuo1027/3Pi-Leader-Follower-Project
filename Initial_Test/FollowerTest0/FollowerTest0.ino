const int leftBumpSensorPin = A6;   // Left bump sensor (ADC input)
const int rightBumpSensorPin = 5;   // Right bump sensor (Digital input)
const int EMIT_PIN = 11;            // EMIT pin, used to control the infrared emitter

const int distanceThreshold = 300;  // ADC threshold for distance determination
const int rightBumpDetected = HIGH; // State of the right bump sensor when infrared signal is detected

void setup() {
    Serial.begin(9600);

    // Configure sensor pins
    pinMode(leftBumpSensorPin, INPUT_PULLUP);
    pinMode(rightBumpSensorPin, INPUT_PULLUP);

    // Disable the infrared emitter of the Follower
    pinMode(EMIT_PIN, INPUT); 
}

void loop() {
    unsigned long timestamp = millis(); // Get the current time in milliseconds
    int leftBumpValue = analogRead(leftBumpSensorPin);
    int rightBumpValue = digitalRead(rightBumpSensorPin);

    // Output data in CSV format as "timestamp,left_value,right_value"
    Serial.print(timestamp);
    Serial.print(",");
    Serial.print(leftBumpValue);
    Serial.print(",");
    Serial.println(rightBumpValue);

    delay(100);
    
}