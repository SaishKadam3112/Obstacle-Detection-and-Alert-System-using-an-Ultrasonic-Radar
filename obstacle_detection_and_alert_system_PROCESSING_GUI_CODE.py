import processing.serial.*;
Serial myPort;

float angle, distance;

void setup() 
{
  size(900, 500);
  smooth();

  myPort = new Serial(this, "COM3", 9600);
  myPort.bufferUntil('\n');
}
