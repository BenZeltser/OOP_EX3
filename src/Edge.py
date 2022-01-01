class Edge:

    def __init__(self, src,dst,weight):

        self.src=src
        self.dst=dst
        self.weight=weight

    def __str__(self):
        return ('src: '+str(self.src)+'\n'+'dst'+str(self.dst)+'\n'+' weight:'+str(self.weight))

    def getSRC(self):
        return self.src

    def getDST(self):
        return self.dst

    def getWeight(self):
        return self.weight