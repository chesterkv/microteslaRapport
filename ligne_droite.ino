#include <math.h>
//initialisation


int get_dist(int trig, int echo) {
  float start fin parcours;
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  start = millis();
  while (digitalRead(echo) == LOW) {
    fin = millis();
  }
  parcours = fin - start;
  dist = 0.034*parcours;
  return dist;
}

void ordre_vitesse(dd) {
long int vitesse;
{
  if (dd<50)
  {
     vitesse=2000;
  }
  else
  {
    vitesse=floor(2135+(d-50)*65/350);
  }
}
}

void tourner(float ecart) {
  //ecart correspond à gauche-droite
  long int signal;
  if (ecart < -20.) {
    signal = 1000;
  }
  else if (ecart > 20.0) {
    signal = 1400
  }
  else {
    signal = 1000 + (floor(ecart)+20)*10;
  }
}



