#include "Motors.h"   
#include "Kinematics.h"
#include "Encoders.h"
Motors_c motors;
Kinematics_c pose;
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

  pose.initialise(0, 0, 0);

  Serial.println("Leader Car Initialized");
}
int change_time = 0;
int start_flag = 1;
int turn_flag = 1;
void loop()
{
  if(start_flag == 1){
    start_time = millis();
    start_flag = 0;
  }
  change_time = millis();
  if(change_time-start_time < 10000){
    motors.setPWM(-15, -15);
    
    // if(pose.theta<0.785){
    //   motors.setPWM(-15,15);
    // }else{
    //   motors.setPWM(-15,-15);
    //   turn_flag = 0;
    // }
    // if(pose.theta>-0.785){             //reverse turning
    //   motors.setPWM(15,-15);
    //   turn_flag = 0;
    // }else{
    //   motors.setPWM(-15,-15);
    // }

  }else if(change_time-start_time < 11000){   // <45 degree  //-15,15
    motors.setPWM(15,-15);
  }else if(change_time-start_time < 20000){
    motors.setPWM(-15,-15);
  }else{motors.setPWM(0,0);}
  Serial.println(pose.theta);
}
