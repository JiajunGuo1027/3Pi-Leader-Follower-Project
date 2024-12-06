#include "Motors.h"   
#include "Kinematics.h"
#include "Encoders.h"

#define WHEEL_DIAMETER 0.08  
#define PPR_VALUE 358.3   
#define INTERVAL 100   

#define L_PWM 10 
#define L_DIR 16 
#define R_PWM 9
#define R_DIR 15 

const int leftBumpSensorPin = A6;  
const int rightBumpSensorPin = 5;  
const int EMIT_PIN = 11;      

float bumper_max = 0.0;                              //bumper&line max & min
float bumper_min = 1000.0;
float lineL_max = 0.0;
float lineL_min = 1000.0;
float lineM_max = 0.0;
float lineM_min = 1000.0;
float lineR_max = 0.0;
float lineR_min = 1000.0;

const int distanceThreshold = 300;  
const int rightBumpDetected = HIGH; 

int cali_f = 1;                                       //calibration status
//int cali_f = 5;

float Kp_L = 0.15; 
float Ki_L = 0.3; 
float Kd_L = 0.1; 

float Kp_R = 0.15; 
float Ki_R = 0.3; 
float Kd_R = 0.1; 

long last_count_e0 = 0;     
long last_count_e1 = 0;      
unsigned long lastTime = 0;   

double R_speed = 0;      
double L_speed = 0;    

const int numSensors = 4;  
const int maxRecords = 120; 
float sensorData[maxRecords][numSensors];
int currentRecord = 0;


// PID 变量
float errorSum = 0;
float lastError = 0;
int flag = 5;
float read_parameter = 0;

Kinematics_c pose;
Motors_c motors;

unsigned long timestamp = millis(); 
int leftBumpValue;
int rightBumpValue;
int linesensor; 
int time_flag = 0;

void bump_line_detect();
void Calibration_bump_line();
void pid_L();
void pid_R();
void speed_detect();
void speed_control();

