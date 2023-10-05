import re
from create_bar import create_bar


class Bar:
    def __init__(self, pixels: int, intersection_width: float, unsanitized_colors: list, speed: int, filename: str):
        assert pixels > 0, 'Supplied px for width, is not > zero! D:'
        assert speed > 0, 'Supplied input for speed, is not > zero! D:'

        self.pixels = int(pixels)
        self.intersection = abs(int(intersection_width))
        self.unsanitized_colors = unsanitized_colors
        self.speed = int(speed)
        self.filename = str(filename.replace('.gif', '')).strip() + '.gif'
        self.colors = []

    def __repr__(self):
        return f"class: {self.__class__.__name__}, 'A {self.pixels}px bar with the colors: {self.unsanitized_colors}'"

    def sanitize_colors_hex(self, hex):
        sanitized = []
        for h in hex:
            sanitized.append([int(h.strip().lstrip('#')[i:i+2], 16)
                             for i in (0, 2, 4)])

        sanitized = [sanitized[0], [0, 0, 0], sanitized[1]]
        return sanitized

    def sanitize_colors_rgb(self, rgb):
        sanitized = []
        rgb_pattern = re.compile(r'[^0-9,]', re.I)
        for r in rgb:
            r = re.sub(rgb_pattern, '', r).strip()
            sanitized.append(r.split(','))

        sanitized = [sanitized[0], [0, 0, 0], sanitized[1]]
        return sanitized

    def sanitize_colors(self, unsanitized):
        try:
            if any(c.isalpha() for c in unsanitized[0]+unsanitized[1]):
                self.colors = self.sanitize_colors_hex(unsanitized)
            else:
                self.colors = self.sanitize_colors_rgb(unsanitized)
        except:
            print('\n'*2 + '\t' + 'Invalid color input! :o')

    def create(self):
        self.sanitize_colors(self.unsanitized_colors)
        create_bar(self.pixels, self.colors, self.intersection, self.filename)
