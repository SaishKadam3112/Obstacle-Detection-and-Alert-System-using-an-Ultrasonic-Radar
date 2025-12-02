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

void draw() 
{
  background(0);
  drawRadar();
  drawSweepLine(angle);
  drawObject(angle, distance);
}

void serialEvent(Serial myPort) 
{
  String data = myPort.readStringUntil('\n');

 if (data != null)
 {
    data = trim(data);
    String values[] = split(data, ',');
    if (values.length == 2)
    {
      angle = float(values[0]);
      distance = float(values[1]);
    }
  }
}


