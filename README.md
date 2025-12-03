🛰️ OBSTACLE DETECTION and ALERT SYSTEM using an ULTRASONIC RADAR

📌 Project Overview :- 

This project is an Obstacle Detection and Alert System that uses an ultrasonic sensor mounted on a rotating servo motor to scan the surroundings. The data is sent to a Processing GUI, which displays a live radar view. A buzzer gives an alert when an object is detected very close.


🛠️ Components Used :-

Arduino UNO

Ultrasonic Sensor (HC-SR04)

Servo Motor (MG995)

Buzzer

Connecting wires

Processing IDE (for radar GUI)


🔧 Pin Configuration :-

Component      	Pin Connection

Servo Motor	        D6

Ultrasonic Trig    	D9

Ultrasonic Echo   	D10

Buzzer	            D8


🖼 Circuit Diagram :-

<img width="1480" height="697" alt="Project Circuit Diagram" src="https://github.com/user-attachments/assets/145d00ac-35c0-49e4-b775-d2fbbbb24009" />


⚙️ Working Principle :-

The servo motor rotates from 0° to 180° and back.

At each angle, the ultrasonic sensor measures distance to an obstacle.

If the obstacle is too close, the buzzer turns ON.

Arduino sends angle,distance data to the Processing GUI.

Processing displays a live radar with moving sweep line and object dots.


💻 Code Explanation :-

Ultrasonic Sensor :-
Measures how far an obstacle is from the sensor.
Uses the formula:
distance = (duration * 0.034) / 2
Sends accurate distance data to Arduino.

Servo Motor :-
Rotates between 0° → 180° → 0°.
Helps the sensor scan the environment like a real radar.
Angle changes are matched with distance readings.

Buzzer Alert :-
Turns ON when an obstacle is detected very close.
Helps give a quick warning to the user.

Serial Communication :-
Arduino sends live data to Processing in the format:
angle,distance
Processing reads these values and updates the display.

Processing GUI (Radar Display) :-
Shows a green semicircle radar on the screen.
Displays a moving sweep line based on servo angle.
Draws red dots where obstacles are detected.
Filters out objects that are too far (noise removal).


🧪 Output Features :-

Real-time radar scanning

Visual obstacle display

Buzzer alert for close objects

Smooth GUI animation


🚀 How to Run :-

Upload the Arduino code to the Arduino UNO.

Open the Processing code in Processing IDE.

Select the correct COM port in the code (example: "COM3").

Run the Processing sketch.

Watch the radar detect obstacles in real-time!


📷 Screenshots / Output :-

<img width="1280" height="991" alt="image" src="https://github.com/user-attachments/assets/7942c7e5-7017-4910-b679-19c7a72b89d9" />

<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/c9d06808-90c0-4aa8-8068-4b9fc3a39cd6" />

<img width="1175" height="1280" alt="image" src="https://github.com/user-attachments/assets/98b3a820-0f82-43fd-832a-dbaba45b272a" />

<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/b780a9e1-5e48-416f-9001-0a9b4ca01b21" />