void setup() {
  pinMode(L_PWM, OUTPUT);
  pinMode(L_DIR, OUTPUT);
  pinMode(R_PWM, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  pinMode(leftBumpSensorPin, INPUT_PULLUP);
  pinMode(rightBumpSensorPin, INPUT_PULLUP);
  pinMode(A11, INPUT_PULLUP);
  pinMode(A0, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);
  pinMode(A3, INPUT_PULLUP);
  pinMode(A4, INPUT_PULLUP);

  //pinMode(EMIT_PIN, INPUT);                                 // INPUT to avoid disruption
  pinMode(EMIT_PIN, OUTPUT);
  digitalWrite(EMIT_PIN, HIGH);
  pose.initialise(0, 0, 0);
  setupEncoder0();
  setupEncoder1();
  Serial.begin(9600);
}

void loop() {
  unsigned long timestamp = millis();
  leftBumpValue = analogRead(leftBumpSensorPin);
  rightBumpValue = digitalRead(rightBumpSensorPin);
  linesensor = analogRead(A2);                                // CSV format for further evaluation: timestamp,sensor 1,sensor 2,...,sensor n
  
  if(timestamp-time_flag > 100){
    for (int i = 0; i < numSensors; i++) {
      sensorData[currentRecord][i] = readSensor(i); 
    }
    Serial.print("Record ");
    Serial.print(currentRecord);
    Serial.print(": ");
    for (int i = 0; i < numSensors; i++) {
      Serial.print(sensorData[currentRecord][i]);
      Serial.print(" ");
    }
    Serial.println();
    currentRecord++;
    if (currentRecord >= maxRecords) {
      currentRecord = 0;                                      // reset to zero
    }
    printAllSensorData();
    time_flag = millis();
  }else{}

  
  // Serial.print(timestamp);
  // Serial.print(",");
  // Serial.print(bumper_min);
  // Serial.print(",");
  // Serial.print(bumper_max);
  // Serial.print(",");
  // Serial.print(lineL_min);
  // Serial.print(",");
  // Serial.print(lineL_max);
  // Serial.print(",");
  // Serial.print(lineM_min);
  // Serial.print(",");
  // Serial.print(lineM_max);
  // Serial.print(",");
  // Serial.print(lineR_min);
  // Serial.print(",");
  // Serial.println(lineR_max);

  Serial.println(pose.theta);
  Serial.println(pose.x);
  delay(100);
  
  //Serial.println(cali_f);
  if(cali_f == 5){
    //speed_detect();
    //speed_control();
    //speed_control_line();
  }else{
    Calibration_bump_line();
  }
}

void printAllSensorData() {
  Serial.println("All recorded sensor data:");

  for (int record = 0; record < maxRecords; record++) {
    Serial.print("Record ");
    Serial.print(record);
    Serial.print(": ");

    for (int sensor = 0; sensor < numSensors; sensor++) {
      Serial.print(sensorData[record][sensor]);
      Serial.print(" ");
    }

    Serial.println(); 
  }
}

float readSensor(int sensorIndex) {
  if(sensorIndex==0){
    return leftBumpValue;
  }else if(sensorIndex==1){
    return analogRead(A0);
  }else if(sensorIndex==2){
    return analogRead(A2);
  }else if(sensorIndex==3){
    return analogRead(A3);
  }


  // if(sensorIndex==0){
  //   return leftBumpValue;
  // }else if(sensorIndex==1){
  //   return rightBumpValue*200;
  // }else if(sensorIndex==2){
  //   return analogRead(A11);
  // }else if(sensorIndex==3){
  //   return analogRead(A0);
  // }else if(sensorIndex==4){
  //   return analogRead(A2);
  // }else if(sensorIndex==5){
  //   return analogRead(A3);
  // }else if(sensorIndex==6){
  //   return analogRead(A4);
  // }
}

void speed_control(){
  digitalWrite(L_DIR, LOW);
  digitalWrite(R_DIR, LOW);
  if(leftBumpValue < ((bumper_max-bumper_min)*0.05+bumper_min) && rightBumpValue == 0){
    motors.setPWM(0,0);
    //pid_L(0, L_speed);
    //pid_R(0, R_speed);
    Serial.println("INTO SPEED1!");
  }else if(leftBumpValue < ((bumper_max-bumper_min)*0.2+bumper_min)){
    //motors.setPWM(17,17);
    pid_L(17, L_speed);
    pid_R(19, R_speed);
    Serial.println("INTO SPEED2!");
  }else if(leftBumpValue < ((bumper_max-bumper_min)*0.65+bumper_min)){
    // motors.setPWM(19,19);
    pid_L(19, L_speed);
    pid_R(21, R_speed);
    Serial.println("INTO SPEED3!");
  }else if(leftBumpValue < ((bumper_max-bumper_min)*0.9+bumper_min)){
    // motors.setPWM(20,20);
    pid_L(20, L_speed);
    pid_R(25, R_speed);
    Serial.println("INTO SPEED4!");
  }else{
    // motors.setPWM(30,30);
    pid_L(30, L_speed);
    pid_R(45, R_speed);
    Serial.println("INTO SPEED5!");
  }
}

void speed_control_line(){
  digitalWrite(L_DIR, LOW);
  digitalWrite(R_DIR, LOW);
  if(analogRead(A2) < ((bumper_max-bumper_min)*0.2+bumper_min) && rightBumpValue == 0){
    motors.setPWM(0,0);
    pid_L(0, L_speed);
    pid_R(0, R_speed);
    Serial.println("INTO SPEED1!");
  }else if(analogRead(A2) < ((bumper_max-bumper_min)*0.5+bumper_min)){
    //motors.setPWM(17,17);
    if(analogRead(A0)+10<analogRead(A3)){
      pid_L(15, L_speed);
      pid_R(21, R_speed);
    }else if(analogRead(A0) >= analogRead(A3)+10){
      pid_L(19, L_speed);
      pid_R(17, R_speed);
    }else{
      pid_L(17, L_speed);
      pid_R(19, R_speed);
    }
    Serial.println("INTO SPEED2!");
  }else if(analogRead(A2) < ((bumper_max-bumper_min)*0.75+bumper_min)){
    // motors.setPWM(19,19);
    if(analogRead(A0)+10<analogRead(A3)){
      pid_L(15, L_speed);
      pid_R(21, R_speed);
    }else if(analogRead(A0) >= analogRead(A3)+10){
      pid_L(19, L_speed);
      pid_R(17, R_speed);
    }else{
      pid_L(19, L_speed);
      pid_R(21, R_speed);
    }
    Serial.println("INTO SPEED3!");
  }else if(analogRead(A2) < ((bumper_max-bumper_min)*0.9+bumper_min)){
    // motors.setPWM(20,20);
    if(analogRead(A0)+10<analogRead(A3)){
      pid_L(15, L_speed);
      pid_R(21, R_speed);
    }else if(analogRead(A0) >= analogRead(A3)+10){
      pid_L(19, L_speed);
      pid_R(17, R_speed);
    }else{
      pid_L(20, L_speed);
      pid_R(23, R_speed);
    }
    Serial.println("INTO SPEED4!");
  }else{
    // motors.setPWM(30,30);
    if(analogRead(A0)+10<analogRead(A3)){
      pid_L(15, L_speed);
      pid_R(21, R_speed);
    }else if(analogRead(A0) >= analogRead(A3)+10){
      pid_L(19, L_speed);
      pid_R(17, R_speed);
    }else{
      pid_L(30, L_speed);
      pid_R(34, R_speed);
    }
    Serial.println("INTO SPEED5!");
  }
}


void Calibration_bump_line(){
  motors.setPWM(0,0);
  pose.update();
  if(cali_f == 1){
    if(pose.theta < 7){
      motors.setPWM(-18, 18);
    }else{cali_f = 2;}
  }else if(cali_f == 2){
    if(pose.theta > 0){
      motors.setPWM(18, -18);
    }else{cali_f = 3;}
  }else if(cali_f == 3){
    if(pose.x > -60){
      motors.setPWM(-18, -18);
    }else{cali_f = 4;}
  }else if(cali_f == 4){
    if(pose.x < -10){
      motors.setPWM(18, 18);
    }else{cali_f = 5;}
  }
  bump_line_detect();
}

void bump_line_detect(){
  if(leftBumpValue>bumper_max){
    bumper_max = leftBumpValue;
  }else{}
  if(leftBumpValue<bumper_min){
    bumper_min = leftBumpValue;
  }else{}
  if(analogRead(A0)>lineL_max){
    lineL_max = analogRead(A0);
  }else{}
  if(analogRead(A0)<lineL_min){
    lineL_min = analogRead(A0);
  }else{}
  if(analogRead(A2)>lineM_max){
    lineM_max = analogRead(A2);
  }else{}
  if(analogRead(A2)<lineM_min){
    lineM_min = analogRead(A2);
  }else{}
  if(analogRead(A3)>lineR_max){
    lineR_max = analogRead(A3);
  }else{}
  if(analogRead(A3)<lineR_min){
    lineR_min = analogRead(A3);
  }else{}
}

void speed_detect(){
  unsigned long currentTime = millis();
  if (currentTime - lastTime >= INTERVAL) {
    long current_count_e0 = count_e0;
    long current_count_e1 = count_e1;

    long delta_count_e0 = current_count_e0 - last_count_e0;
    long delta_count_e1 = current_count_e1 - last_count_e1;

    last_count_e0 = current_count_e0;
    last_count_e1 = current_count_e1;

    double deltaTime = (currentTime - lastTime) / 1000.0;
    lastTime = currentTime;

    double circumference = WHEEL_DIAMETER * 3.14159; 
    R_speed = (delta_count_e0 * circumference) / (PPR_VALUE * deltaTime)*100;
    L_speed = (delta_count_e1 * circumference) / (PPR_VALUE * deltaTime)*100;

    Serial.print("R_Speed: ");
    Serial.print(R_speed);
    Serial.print(" cm/s | L_Speed: ");
    Serial.print(L_speed);
    Serial.println(" cm/s");
  }

  delay(10); 
}

void pid_L(float targetSpeed, float currentSpeed){

  float error = targetSpeed - currentSpeed;
  
  errorSum += error;                             // Integral
  float dError = error - lastError;              // Differential
  float output = Kp_L * error + Ki_L * errorSum + Kd_L * dError;  // output

  output = constrain(output, 0, 255);

  analogWrite(L_PWM, output); 

  currentSpeed += (targetSpeed - currentSpeed) * 0.1;

  lastError = error;

  delay(10);
  //Serial.println("PID_L SUCCESS!");
}

void pid_R(float targetSpeed, float currentSpeed){

  float error = targetSpeed - currentSpeed;
  
  errorSum += error;          
  float dError = error - lastError;             
  float output = Kp_R * error + Ki_R * errorSum + Kd_R * dError; 

  output = constrain(output, 0, 255);

  analogWrite(R_PWM, output);  

  currentSpeed += (targetSpeed - currentSpeed) * 0.1;

  lastError = error;

  delay(10);
  //Serial.println("PID_R SUCCESS!");
}