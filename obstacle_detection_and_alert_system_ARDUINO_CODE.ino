#include <Servo.h>
int trigPin = 9;
int echoPin = 10;

void setup()
{
  Serial.begin(9600);
  servo.attach(6);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

long getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
