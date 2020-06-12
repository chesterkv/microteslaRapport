import numpy as np

class car:
    def __init__(self, position=(0,0), direction=0, view_distance=200, speed=1):
        self.pos=position
        self.dir=direction # angle en rad dans le repère de la map
        self.visu=view_distance
        self.orientation='R'
        self.speed=speed
    
    def orientate(self):
        angle=self.dir%(2*np.pi)
        if angle >= np.pi/4 and angle < 3*np.pi/4:
            self.orientation='U'
        elif angle >= 3*np.pi/4 and angle < 5*np.pi/4 :
            self.orientation='L'
        elif angle >= 5*np.pi/4 and angle < 7*np.pi/4 :
            self.orientation='D'
        else:
            self.orientation='R'

    def vect_prod(self,V1,V2):
        return V1[0]*V2[1]-V1[1]*V2[0]

    def inter_seg(self,angle,segment):

        A1=self.pos; B1=(self.pos[0] + self.visu*np.cos(angle), self.pos[1]+self.visu*np.sin(angle))
        A2=segment.pt1; B2=segment.pt2

        vect_A1B1=(np.cos(angle), np.sin(angle))
        vect_A2B2=(A2[0]-B2[0], A2[1]-B2[1]); vect_A1B2=(A1[0]-B2[0], A1[1]-B2[1]); vect_A1A2=(A1[0]-A2[0], A1[1]-A2[1]); vect_A2B1=(A2[0]-B1[0], A2[1]-B1[1]) ; vect_A2A1=(A2[0]-A1[0], A2[1]-A1[1])
        
        if self.vect_prod(vect_A1B1,vect_A2B2)==0 or self.vect_prod(vect_A1B1,vect_A1B2)*self.vect_prod(vect_A1B1,vect_A1A2)>0 or self.vect_prod(vect_A2B2,vect_A2B1)*self.vect_prod(vect_A2B2,vect_A2A1)>0:
            return self.visu
        
        return (vect_A2B2[1]*(A1[0]-A2[0])-vect_A2B2[0]*(A1[1]-A2[1]))/self.vect_prod(vect_A2B2,vect_A1B1)

    def view(self, angle, segments):
        dist=self.visu
        for segment in segments.values():
            dist=min(dist, self.inter_seg(self.dir+angle,segment))
        return dist
        
    def move(self):
        (move_x,move_y)=self.pos
        move_x+= self.speed*np.cos(self.dir)
        move_y+= self.speed*np.sin(self.dir)
        self.pos=(move_x,move_y)
    
    def turn_IA5(self, segments):
        r,l=self.view(-np.pi/4, segments),self.view(np.pi/4, segments)
        right=r>l
        vision=self.view(0,segments)
        if vision<10:
            if right :
                self.dir-= (np.pi/8)*10/vision
            else :
                self.dir+= (np.pi/8)*10/vision
        else:
            if min(r,l)<5:
                if right:
                        self.dir-= np.pi/16
                else :
                        self.dir+= np.pi/16
        self.move()

    def turn_IA7(self, segments):
        r=np.average([self.view(i,segments) for i in np.linspace(-3*np.pi/8,-np.pi/8,10)])
        l=np.average([self.view(i,segments) for i in np.linspace(3*np.pi/8,np.pi/8,10)])
        right=r>l
        vision=self.view(0,segments)
        if vision<10:
            if right :
                self.dir-= (np.pi/8)*10/vision
            else :
                self.dir+= (np.pi/8)*10/vision
        else:
            if min(r,l)<5:
                if right:
                        self.dir-= np.pi/16
                else :
                        self.dir+= np.pi/16
        self.move()