from Tkinter import *
from include import *

def mouseLeftPressed(event):
    coords = (event.x, event.y)
    newPoint = EndPoint(coords)
    if (c.data.currentCurve != None):
        c.data.currentCurve.addEndPoint(newPoint)
    else:
        print "c.data.currentCurve was None in mouseLeftPressed"
    redrawAll()

def mouseRightPressed(event):
    coords = (event.x, event.y)
    newPoint = ControlPoint(coords)
    if (c.data.currentCurve != None):
        c.data.currentCurve.addControlPoint(newPoint)
    else:
        print "c.data.currentCurve was None in mouseRightPressed"
    redrawAll()

def keyPressed(event):
    if (event.char == "i" or event.char == "c"):
        init()
    redrawAll()

def doTimerFired():
    redrawAll()

def timerFired():
    delay = 50 # milliseconds
    doTimerFired()
    c.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    c.delete(ALL) #TODO: Update to Delta Graphics
    # draw the circles
    for curve in c.data.curveList:
        curve.draw(c)
def init():
    c.data.currentCurve = None
    c.data.currentCurve = BezierCurve()
    c.data.curveList = []
    c.data.curveList = [c.data.currentCurve]
    print len(c.data.curveList)
    for curve in c.data.curveList:
        for segment in curve.segments:
            print "    %d" % segment.length()

def run():
    # create the root and the c
    global c #canvas
    root = Tk()
    cWidth = 300
    cHeight = 200
    c = Canvas(root, width=cWidth, height=cHeight)
    c.pack()
    # Set up c data and call init
    class Struct: pass
    c.data = Struct()
    c.data.cWidth = cWidth
    c.data.cHeight = cHeight
    init()
    # set up events
    root.bind("<Button-1>", mouseLeftPressed)
    root.bind("<Button-3>", mouseRightPressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
