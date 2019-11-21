const int switchPin = 7;
int switchState = 0;
int switchPrev = 0;

const int delayTime = 100;
unsigned long prevDelay = 0;

void setup() {
  pinMode(switchPin, INPUT);
  Serial.begin(38400);
  Serial.println("Program Start");
}

void loop() {
  switchState = digitalRead(switchPin);
  unsigned long currentMS = millis();


  if (switchState != switchPrev && currentMS - prevDelay > delayTime) {
    prevDelay = currentMS;
    if (switchState == HIGH) {
      Serial.println("on");
    } else {
      Serial.println("off");
  }    }

  switchPrev = switchState;
 }
