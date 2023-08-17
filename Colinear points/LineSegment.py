from Point import Point
class LineSegment:
    def __init__(self, p:Point, q:Point) -> None:
        self.p = p
        self.q = q
    
    # draws this line segment
    def draw(self):
        self.p.drawTo(self.q)

