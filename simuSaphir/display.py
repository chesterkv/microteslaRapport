from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation 

def display_init(map): # fonction qui initialise la fenêtre d'affichage 
    global ax           # On définit ax comme une variable globale 
    fig= plt.figure(1) #On force l'affichage sur la 1ère image 
    ax = fig.add_subplot()
    plt.axis('equal') 
    max_bound=max(map.taille_y,map.taille_x)
    ax.set_xbound(lower=0, upper=max_bound+2)  #tailles des axes
    ax.set_ybound(lower=0, upper=max_bound+2)  
    return fig

def display(car,map,i):
    global ax
    plt.figure(1)
    plt.clf() #Pour ne pas superposer les images qui se succèdent
    fig=display_init(map)

    car.orientate()
    arr_lena1 = mpimg.imread('voiture_'+car.orientation+'.png') #charge l'image de la voiture

    imagebox1 = OffsetImage(arr_lena1, zoom=2)        #config de la taille de la voiture
    ab1 = AnnotationBbox(imagebox1, car.pos, frameon=False, box_alignment=(0.5,0.5))     #associer une image à une position 
    ax.add_artist(ab1)  # ajouter l'image à la fenêtre en utilisant la classe artist
    
    map.trace_map()
    '''
    fig.savefig('frame_'+str(i)+'.png') #sert à enregister les frames de la simulation 
    '''
    plt.pause(0.0000000000000000000001)