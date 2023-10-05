import re
from create_bar import create_bar


class Bar:
    def __init__(self, pixels: int, unsanitized_colors: list, intersection_width: float, speed: int, filename: str):
        assert pixels > 0, f'Supplied px for width, is not > zero! D:'

        # size_dict = {'large': 1, 'medium': 2, 'smaller':6, 'smallest':98}
        # self.intersection = pixels//intersection_width

        self.pixels = int(pixels)
        self.unsanitized_colors = unsanitized_colors
        self.intersection = abs(int(intersection_width))
        self.filename = str(filename).strip() + '.gif'
        self.colors = []

    def __repr__(self, bar):
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
