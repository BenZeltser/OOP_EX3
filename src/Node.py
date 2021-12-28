import random

import null as null

class node:

    def __init__(self,key,geoLocation):
        self.key = key
        '''Init neighbors'''
        self.ancestors=0
        self.children=0

        if (geoLocation == null):
            '''place x,y in the field of existing range'''
            x=random.uniform(35,36)
            y=random.uniform(32,33)
            '''Z is always 0 hence we are working in a 2D Plane'''
            geoLocation = (x,y,0)
            '''Once finished Initialization we will attribute it'''
            self.geoLocation = geoLocation





    def __str__(self):
        return ('Key: '+str(self.key)+'\n'+'Geolocation'+str(self.geoLocation.x)+','+str(self.geoLocation.y))

