#include "Wire.h"
#include "BlinkM_funcs.h"

#define blinkm_addr 0x00

boolean handShake = false;
const int beat_pin = 13;

int beatState = LOW;
long prevMillis = 0;
unsigned long currentMillis;
int beat_time = 500;
int state = 3;

void turn_off(){
  BlinkM_setRGB( blinkm_addr, 0x00, 0x00, 0x00); 
}

void turn_red(){
  BlinkM_setRGB( blinkm_addr, 0xff, 0x00, 0x00); 
}

void turn_orange(){
  BlinkM_setRGB( blinkm_addr, 0xff, 0xff, 0x00); 
}

void turn_cyan(){
  BlinkM_setRGB( blinkm_addr, 0x00, 0xff, 0xff); 
}

void setup() {
  BlinkM_beginWithPower();  
  BlinkM_stopScript( blinkm_addr ); 
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

   if (state == 0) {
      turn_red(); 
   }
   if (state == 1) {
      turn_orange(); 
   }
   if (state == 2) {
      turn_cyan(); 
   }
   if (state == 3) {
      turn_off(); 
   }

}

void ack() {
      for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
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
    if (inChar == 'r') {      
      state = 0;
      for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
      }   
    }
    if (inChar == 'o') {
      state = 1;
      for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
      }   
    }
    if (inChar == 'c') {      
      state = 2;
      for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
      }   
    }    
    if (inChar == 'x') {
      state = 3; 
       for (int i = 0; i < 50; i++)
      {
        Serial.println("T");
      }   
    }
  }
}


