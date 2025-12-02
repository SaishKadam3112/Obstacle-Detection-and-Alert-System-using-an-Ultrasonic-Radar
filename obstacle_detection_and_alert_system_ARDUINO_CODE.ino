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

long getDistance() 
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  long distance = (duration * 0.034) / 2;
  return distance;
}

void loop() {

  // Sweep 0 to 180 degrees
  for (int pos = 0; pos <= 180; pos++) {
   servo.write(pos);
   delay(20);
   long distance = getDistance();

   Serial.print(pos);
   Serial.print(",");
   Serial.println(distance);
  }

  // Sweep 180 back to 0 degrees
  for (int pos = 180; pos >= 0; pos--) {
    servo.write(pos);
    delay(20);
    long distance = getDistance();
