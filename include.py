class Point(object):
    
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def draw(self, canvas):
        print "called draw on non-End/Ctrl Point"
        assert(False)

class EndPoint(Point):
    
    def __init__(self, coordinates):
        super(EndPoint, self).__init__(coordinates)
    
    def isEndPoint(self): return True
    
    def isControlPoint(self): return False

    def draw(self, canvas):
        canvas.create_oval(self.x-3, self.y-3, self.x+3, self.y+3, fill="cyan")

class ControlPoint(Point):
    
    def __init__(self, coordinates):
        super(ControlPoint, self).__init__(coordinates)
    
    def isEndPoint(self): return False
    
    def isControlPoint(self): return True

    def draw(self, canvas):
        canvas.create_oval(self.x-3, self.y-3, self.x+3, self.y+3, fill="magenta")

#invariant: Never have more than 4 points
#invariant: first point always a endPoint
#invariant: never more than two controlPoints in a row
class BezierSegment(object):
    
    def __init__(self, points = []):
        assert type(points == list)
        self.points = points # startPoint, [controlPoint1], [controlPoint2], endPoint
        if (self.length() > 4):
            print "initialized a bezSegment of length > 4"
    
    def length(self): return len(self.points)
    
    #returns Falsy value when no action should be taken above
    #returns BezierSegment when this segment is completed
    def addEndPoint(self, point):
        assert (point.isEndPoint())
        if (self.length() > 3):
            print "attempted to add endPoint to full BezierSegment!\n"
            return False
        self.points.append(point)
        if (self.length() == 1):
            return None  #new segment
        else:
            return BezierSegment([point]) #create new Bezier Segment starting at pt
        
    #always returns False because no action required above
    def addControlPoint(self, point):
        assert(point.isControlPoint())
        if (self.length() < 3):
            if (self.length() == 0):
                print "attempted to add controlPoint to segment with 0 points!\n"
                return False
            self.points.append(point)
        else:
            print "attempted to add controlPoint to segment with 3 points!\n"
            return False

    def draw(self, canvas):
        for p in self.points:
            p.draw(canvas)

class BezierCurve(object):
    def __init__(self):
        self.currSegment = BezierSegment()
        #note that the current segment is always at the end of the segmentList
        self.segments = [self.currSegment]
    
    def addEndPoint(self, point):
        assert(point.isEndPoint())
        newSegment = self.currSegment.addEndPoint(point)
        if (newSegment):
            self.currSegment = newSegment
            self.segments.append(self.currSegment)
            

    def addControlPoint(self, point):
        assert(point.isControlPoint())
        self.currSegment.addControlPoint(point)

    def draw(self, canvas):
        for s in self.segments:
            s.draw(canvas)


