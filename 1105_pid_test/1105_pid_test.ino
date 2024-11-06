#include <Wire.h>
#include <LSM6.h>
#include "Encoders.h"
#include "Kinematics.h"

LSM6 imu;
Kinematics_c pose;

#define WHEEL_DIAMETER 0.08    // 轮子直径为 0.1 米（根据实际情况调整）
#define PPR_VALUE 358.3        // 编码器每转的脉冲数（根据实际情况调整）
#define INTERVAL 100           // 速度计算时间间隔（毫秒）

// 定义电机引脚
#define L_PWM 10 // This is correct.
#define L_DIR 16 // This is the wrong pin! 
#define R_PWM 9 // This is the wrong pin! 
#define R_DIR 15 // This is the wrong pin! 

// PID 参数
float Kp_L = 0.15;  // 比例增益
float Ki_L = 0.3;  // 积分增益
float Kd_L = 0.1;  // 微分增益

float Kp_R = 0.15;  // 比例增益
float Ki_R = 0.3;  // 积分增益
float Kd_R = 0.1;  // 微分增益

long last_count_e0 = 0;        // 上一次的编码器计数
long last_count_e1 = 0;        // 上一次的编码器计数
unsigned long lastTime = 0;    // 上一次的时间

double R_speed = 0;           // 编码器0测得的速度
double L_speed = 0;           // 编码器1测得的速度

// PID 变量

float errorSum = 0;
float lastError = 0;
int flag = 1;
float read_parameter = 0;

void pid_L();
void pid_R();
void speed_detect();

void setup() {
  // 设置引脚为输出模式
  pinMode(L_PWM, OUTPUT);
  pinMode(L_DIR, OUTPUT);
  pinMode(R_PWM, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  digitalWrite(L_DIR, LOW);
  digitalWrite(R_DIR, LOW);
  analogWrite(L_PWM, 18);
  analogWrite(R_PWM, 18);


  Serial.begin(9600);
  
  // 初始化编码器
  setupEncoder0();
  setupEncoder1();

  Wire.begin();

}

void loop() {
  pose.update();
  Serial.print("pose_theta:");
  Serial.println(pose.theta);
  speed_detect();
  pid_R(27, R_speed);
  pid_L(25, L_speed);

  // if(pose.theta>0){
  //   pid_R(20, R_speed);
  //   pid_L(21, L_speed);
  // }else if(pose.theta<=0){
  //   pid_R(22, R_speed);
  //   pid_L(20, L_speed);
  // }else{
  //   pid_R(20, R_speed);
  //   pid_L(20, L_speed);
  // }

}
void speed_control(){
  if(read_parameter > 1500){
    pid_L(40, L_speed);
    pid_R(40, R_speed);
  }else if(1500 >= read_parameter > 1000){
    pid_L(30, L_speed);
    pid_R(30, R_speed);
  }else if(1000 >= read_parameter > 800){
    pid_L(25, L_speed);
    pid_R(25, R_speed);
  }else if(800 >= read_parameter > 700){
    pid_L(23, L_speed);
    pid_R(23, R_speed);
  }else if(700 >= read_parameter > 600){
    pid_L(20, L_speed);
    pid_R(20, R_speed);
  }else if(600 >= read_parameter){
    pid_L(16, L_speed);
    pid_R(16, R_speed);
  }
}

void speed_detect(){
  unsigned long currentTime = millis();

  // 每隔 INTERVAL 时间计算一次速度
  if (currentTime - lastTime >= INTERVAL) {
    // 获取当前编码器计数
    long current_count_e0 = count_e0;
    long current_count_e1 = count_e1;

    // 计算脉冲增量
    long delta_count_e0 = current_count_e0 - last_count_e0;
    long delta_count_e1 = current_count_e1 - last_count_e1;

    // 更新上一次的计数
    last_count_e0 = current_count_e0;
    last_count_e1 = current_count_e1;

    // 计算时间间隔（秒）
    double deltaTime = (currentTime - lastTime) / 1000.0;
    lastTime = currentTime;

    // 计算线速度 (m/s)
    double circumference = WHEEL_DIAMETER * 3.14159;   // 轮子的周长
    R_speed = (delta_count_e0 * circumference) / (PPR_VALUE * deltaTime)*100;
    L_speed = (delta_count_e1 * circumference) / (PPR_VALUE * deltaTime)*100;

    // 输出速度
    Serial.print("R_Speed: ");
    Serial.print(R_speed);
    Serial.print(" cm/s | L_Speed: ");
    Serial.print(L_speed);
    Serial.println(" cm/s");
  }

  delay(10);  // 主循环延时，以免过多占用处理器资源
}

void pid_L(float targetSpeed, float currentSpeed){
  // 计算误差

  float error = targetSpeed - currentSpeed;
  
  // PID 控制器公式
  errorSum += error;                             // 积分部分
  float dError = error - lastError;              // 微分部分
  float output = Kp_L * error + Ki_L * errorSum + Kd_L * dError;  // PID 输出

  // 限制输出范围
  output = constrain(output, 0, 255);

  // 将输出设置为 PWM 信号
  analogWrite(L_PWM, output);  // 控制电机1
  
  // 更新当前速度（模拟逐渐达到目标）
  currentSpeed += (targetSpeed - currentSpeed) * 0.1;

  // 存储误差用于下次计算微分
  lastError = error;

  // 延迟以观察效果
  delay(100);
}

void pid_R(float targetSpeed, float currentSpeed){
  // 计算误差

  float error = targetSpeed - currentSpeed;
  
  // PID 控制器公式
  errorSum += error;                             // 积分部分
  float dError = error - lastError;              // 微分部分
  float output = Kp_R * error + Ki_R * errorSum + Kd_R * dError;  // PID 输出

  // 限制输出范围
  output = constrain(output, 0, 255);

  // 将输出设置为 PWM 信号
  analogWrite(R_PWM, output);  // 控制电机1
  
  // 更新当前速度（模拟逐渐达到目标）
  currentSpeed += (targetSpeed - currentSpeed) * 0.1;

  // 存储误差用于下次计算微分
  lastError = error;

  // 延迟以观察效果
  delay(100);
}