import pylab
import math
import numpy as np

#pylab.plot([1,2,3,4,5,6,7], [2,3,9,16,25,36,49])
#pylab.show()

#def plotSquares(maxNum=20):
#    xlist, ylist = [], []
#    for x in range (1, maxNum+1):
#        xlist.append(x)
#        ylist.append(x*x)
#    pylab.plot(xlist, ylist)
#    pylab.show()

#plotSquares()

def my_plot(maxNum=4):
    pylab.title("Sine and Cosine at various factors of X")
    sin_collection, cos_collection = [], []
    xlist = np.arange(0, 4*np.pi, 0.1)
    for i in np.arange(-1, 1, 0.2):
        sinlist, coslist = [], []
        for x in xlist:
            sinlist.append(np.sin(x*i))
            coslist.append(np.cos(x*i))
        sin_collection.append(sinlist)
        cos_collection.append(coslist)
    for sin in sin_collection:
        pylab.plot(xlist, sin)
    for cos in cos_collection:
        pylab.plot(xlist, cos)
    pylab.show()
        
#my_plot()
        