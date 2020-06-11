//l'objectif est ici de contrôler simultanément le moteur et le servomoteur
//en donnant des ordres arbitraires
//on a trouvé empiriquement les ordres à mettre en entrée
//moteur : 2000-2135 (arrêt-pleine puissance)
//servomoteur : 1000-1200-1400 (complètement à gauche - milieu - complètement à droite)

#include <Servo.h>
#include <math.h>

void ordre_vitesse(dd)
long int vitesse
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
