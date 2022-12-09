#define USE_ARDUINO_INTERRUPTS true   
#include <PulseSensorPlayground.h>      

int sensorPin = A1;
const int PulseWire = 0;  
const int LED13 = 13;        
int Threshold = 550;          
                               
PulseSensorPlayground pulseSensor; 

void setup() {   
  Serial.begin(9600);   
  pulseSensor.begin();
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);    
  pulseSensor.setThreshold(Threshold);  
}
void loop() {
  int myBPM = pulseSensor.getBeatsPerMinute();
  int reading = analogRead(sensorPin);
  float voltage = reading * 3.3;
  voltage /= 1024.0;
  voltage *= 0.5;
  int temp = (voltage - 0.5) * 100; 
  Serial.print(myBPM);
  Serial.print(",");
  Serial.println(temp);                     
  delay(1000);                   
 }
