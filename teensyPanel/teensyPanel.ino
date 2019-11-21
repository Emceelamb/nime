const int channel = 1

                    const int sw0 = 0;
const int sw1 = 1;
const int sw2 = 2;
const int sw3 = 3;
const int sw4 = 4;
const int sw5 = 5;
const int sw6 = 6;
const int sw7 = 7;
const int sw8 = 8;
const int sw9 = 9;

int sw0_state = 0;
int sw1_state = 0;
int sw2_state = 0;
int sw3_state = 0;
int sw4_state = 0;
int sw5_state = 0;
int sw6_state = 0;
int sw7_state = 0;
int sw8_state = 0;
int sw9_state = 0;

int sw0_prev = 0;
int sw1_prev = 0;
int sw2_prev = 0;
int sw3_prev = 0;
int sw4_prev = 0;
int sw5_prev = 0;
int sw6_prev = 0;
int sw7_prev = 0;
int sw8_prev = 0;
int sw9_prev = 0;

const int delayTime = 100;
unsigned long prevDelay = 0;

void setup() {
  setPins();
  Serial.begin(38400);
}

void loop() {
  readPins();
  unsigned long currentMS = millis();
  toggleSwitches(currentMS);
  switchState();
}
