from dataclasses import dataclass

def simple_match() -> None:
    c = 3

    match c:
        case 1:
            print('One')
        case 2:
            print('Two')
        case 3:
            print('Three')
        case _:
            print('Other')

@dataclass
class Point:
    x: int
    y: int


def where_am_i(point: Point) -> str:
    match point:
        case Point(x = 0, y = 0):
            return 'Origin'
        case Point(x = 0) as p:
            return f'Y={p.y}'
        case Point(y = 0) as p:
            return f'X={p.y}'
        case Point() as p:
            return f'X={p.x}, Y={p.y}'
        case _:
            raise ValueError('Not a point')

@dataclass
class Rectangle:
    width: float
    length: float


@dataclass
class Circle:
    radius: float

def identify_shape(shape: Point | Rectangle | Circle) -> str:
    match shape:
        case Point():
            return  f'This is a Point({shape.x}, {shape.y})'
        case Rectangle():
            return f'This is a Rectangle({shape.width}, {shape.length})'
        case Circle():
            return f'This is a Circle({shape.radius})'
        case _:
            raise ValueError('Unknown Shape')


if __name__ == "__main__":
    point: Point = Point(1, 1)
    rectangle: Rectangle = Rectangle(3, 4)
    circle: Circle = Circle(1)
    unknown: int = 1

    print(identify_shape(point))
    print(identify_shape(rectangle))
    print(identify_shape(circle))
    print(identify_shape(unknown))
