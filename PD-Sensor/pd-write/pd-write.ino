int potPin0 = 0;    // select the input pin for the potentiometer
int potPin1 = 1;
int potPin2 = 2;
int potPin3 = 3;

int val0 = 0;       // variable to store the value coming from the sensor
int val1 = 0;
int val2 = 0;
int val3 = 0;


void setup() {
  Serial.begin(9600);
}

void loop() {
  val0 = analogRead(potPin0);    // read the value from the sensor
  val1 = analogRead(potPin1);
  val2 = analogRead(potPin2);
  val3 = analogRead(potPin3);
  
// Serial.print(val);
//  Serial.println();
  val0 = val0/4;
  val1 = val1/4;
  val2 = val2/4;    
  val3 = val3/4;    
//  Seria/l.write(val);
  Serial.write(val0);
  Serial.write(val1);
  Serial.write(val2);
  Serial.write(val3);
  delay(100);
}
