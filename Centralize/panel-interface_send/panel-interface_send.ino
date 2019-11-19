const int knob3 = A0;

const int sw0 = 13;
const int sw1 = 12;
const int sw2 = 11;
const int sw3 = 10;
const int sw4 = 9;
const int sw5 =  8;
const int sw6 =  7;
const int sw7 =  6;
const int sw8 =  5;
const int sw9 =  4;

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

bool sw0_send = false;
bool sw1_send = false;
bool sw2_send = false;
bool sw3_send = false;
bool sw4_send = false;
bool sw5_send = false;
bool sw6_send = false;
bool sw7_send = false;
bool sw8_send = false;
bool sw9_send = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(sw0, INPUT);
  pinMode(sw1, INPUT);
  pinMode(sw2, INPUT);
  pinMode(sw3, INPUT);
  pinMode(sw4, INPUT);
  pinMode(sw5, INPUT);
  pinMode(sw6, INPUT);
  pinMode(sw7, INPUT);
  pinMode(sw8, INPUT);
  pinMode(sw9, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sw0_state = digitalRead(sw0);
  sw1_state = digitalRead(sw1);
  sw2_state = digitalRead(sw2);
  sw3_state = digitalRead (sw3);
  //  sw4_state = digitalRead(sw4);
  sw5_state = digitalRead(sw5);
  sw6_state = digitalRead(sw6);
  sw7_state = digitalRead(sw7);
  sw8_state = digitalRead(sw8);
  sw9_state = digitalRead(sw9);
  //  Serial.println(sw8_state);
  toggleSwitch(sw0, sw0_state, sw0_prev, sw0_send);
  toggleSwitch(sw1, sw1_state, sw1_prev, sw1_send);
  toggleSwitch(sw2, sw2_state, sw2_prev, sw2_send);
  toggleSwitch(sw3, sw3_state, sw3_prev, sw3_send);
  toggleSwitch(sw4, sw4_state, sw4_prev, sw4_send);
  toggleSwitch(sw5, sw5_state, sw5_prev, sw5_send);
  toggleSwitch(sw6, sw6_state, sw6_prev, sw6_send);
  toggleSwitch(sw7, sw7_state, sw7_prev, sw7_send);
  toggleSwitch(sw8, sw8_state, sw8_prev, sw8_send);
  toggleSwitch(sw9, sw9_state, sw9_prev, sw9_send);

  sw0_prev = sw0_state;
  sw0_send = sw0_state;

  sw1_prev = sw1_state;
  sw1_send = sw1_state;

  sw2_prev = sw2_state;
  sw2_send = sw2_state;

  sw3_prev = sw3_state;
  sw3_send = sw3_state;

  sw4_prev = sw4_state;
  sw4_send = sw4_state;

  sw5_prev = sw5_state;
  sw5_send = sw5_state;

  sw6_prev = sw6_state;
  sw6_send = sw6_state;

  sw7_prev = sw7_state;
  sw7_send = sw7_state;

  sw8_prev = sw8_state;
  sw8_send = sw8_state;

  sw9_prev = sw9_state;
  sw9_send = sw9_state;

  int knob3val = analogRead(knob3);
  sendVal(sw0, sw0_send, knob3val);
  sendVal(sw1, sw1_send, knob3val);
  sendVal(sw2, sw2_send, knob3val);
  sendVal(sw3, sw3_send, knob3val);
  sendVal(sw4, sw4_send, knob3val);
  sendVal(sw5, sw5_send, knob3val);
  sendVal(sw6, sw6_send, knob3val);
  sendVal(sw7, sw7_send, knob3val);
  sendVal(sw8, sw8_send, knob3val);
  sendVal(sw9, sw9_send, knob3val);
}

void toggleSwitch(int sw, int sw_state, int sw_prev, bool sw_send) {
  if (sw_state != sw_prev) {
    if (sw_state == HIGH) {
      sw_send = true;
      Serial.print(sw);
      Serial.println(" on");
      Serial.println(sw_send);
    } else {
      Serial.print(sw);
      Serial.println(" off");
      sw_send = false;
    }
    delay(50);
  }
}

void sendVal(int sw, int sw_send, int knobval) {
  //  Serial.println(sw_send);
  if (sw_send == true) {
    Serial.print(sw);
    Serial.print(", ");
    Serial.print(sw_send);
    Serial.print(", ");
    Serial.println(knobval);

    //    Serial.write(knobval);

  }
  //  Serial.println(knob);
}

