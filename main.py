from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    font_list = figlet.getFonts()
    if len(sys.argv) == 1:
        f = font_list[random.randint(0, len(font_list))]
        figlet.setFont(font=f)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in font_list:
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


    string = input("Input: ")
    print(figlet.renderText(string))
    k=input("press close to exit") 


if __name__ == "__main__":
    main()
