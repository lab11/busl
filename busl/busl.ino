boolean handShake = false;
const int beat_pin = 13;

int beatState = LOW;
long prevMillis = 0;
unsigned long currentMillis;
int beat_time = 500;

void setup() {
  Serial.begin(9600);
  pinMode(beat_pin, OUTPUT);
}

void loop() {
   if (handShake == false) {
     Serial.println("R");
   }

   if (currentMillis - prevMillis > beat_time) {
      prevMillis = currentMillis;   
      if (beatState == LOW)
        beatState = HIGH;
      else
        beatState = LOW;
      digitalWrite(beat_pin, beatState); 
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
    if (inChar == 'B') {
       currentMillis = millis(); 
    }
    if (inChar == '1') {
       
    }
    if (inChar == '2') {
      
    }
    if (inChar == '3') {
      
    }    
  }
}


