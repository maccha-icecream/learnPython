import abc
import sys


# 色空間のインターフェイス
class IColor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_rgb(self) -> 'ColorRGB':
        raise NotImplementedError()
    @abc.abstractmethod
    def to_hsl(self) -> 'ColorHSL':
        raise NotImplementedError()

# HSL色空間
class ColorHSL(IColor):
    def __init__(self, hue:int, saturation:int, lightness: int):
        self.hue = hue
        self.saturation = saturation
        self.lightness = lightness

    def to_hsl(self) -> 'ColorHSL':
        return self

    def __str__(self):
        return f'hsl({self.hue}, {self.saturation}%, {self.lightness}%)'

    def to_rgb(self) -> 'ColorRGB':
        rgb_from_hsl = ColorRGB(0, 0, 0)

        if (self.hue == 360):
            self.hue = 0

        if self.lightness <= 49:
            max_in_hsl = 2.55 * (self.lightness + self.lightness * (self.saturation / 100))
            min_in_hsl = 2.55 * (self.lightness - self.lightness * (self.saturation / 100))
        else:
            max_in_hsl = 2.55 * (self.lightness + (100 - self.lightness) * (self.saturation / 100))
            min_in_hsl = 2.55 * (self.lightness - (100 - self.lightness) * (self.saturation / 100))

        if (self.hue < 60):
            rgb_from_hsl.red = max_in_hsl
            rgb_from_hsl.green = min_in_hsl + (max_in_hsl - min_in_hsl) * (self.hue / 60)
            rgb_from_hsl.blue = min_in_hsl
        elif (60 <= self.hue < 120):
            rgb_from_hsl.red = min_in_hsl + (max_in_hsl - min_in_hsl) * ((120 - self.hue) / 60)
            rgb_from_hsl.green = max_in_hsl
            rgb_from_hsl.blue = min_in_hsl
        elif (120 <= self.hue < 180):
            rgb_from_hsl.red = min_in_hsl
            rgb_from_hsl.green = max_in_hsl
            rgb_from_hsl.blue = min_in_hsl + (max_in_hsl - min_in_hsl) * ((self.hue - 120) / 60)
        elif (180 <= self.hue < 240):
            rgb_from_hsl.red = min_in_hsl
            rgb_from_hsl.green = min_in_hsl + (max_in_hsl - min_in_hsl) * ((240 - self.hue) / 60)
            rgb_from_hsl.blue = max_in_hsl
        elif (240 <= self.hue < 300):
            rgb_from_hsl.red = min_in_hsl + (max_in_hsl - min_in_hsl) * ((self.hue - 240) / 60)
            rgb_from_hsl.green = min_in_hsl
            rgb_from_hsl.blue = max_in_hsl
        elif (300 <= self.hue < 360):
            rgb_from_hsl.red = max_in_hsl
            rgb_from_hsl.green = min_in_hsl
            rgb_from_hsl.blue = min_in_hsl + (max_in_hsl - min_in_hsl) * ((360 - self.hue) / 60)

        rgb_from_hsl.red = round(rgb_from_hsl.red)
        rgb_from_hsl.green = round(rgb_from_hsl.green)
        rgb_from_hsl.blue = round(rgb_from_hsl.blue)

        return rgb_from_hsl


# RGB色空間
class ColorRGB(IColor):
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'rgb({self.red}, {self.green}, {self.blue})'

    def to_rgb(self) -> 'ColorRGB':
        return self

    def to_hsl(self) -> 'ColorHSL':
        max_in_rgb = max(self.red, self.green, self.blue)
        min_in_rgb = min(self.red, self.green, self.blue)
        hsl = {'h': 0, 's': 0, 'l': (max_in_rgb + min_in_rgb) / 2}

        if (max_in_rgb != min_in_rgb):
            if (max_in_rgb == self.red):
                hsl['h'] = 60 * (self.green - self.blue) / (max_in_rgb - min_in_rgb)
            if (max_in_rgb == self.green):
                hsl['h'] = 60 * (self.blue - self.red) / (max_in_rgb - min_in_rgb) + 120
            if (max_in_rgb == self.blue):
                hsl['h'] = 60 * (self.red - self.green) / (max_in_rgb - min_in_rgb) + 240

        if (hsl['l'] <= 127):
            hsl['s'] = (max_in_rgb - min_in_rgb) / (max_in_rgb + min_in_rgb)
        else:
            hsl['s'] = (max_in_rgb - min_in_rgb) / (510 - max_in_rgb - min_in_rgb)

        if (hsl['h'] < 0):
            hsl['h'] += 360

        hsl['h'] = round(hsl['h'])
        hsl['s'] = round(hsl['s'] * 100)
        hsl['l'] = round(hsl['l'] / 255 * 100)

        return ColorHSL(hsl['h'], hsl['s'], hsl['l'])


if __name__ == "__main__":
    rgb = ColorRGB(105, 207, 152)
    print(rgb)
    hsl = ColorHSL(148, 52, 61)
    print(hsl)
    rgb = hsl.to_rgb()
    print(rgb)