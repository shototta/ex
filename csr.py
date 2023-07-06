from typing import Tuple


class Rectangle:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def calculate_area(self) -> float:
        return self.a * self.b

    def params(self) -> tuple[float, float]:
        return self.a, self.b

    def Per(self) -> float:
        return self.a * 2 + self.b * 2

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Square(Rectangle):
    def calculate_area(self) -> float:
        return self.a * self.a

    def params(self) -> tuple[float, float]:
        return self.a, self.a

    def Per(self) -> float:
        return self.a * 4


class Circle:
    def __init__(self, r: float) -> None:
        self.r = r

    def calculate_area(self) -> float:
        return self.r * 3.14 * self.r * 3.14

    def Per(self) -> float:
        return self.r * 2 * 3.14

    def params(self) -> float:
        return self.r

    def __repr__(self):
        return f'{self.__class__.__name__}'


def result(shapes: list[Rectangle]):
    for shape in shapes:
        print(shape)
        print(shape.params())
        print(shape.Per())
        print(shape.calculate_area())


def main():
    circle = Circle(5)
    rectangle = Rectangle(2, 3)
    square = Square(2, 2)

    result([circle, rectangle, square])


if __name__ == '__main__':
    main()
