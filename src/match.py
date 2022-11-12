from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def where_am_i(point: Point) -> str:
    match point:
        case Point(x=0, y=0):
            return 'Origin'
        case Point(x=0) as p:
            return f'Y={p.y}'
        case Point(y=0) as p:
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
            return f'This is a Point({shape.x}, {shape.y})'
        case Rectangle():
            return f'This is a Rectangle({shape.width}, {shape.length})'
        case Circle():
            return f'This is a Circle({shape.radius})'
        case _:
            raise ValueError('Unknown Shape')


def macth_dict(resonse: dict) -> None:
    match resonse:
        case {'status': 200, 'north lat': x}:
            print(f'北緯{x}度')
        case {'status': 200, 'south lat': x}:
            print(f'南緯{x}度')
        case _:
            raise ValueError('Unknown Response')


def macth_cood(cood_list: list) -> None:
    match cood_list:
        case [0]:
            print('1次元の原点です.')
        case [x]:
            print(f'1次元の座標（{x}）です.')
        case [0, 0]:
            print('2次元の原点です.')
        case [x, y]:
            print(f'2次元の座標（{x}, {y}）です.')
        case _:
            raise ValueError('Unknown Point.')


def match_greater_than_zero_cood(cood_list: list) -> None:
    match cood_list:
        case [x] if x >= 0:
            print(f'1次元の座標（{x}）です.')
        case [x, y] if x >= 0 and y >= 0:
            print(f'2次元の座標（{x}）です.')
        case _:
            raise ValueError('Unknown Point.')


if __name__ == "__main__":
    point: Point = Point(1, 1)
    rectangle: Rectangle = Rectangle(3, 4)
    circle: Circle = Circle(1)
    unknown: int = 1

    print(identify_shape(point))
    print(identify_shape(rectangle))
    print(identify_shape(circle))
    # print(identify_shape(unknown))

    res_dict = {'status': 200, 'south lat': 9.02}
    macth_dict(res_dict)

    match_greater_than_zero_cood([-1])
    match_greater_than_zero_cood([0])
