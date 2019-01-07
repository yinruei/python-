import math, copy
class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

def distance(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    dx = p1.x-p2.x
    dy = p1.y-p2.y
    dist = math.sqrt(dx**2 + dy**2)
    # print('%g' % dist)
    # print(dist)
    return dist

class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner.
    """

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width  += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    """Move the Rectangle by modifying its corner object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_new(rect, dx, dy):
    """Move the Rectangle and return a new Rectangle object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).

    returns: new Rectangle
    """
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)

    return new


def main():
    blank = Point()
    origin = Point()
    origin.x = 0
    origin.y = 0
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)
    # distance(origin, blank)
    print('兩 點 的 距 離 : ', distance(origin, blank))


    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    # center = find_center(box)
    # print(print_point(center))

    move_rectangle(box, 50, 100)
    print(box.corner.x)
    print(box.corner.y)

    new = move_rectangle_new(box, 50, 100)
    print(new.corner.x)
    print(new.corner.y)

    print(isinstance(blank, Point))#檢查一個物件是否為某個類別的實體
    print(hasattr(blank,'x'))#如果你不確定一個物件是否具有某個特定的實體，可以用hasattr查看

if __name__ == "__main__":
    main()