void toggleSwitch(int sw, int sw_state, int sw_prev, unsigned long currentMS) {
  if (sw_state != sw_prev && currentMS - prevDelay > delayTime) {
    prevDelay = currentMS;
    int note = 60 + sw;
    if (sw_state == HIGH) {
      Serial.print(sw);
      Serial.println(" on");
      usbMIDI.sendNoteOn(note, 99, channel);
    } else {
      Serial.print(sw);
      Serial.println("off");
      usbMIDI.sendNoteOn(note, 99, channel);
    }
  }
}
