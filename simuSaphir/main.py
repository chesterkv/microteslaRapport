from car import *
from display import *
from map import *

mmp= map(taille_x=30,taille_y=20,largeur_route=10)
mmp.create_map()
voiture=car(position=(2,2),direction=0,speed=3,view_distance=200) # la variable speed définit les intervalles de temps entre deux prises de décision

nb_frames=180

display_init(mmp)
for i in range(nb_frames):
    display(voiture,mmp,i)
    voiture.turn_IA7(segments=mmp.segments)