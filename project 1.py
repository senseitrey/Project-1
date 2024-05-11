from gui import *


def main():

    window = Tk()
    window.title('Ballot')
    window.geometry('250x250')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
