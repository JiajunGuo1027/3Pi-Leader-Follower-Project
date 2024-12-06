#include "Motors.h"

Motors_c motors;

// Sensor pin definitions
const int leftBumpSensorPin = A6;    // Left bump sensor (ADC input)
const int rightBumpSensorPin = 5;   // Right bump sensor (Digital input)
const int EMIT_PIN = 11;             // Infrared emitter control pin

void setup()
{
  // Initialize serial communication
  Serial.begin(9600);

  // Configure sensor pins
  pinMode(leftBumpSensorPin, INPUT_PULLUP);
  pinMode(rightBumpSensorPin, INPUT_PULLUP);

  // Disable Follower's infrared emitter
  pinMode(EMIT_PIN, INPUT); // Set EMIT as INPUT to avoid interfering with the Leader's infrared signal

  // Initialize motors
  motors.initialise();

  // Notification message
  Serial.println("Follower Car Initialized");
}

void loop()
{
  // Read the value of the left sensor
  int leftBumpValue = analogRead(leftBumpSensorPin);

  // Control speed based on the left sensor value
  //int speed = 0;  // Default to stop

  if (leftBumpValue > 800 || leftBumpValue < 50) {
    // Stop
    //speed = 0;
    motors.setPWM(0, 0);
    Serial.println("Stopping: Left sensor > 800 or < 50");
  } else if (leftBumpValue >= 600 && leftBumpValue <= 700) {
    // Accelerate
    //speed = 20;
    motors.setPWM(20, 20);
    delay(1000);
    Serial.println("Accelerating: Left sensor in [600, 700]");
  } else if (leftBumpValue > 100 && leftBumpValue < 600) {
    // Maintain constant speed
    //speed = 18;
    motors.setPWM(18, 16);
    Serial.println("Moving at normal speed: Left sensor in [100, 600]");
  } else if (leftBumpValue >= 50 && leftBumpValue <= 100) {
    // Decelerate
    //speed = 14;
    motors.setPWM(15, 11);
    Serial.println("Decelerating: Left sensor in [50, 100]");
  }

  // Set motor speed
  //motors.setPWM(speed, speed);

  Serial.print("Left Bump Sensor (ADC): ");
  Serial.println(leftBumpValue);
  // Serial.print("\tCurrent Speed: ");
  // Serial.println(speed);

  delay(100);  
}
