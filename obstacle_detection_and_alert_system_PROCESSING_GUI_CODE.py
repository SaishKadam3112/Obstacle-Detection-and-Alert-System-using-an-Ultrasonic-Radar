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

void drawRadar() 
{
  stroke(0, 255, 0);
  noFill();
  
  // Radar circles
  arc(width/2, height, 800, 800, PI, TWO_PI);
  arc(width/2, height, 600, 600, PI, TWO_PI);
  arc(width/2, height, 400, 400, PI, TWO_PI);
  arc(width/2, height, 200, 200, PI, TWO_PI);
  
  // Angle lines
  for (int i = 0; i <= 180; i += 30)
 {
    float x = width/2 + 400 * cos(radians(i));
    float y = height - 400 * sin(radians(i));
    line(width/2, height, x, y);
  }
}

void drawSweepLine(float a) 
{
  stroke(0, 255, 0);
  strokeWeight(2);
  float x = width/2 + 400 * cos(radians(a));
  float y = height - 400 * sin(radians(a));
  line(width/2, height, x, y);
 }


