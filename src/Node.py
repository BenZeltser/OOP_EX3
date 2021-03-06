import random
import time
class Node:

    def __init__(self,key,geoLocation):
        self.key = key
        '''Init neighbors'''
        if (geoLocation == None):
            '''place x,y in the field of existing range'''
            x=random.uniform(35,36)
            y=random.uniform(32,33)
            '''Z is always 0 hence we are working in a 2D Plane'''
            geoLocation = (x,y,0)
            '''Once finished Initialization we will attribute it'''
            self.geoLocation = geoLocation
        else:
            self.geolocation=geoLocation





    def __str__(self):
        return ('Key: '+str(self.key)+'\n'+'Geolocation'+str(self.geoLocation.x)+','+str(self.geoLocation.y))


    def getX(self):
        return self.geoLocation[0]

    def getY(self):
        return self.geoLocation[1]

    def getZ(self):
        return 0