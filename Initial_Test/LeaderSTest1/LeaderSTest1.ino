#include "Motors.h"

Motors_c motors;
// Define infrared emitter pin
const int EMIT_PIN = 11;    // Infrared emitter control pin

void setup()
{
  // Initialize serial communication
  Serial.begin(9600);

  // Set the infrared emitter pin as output
  pinMode(EMIT_PIN, OUTPUT);
  digitalWrite(EMIT_PIN, LOW); // Activate the infrared emitter

  // Initialize motors
  motors.initialise();

  // Notification message
  Serial.println("Leader Car Initialized");
}

void loop()
{
  motors.setPWM(-15, -15);
  delay(5000);
  motors.setPWM(0, 0);
  delay(3000);
}
