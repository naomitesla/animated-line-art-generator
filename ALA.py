import sys
import colorama
from bar import Bar


class color:
    red = '\033[31m'
    green = '\033[92m'
    pink = '\033[95m'


colorama.init(wrap=False)
stream = colorama.AnsiToWin32(sys.stderr).stream

start = color.red + "\n" + "╒" + "═"*50 + "╕" + color.green
end = color.red + "╘" + "═"*50 + "╛" + "\n"
input_str = lambda input: f"\033[92m   {input}: \033[95m"
status = 1


def entry():
    print(start)
    try:
        bar = Bar(int(input(input_str('Width (px)'))),
                [input(input_str('Background color(RGB/Hex)')),
                input(input_str('Secondary color(RGB/Hex)'))],
                input(input_str('Passing line width (px)')),
                input(input_str('Filename without extension')))
        Bar.create(bar)
        status = 0
    except KeyboardInterrupt:
        print(color.red + "I DONT CARE! D:<" + color.pink +
            "\n"*2 + "\t" + "Goodbye :p" + '\n')
        exit(0)
    except ValueError:
        print(color.red + "\n"*2 + "\t" + "Invalid input! D:" + '\n')
    except ZeroDivisionError:
        print(color.red + "\n"*2 + "\t" + "Percentage can't be 100 silly! :O" + '\n')
    print(end)
    if not status:
        print(color.pink + "  Your GIF has been made! Have fun! c:")

entry()