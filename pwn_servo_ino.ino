#include <Servo.h>

int c=0;
Servo moteur;
Servo servo;

void setup()
{
  moteur.attach(9);
  servo.attach(11);
}

void loop()
{
  if (c==0) {
  servo.writeMicroseconds(1400);
  moteur.writeMicroseconds(2135);
  delay(600);
  servo.writeMicroseconds(1000);
  moteur.writeMicroseconds(2135);
  delay(600);
  servo.writeMicroseconds(1200);
  moteur.writeMicroseconds(2000);
  c=1;}
  
}
