void toggleSwitch(int sw, int sw_state, int sw_prev, unsigned long currentMS) {
  if (sw_state != sw_prev && currentMS - prevDelay > delayTime) {
    prevDelay = currentMS;
    if (sw_state == HIGH) {
      Serial.println("on");
    } else {
      Serial.println("off");
    }
  }
}
