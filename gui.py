from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_title = Label(self.frame_one, text='VOTE MENU')

        self.label_title.pack(side='top')
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.label_vote = Label(self.frame_two, text='V: Vote')
        self.label_quit = Label(self.frame_two, text='Q: Quit')
        self.label_vote.pack(side='top')
        self.label_quit.pack(side='top')
        self.frame_two.pack()

        self.frame_three = Frame(self.window)
        self.input = Entry(self.frame_three, width=20)
        self.button_save = Button(self.frame_three, text='SAVE', command=self.submit)
        self.input.pack(side='left')
        self.button_save.pack(side='left')
        self.frame_three.pack()

    def submit(self):
        if self.input.get() == 'V':
            self.label_title.config(text='CANDIDATE MENU')
            self.label_vote.config(text='1: John')
            self.label_quit.config(text='2: Jane')
            self.input.delete(0, END)
        elif self.input.get() == 'v':
            self.label_title.config(text='CANDIDATE MENU')
            self.label_vote.config(text='1: John')
            self.label_quit.config(text='2: Jane')
            self.input.delete(0, END)
        elif self.input.get() == '1':
            self.label_vote.config(text='Voted John')
            self.label_quit.destroy()
            self.label_title.config(text='CANDIDATE MENU')
            self.input.destroy()
            self.button_save.destroy()
        elif self.input.get() == 'John':
            self.label_vote.config(text='Voted John')
            self.label_quit.destroy()
            self.label_title.config(text='CANDIDATE MENU')
            self.input.destroy()
            self.button_save.destroy()
        elif self.input.get() == '2':
            self.label_vote.config(text='Voted Jane')
            self.label_quit.destroy()
            self.label_title.config(text='CANDIDATE MENU')
            self.input.destroy()
            self.button_save.destroy()
        elif self.input.get() == 'Jane':
            self.label_vote.config(text='Voted Jane')
            self.label_quit.destroy()
            self.label_title.config(text='CANDIDATE MENU')
            self.input.destroy()
            self.button_save.destroy()
        else:
            self.label_title.config(text='INPUT NOT VALID')
            self.label_vote.destroy()
            self.label_quit.destroy()
            self.input.destroy()
            self.button_save.destroy()
