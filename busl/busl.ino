boolean handShake = false;

void setup() {
  Serial.begin(9600);
}

void loop() {
   if (handShake == false) {
     Serial.println("R");
   }

}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read(); 
    if (inChar == 'H') {
      for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
      }
      handShake = true;
    }
  }
}


