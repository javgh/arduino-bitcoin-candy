const int motorPin = 12;
const int motorRunTime = 1500;

boolean triggerMotorEvent = false;

void setup() {
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
}

void serialEvent() {
  // read everything available at the moment
  while (Serial.available()) {
    Serial.read(); // not interested in payload
  }
  triggerMotorEvent = true;
}


void loop() {
  if (triggerMotorEvent) {
    digitalWrite(motorPin, HIGH);
    delay(motorRunTime);
    digitalWrite(motorPin, LOW);
    triggerMotorEvent = false;
  }
}
