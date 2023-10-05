from colorama import Style
from bar import Bar


class colors:
    red = '\u001b[38;5;161m'
    pink = '\u001b[38;5;206m'
    green = '\u001b[38;5;82m'


reset = Style.RESET_ALL
start = colors.red + '\n' + '╒' + '═'*50 + '╕' + colors.green + reset
end = colors.red + '╘' + '═'*50 + '╛' + '\n' + reset
def input_pretty(input): return f'{colors.green}   {input}: {colors.pink}'


def entry():
    status = 1
    padding = '\n' * 2 + '\t'
    print(start)
    try:
        bar = Bar(int(input(input_pretty('Width (px)'))),
                  int(input(input_pretty('Passing line width (px)'))),
                  [input(input_pretty('Background color (RGB/Hex)')),
                   input(input_pretty('Secondary color (RGB/Hex)'))],
                  int(input(input_pretty('Speed (1-100)'))),
                  input(input_pretty('Filename')))
        Bar.create(bar)
        status = 0
    except KeyboardInterrupt:
        print(f''' {colors.red} I DONT CARE! D:< \n{end}
                   {colors.pink}{padding} Goodbye :p {reset} \n
             ''')
        exit(0)
    except ValueError:
        print(f'{padding}Invalid input! D: \n')
    except ZeroDivisionError:
        print(f'{colors.red}{padding}Percentage can\'t be 100 silly! :O \n')

    print(end)
    if not status:
        print(f'{colors.pink}  Your GIF has been made! Have fun! c: {reset}')


if __name__ == "__main__":
    entry()
