const int EMIT_PIN = 11;    // Infrared emitter control pin

void setup()
{
  // Initialize serial communication
  Serial.begin(9600);

  // Set the infrared emitter pin to output mode
  pinMode(EMIT_PIN, OUTPUT);
  digitalWrite(EMIT_PIN, LOW); // Activate the infrared emitter

  Serial.println("Leader Car Initialized");
}

void loop()
{

}