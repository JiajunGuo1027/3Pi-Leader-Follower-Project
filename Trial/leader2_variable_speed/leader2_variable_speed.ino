#include "Motors.h"   
Motors_c motors;
const int EMIT_PIN = 11;  
#define L_PWM 10 // This is correct.
#define L_DIR 16 // This is the wrong pin! 
#define R_PWM 9 // This is the wrong pin! 
#define R_DIR 15 // This is the wrong pin! 

int start_time = 0;

void setup()
{
  pinMode(L_PWM, OUTPUT);
  pinMode(L_DIR, OUTPUT);
  pinMode(R_PWM, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  Serial.begin(9600);

  pinMode(A2, INPUT_PULLUP);
  pinMode(EMIT_PIN, OUTPUT);
  digitalWrite(EMIT_PIN, HIGH); 

  Serial.println("Leader Car Initialized");
}
int change_time = 0;
int start_flag = 1;
void loop()
{
  if(start_flag == 1){
    start_time = millis();
    start_flag = 0;
  }
  change_time = millis();
  if(change_time-start_time<5000){
    motors.setPWM(-15,-15);
  }else if(change_time-start_time<10000){
    motors.setPWM(-20,-20);
  }else if(change_time-start_time<15000){
    motors.setPWM(-15,-15);
  }else if(change_time-start_time<20000){
    motors.setPWM(-20,-20);
  }else{
    motors.setPWM(0,0);
  }
  Serial.print(start_time);
  Serial.print(",");
  Serial.println(change_time);
}
