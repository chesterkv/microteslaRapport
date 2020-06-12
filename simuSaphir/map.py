import matplotlib.pyplot as plt 
import numpy as np

class map:
    def __init__(self,taille_x=30,taille_y=20,largeur_route=10):
        self.taille_x=taille_x
        self.taille_y=taille_y
        self.largeur_route=largeur_route
        self.segments={}
    
    class segment :
        def __init__(self,point1=(0,0), point2=(0,0)):
            self.pt1=point1 
            self.pt2=point2 
        def trace(self):
            plt.plot([self.pt1[0],self.pt2[0]],[self.pt1[1],self.pt2[1]],color='r')

    def create_map(self):
        L=self.taille_x; l=self.taille_y; m=self.largeur_route
        exte=[[0,0],[L,0],[L,-l],[L+3*m,-l],[L+3*m,L+2*m-l],[L+m,L+4*m-l],[L,L+4*m-l],[L,L+3*m-l],[L-m,L+3*m-l],[L-m,L+3*m-l-m/5],[L-2*m,L+3*m-l-m/5],[L-2*m,L+3*m-l],[-m,L+3*m-l],[-m,0]]
        inte=[[m,m],[m+L,m],[m+L,m-l],[2*m+L,m-l],[2*m+L,L+m-l],[m+L,L+2*m-l],[-m+L,L+2*m-l],[-m+L,L+2*m-l-m/5],[-2*m+L,L+2*m-l-m/5],[-2*m+L,L+2*m-l],[0,L+2*m-l],[0,m]]
        obst=[[0.8*m+L,L+2.6*m-l],[0.8*m+L,L+3*m-l],[1.2*m+L,L+3*m-l],[1.2*m+L,L+2.6*m-l]]

        for i in range(len(exte)):
            self.segments[2*i] = self.segment(point1=exte[i-1],point2=exte[i])
        for i in range(len(inte)):
            self.segments[2*i+1] = self.segment(point1=inte[i-1],point2=inte[i])
        for i in range(len(obst)):
            self.segments["obs",i] = self.segment(point1=obst[i-1],point2=obst[i])
        
    def trace_map(self):
        for i in self.segments.values():
            i.trace()   
        



    
