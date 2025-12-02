#include <Servo.h>
int trigPin = 9;
int echoPin = 10;

void setup() {
  Serial.begin(9600);
  servo.attach(6);
