import colorama
from bar import Bar


class colors:
    red = '\u001b[38;5;161m'
    pink = '\u001b[38;5;206m'
    green = '\u001b[38;5;82m'


reset = colorama.Style.RESET_ALL
start = colors.red + '\n' + '╒' + '═'*50 + '╕' + colors.green + reset
end = colors.red + '╘' + '═'*50 + '╛' + '\n' + reset
def input_str(input): return f'{colors.green}   {input}: {colors.pink}'


def entry():
    status = 1
    padding = '\n' * 2 + '\t'
    print(start)
    try:
        bar = Bar(int(input(input_str('Width (px)'))),
                  [input(input_str('Background color (RGB/Hex)')),
                   input(input_str('Secondary color (RGB/Hex)'))],
                  input(input_str('Passing line width (px)')),
                  input(input_str('Speed')),
                  input(input_str('Filename')))
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
