//amélioration du code de ligne_droite.ino
//on voit ici une loop qui effectue les commandes en boucle :
//on calcule les distances à droite et à gauche et on en déduit l'ordre de direction qui en découle.

#include <math.h>
#include <Servo.h>
//initialisation
Servo servo;

int get_dist(int trig, int echo)
{
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

void ordre_vitesse(dd) 
{
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

void tourner(float ecart)
{
  //ecart correspond à droite_gauche
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

void setup()
{
  servo.attach(11);
}

void loop()
{
  //ordre servomoteur
  dist_d=get_dist();
  dist_g=get_dist();
  ec=dist_d-dist_g;
  tourner(ec);

  //ordre moteur

  //fin de la boucle
  delay(100);
}
