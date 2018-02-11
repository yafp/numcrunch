#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' a simple number cruncher (calculator) in python '''


# https://github.com/hiamandeep/tkcalc/blob/master/tkcalc.py
# https://github.com/kirimijesse/GUI-Python-Calculator-/blob/master/calculator.py

# icon:
# https://www.iconsdb.com/navy-blue-icons/calculator-8-icon.html

# ------------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------------
import Tkinter as Tk
import datetime                     # for timestamp generation
import tkFont                       # for fonts
#import math
from PIL import Image, ImageTk      # for image handling

import __future__

# project specific
import colors as c
import settings as s 


# ---------------------------------------------------------------------------- #
# ON VERBOSE
# ---------------------------------------------------------------------------- #
def on_verbose(message):
    ''' Display verbose output if verbose is set '''
    if(s.VERBOSE):
        timestamp = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
        print(timestamp + " ::: "+message)


class Window(Tk.Frame):
    ''' foo '''
    def __init__(self, master=None):
        ''' init the frame '''
        Tk.Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title(s.APP_NAME)
        self.master.geometry('{}x{}'.format(s.WINDOW_WIDTH, s.WINDOW_HEIGHT))

        # Font
        #
        display_font_big = tkFont.Font(family='digital-7', size=48, weight='normal')
        display_font_small = tkFont.Font(family='digital-7', size=12, weight='normal')
        display_font_small_bold = tkFont.Font(family='digital-7', size=12, weight='bold')

        # Window icon
        icon = Tk.PhotoImage(file='images/calc.png')
        self.master.call('wm', 'iconphoto', self.master, icon)


        # ROW 0 - Head
        #
        # LABEL: calculator model/series
        self.label_series = Tk.Label(root, text="PUE-2703 P-Series")
        self.label_series['font'] = display_font_small_bold
        self.label_series.grid(row=0, column=1, columnspan=2, sticky="w", padx=10, pady=(10, 0))
        self.label_series.config(fg=c.GRAY)

        # solar panel image
        image = Image.open("images/solar-panel.gif")
        photo = ImageTk.PhotoImage(image)
        self.label = Tk.Label(image=photo)
        self.label.image = photo
        self.label.config(justify='right')
        self.label.grid(row=0, column=3, columnspan=2, sticky="e", padx=30, pady=(10, 0))


        # ROW 1
        #
        # ENTRY - History / Status
        self.entry_status = Tk.Entry(root, width=s.INPUT_WIDTH)
        self.entry_status['justify'] = 'right'
        self.entry_status['bg'] = c.BLACK
        self.entry_status['fg'] = c.GREEN
        self.entry_status['disabledbackground'] = c.BLACK
        self.entry_status['disabledforeground'] = c.YELLOW
        self.entry_status['font'] = display_font_small
        self.entry_status['state'] = 'disabled'
        self.entry_status['borderwidth'] = 0
        self.entry_status['highlightbackground'] = c.BLACK
        self.entry_status.grid(row=1, column=1, columnspan=4, sticky="nsew", padx=(0, 0), pady=(10, 0), ipady=10)


        # ROW 2
        #
        # ENTRY - Display
        self.entry_display = Tk.Entry(root, width=s.INPUT_WIDTH)
        self.entry_display['justify'] = 'center'
        self.entry_display['bg'] = c.BLACK
        self.entry_display['fg'] = c.GREEN
        self.entry_display['disabledbackground'] = c.BLACK
        self.entry_display['disabledforeground'] = c.GREEN
        self.entry_display['font'] = display_font_big
        self.entry_display['state'] = 'disabled'
        self.entry_display['borderwidth'] = 0
        self.entry_display['highlightbackground'] = c.BLACK
        self.entry_display.grid(row=2, column=1, columnspan=4, sticky="nsew", pady=(0, 15), ipady=25)


        # ROW 3:
        #
        # Button: Backspace
        self.bt_backspace = Tk.Button(self.master, command=lambda: self.backspace())
        self.bt_backspace['text'] = "BACK"
        self.bt_backspace['state'] = "normal"
        self.bt_backspace['width'] = s.BUTTON_WIDTH
        self.bt_backspace['height'] = s.BUTTON_HEIGHT_REDUCED
        self.bt_backspace['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_backspace['background'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT
        self.bt_backspace['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_backspace['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_backspace['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_backspace.grid(row=3, column=1, padx=s.BUTTON_PADDING_X, pady=(0, 15))

        # ESC
        self.bt_esc = Tk.Button(self.master, command=lambda: self.clear_text())
        self.bt_esc['text'] = "RESET"
        self.bt_esc['state'] = "normal"
        self.bt_esc['width'] = s.BUTTON_WIDTH
        self.bt_esc['height'] = s.BUTTON_HEIGHT_REDUCED
        self.bt_esc['foreground'] = "red"
        self.bt_esc['background'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT
        self.bt_esc['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_esc['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_esc['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_esc.grid(row=3, column=4, padx=s.BUTTON_PADDING_X, pady=(0, 15))


        # ROW 4
        #
        # Button 7
        self.bt_7 = Tk.Button(self.master, command=lambda: self.append_to_display(7))
        self.bt_7['text'] = "7"
        self.bt_7['state'] = "normal"
        self.bt_7['width'] = s.BUTTON_WIDTH
        self.bt_7['height'] = s.BUTTON_HEIGHT
        self.bt_7['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_7['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_7['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_7['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_7['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_7.grid(row=4, column=1, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 8
        self.bt_8 = Tk.Button(self.master, command=lambda: self.append_to_display(8))
        self.bt_8['text'] = "8"
        self.bt_8['state'] = "normal"
        self.bt_8['width'] = s.BUTTON_WIDTH
        self.bt_8['height'] = s.BUTTON_HEIGHT
        self.bt_8['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_8['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_8['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_8['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_8['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_8.grid(row=4, column=2, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 9
        self.bt_9 = Tk.Button(self.master, command=lambda: self.append_to_display(9))
        self.bt_9['text'] = "9"
        self.bt_9['state'] = "normal"
        self.bt_9['width'] = s.BUTTON_WIDTH
        self.bt_9['height'] = s.BUTTON_HEIGHT
        self.bt_9['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_9['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_9['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_9['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_9['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_9.grid(row=4, column=3, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button: Operator +
        self.bt_op_add = Tk.Button(self.master, command=lambda: self.append_to_display(" + "))
        self.bt_op_add['text'] = "+"
        self.bt_op_add['state'] = "normal"
        self.bt_op_add['width'] = s.BUTTON_WIDTH
        self.bt_op_add['height'] = s.BUTTON_HEIGHT
        self.bt_op_add['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_op_add['background'] = s.BUTTON_BACKGROUND_COLOR_OPERATOR
        self.bt_op_add['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_op_add['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_op_add['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_op_add.grid(row=4, column=4, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # ROW 5 - 4-6
        #
        # Button 4
        self.bt_4 = Tk.Button(self.master, command=lambda: self.append_to_display(4))
        self.bt_4['text'] = "4"
        self.bt_4['state'] = "normal"
        self.bt_4['width'] = s.BUTTON_WIDTH
        self.bt_4['height'] = s.BUTTON_HEIGHT
        self.bt_4['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_4['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_4['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_4['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_4['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_4.grid(row=5, column=1, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 5
        self.bt_5 = Tk.Button(self.master, command=lambda: self.append_to_display(5))
        self.bt_5['text'] = "5"
        self.bt_5['state'] = "normal"
        self.bt_5['width'] = s.BUTTON_WIDTH
        self.bt_5['height'] = s.BUTTON_HEIGHT
        self.bt_5['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_5['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_5['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_5['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_5['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_5.grid(row=5, column=2, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 6
        self.bt_6 = Tk.Button(self.master, command=lambda: self.append_to_display(6))
        self.bt_6['text'] = "6"
        self.bt_6['state'] = "normal"
        self.bt_6['width'] = s.BUTTON_WIDTH
        self.bt_6['height'] = s.BUTTON_HEIGHT
        self.bt_6['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_6['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_6['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_6['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_6['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_6.grid(row=5, column=3, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button: Operator -
        self.bt_op_subst = Tk.Button(self.master, command=lambda: self.append_to_display(" - "))
        self.bt_op_subst['text'] = "-"
        self.bt_op_subst['state'] = "normal"
        self.bt_op_subst['width'] = s.BUTTON_WIDTH
        self.bt_op_subst['height'] = s.BUTTON_HEIGHT
        self.bt_op_subst['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_op_subst['background'] = s.BUTTON_BACKGROUND_COLOR_OPERATOR
        self.bt_op_subst['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_op_subst['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_op_subst['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_op_subst.grid(row=5, column=4, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # ROW 6 - 1-3
        #
        # Button 1
        self.bt_1 = Tk.Button(self.master, command=lambda: self.append_to_display(1))
        self.bt_1['text'] = "1"
        self.bt_1['state'] = "normal"
        self.bt_1['width'] = s.BUTTON_WIDTH
        self.bt_1['height'] = s.BUTTON_HEIGHT
        self.bt_1['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_1['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_1['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_1['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_1['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_1.grid(row=6, column=1, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 2
        self.bt_2 = Tk.Button(self.master, command=lambda: self.append_to_display(2))
        self.bt_2['text'] = "2"
        self.bt_2['state'] = "normal"
        self.bt_2['width'] = s.BUTTON_WIDTH
        self.bt_2['height'] = s.BUTTON_HEIGHT
        self.bt_2['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_2['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_2['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_2['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_2['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_2.grid(row=6, column=2, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button 3
        self.bt_3 = Tk.Button(self.master, command=lambda: self.append_to_display(3))
        self.bt_3['text'] = "3"
        self.bt_3['state'] = "normal"
        self.bt_3['width'] = s.BUTTON_WIDTH
        self.bt_3['height'] = s.BUTTON_HEIGHT
        self.bt_3['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_3['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_3['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_3['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_3['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_3.grid(row=6, column=3, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button: Operator *
        self.bt_op_multi = Tk.Button(self.master, command=lambda: self.append_to_display(" * "))
        self.bt_op_multi['text'] = "*"
        self.bt_op_multi['state'] = "normal"
        self.bt_op_multi['width'] = s.BUTTON_WIDTH
        self.bt_op_multi['height'] = s.BUTTON_HEIGHT
        self.bt_op_multi['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_op_multi['background'] = s.BUTTON_BACKGROUND_COLOR_OPERATOR
        self.bt_op_multi['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_op_multi['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_op_multi['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_op_multi.grid(row=6, column=4, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # ROW 7
        #
        # Button: ,
        self.bt_comma = Tk.Button(self.master, command=lambda: self.append_to_display("."))
        self.bt_comma['text'] = "."
        self.bt_comma['state'] = "normal"
        self.bt_comma['width'] = s.BUTTON_WIDTH
        self.bt_comma['height'] = s.BUTTON_HEIGHT
        self.bt_comma['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_comma['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_comma['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_comma['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_comma['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_comma.grid(row=7, column=1, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)

        # Button: 0
        self.bt_0 = Tk.Button(self.master, command=lambda: self.append_to_display(0))
        self.bt_0['text'] = "0"
        self.bt_0['state'] = "normal"
        self.bt_0['width'] = s.BUTTON_WIDTH
        self.bt_0['height'] = s.BUTTON_HEIGHT
        self.bt_0['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_0['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_0['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_0['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_0['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_0.grid(row=7, column=2, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # Button: %
        self.bt_percent = Tk.Button(self.master, command=lambda: self.append_to_display('%'))
        self.bt_percent['text'] = "%"
        self.bt_percent['state'] = "normal"
        self.bt_percent['width'] = s.BUTTON_WIDTH
        self.bt_percent['height'] = s.BUTTON_HEIGHT
        self.bt_percent['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_percent['background'] = s.BUTTON_BACKGROUND_COLOR_NUMBER
        self.bt_percent['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_percent['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_percent['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_percent.grid(row=7, column=3, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # Button: Operator /
        self.bt_op_div = Tk.Button(self.master, command=lambda: self.append_to_display(" / "))
        self.bt_op_div['text'] = "/"
        self.bt_op_div['state'] = "normal"
        self.bt_op_div['width'] = s.BUTTON_WIDTH
        self.bt_op_div['height'] = s.BUTTON_HEIGHT
        self.bt_op_div['foreground'] = s.BUTTON_FONT_COLOR_DEFAULT
        self.bt_op_div['background'] = s.BUTTON_BACKGROUND_COLOR_OPERATOR
        self.bt_op_div['activebackground'] = s.BUTTON_BACKGROUND_COLOR_DEFAULT_HOVER
        self.bt_op_div['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_op_div['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_op_div.grid(row=7, column=4, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # ROW 8 - 
        #
        # Button: =
        self.bt_equals = Tk.Button(self.master, command=lambda: self.on_calc())
        self.bt_equals['text'] = "="
        self.bt_equals['state'] = "normal"
        self.bt_equals['width'] = 20
        self.bt_equals['height'] = s.BUTTON_HEIGHT
        self.bt_equals['foreground'] = c.AQUA
        self.bt_equals['background'] = c.NAVY
        self.bt_equals['activebackground'] = c.NAVY
        self.bt_equals['activeforeground'] = c.AQUA
        self.bt_equals['borderwidth'] = s.BUTTON_BORDER_WIDTH
        self.bt_equals['highlightbackground'] = s.BUTTON_BORDER_COLOR
        self.bt_equals.grid(row=8, column=3, columnspan=2, padx=s.BUTTON_PADDING_X, pady=s.BUTTON_PADDING_Y)


        # ROW 9 - Footer
        #
        # LABEL
        self.ui_footer_label = Tk.Label(root, text=s.APP_NAME+" v"+s.APP_VERSION+"\n"+s.APP_URL)
        self.ui_footer_label.config(justify='center') # center input
        self.ui_footer_label.grid(row=9, column=1, columnspan=4, pady=10)
        self.ui_footer_label.config(fg="gray")


        self.master.bind("<KeyPress>", self.keydown)
        #frame.bind("<KeyRelease>", keyup)


        # master.grid_columnconfigure(4, minsize=100)
        col_count, row_count = master.grid_size()
        for col in xrange(col_count):
            master.grid_columnconfigure(col, minsize=20)

        for row in xrange(row_count):
            master.grid_rowconfigure(row, minsize=20)

        # eye-candy: change status line color over time
        self.change_color()


    def keydown(self, event):
        ''' triggered by key-presses '''
        on_verbose('Function keydown launched')
        print "\tPressed", repr(event.char)

        if event.char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', \
                            '+', '-', '*', '/', '.', '(', ')', '%']:
            self.append_to_display(event.char)
        elif(event.char == "\r"):
            on_verbose("\tEnter/Return - triggering equals")
            self.on_calc()
        elif(event.char == "\x08"):
            on_verbose("\tBackspace - triggering BACK")
            self.backspace()
        else:
            on_verbose("\tIgnoring input")



    def on_calc(self):
        ''' do calculate the expression currently in display '''
        on_verbose('Function: on_calc launched')

        self.expression = self.entry_display.get()
        on_verbose("\t"+self.expression)

        on_verbose("\tHandling %")
        self.expression = self.expression.replace("%", "/ 100")
        on_verbose("\t"+self.expression)

        try:
            #self.result = eval(self.expression) # 1/2 = 0
            self.result = eval(self.expression+'.0') # 1/2 = 0.5 

            # Try to detect if results ends with .0
            split = str(self.result).split('e')
            if split[0].endswith('.0'):
                self.replace_text(self.result) 
                self.backspace()
                self.backspace()
            else:
                 self.replace_text(self.result)

            #self.replace_text(self.result)
        except:
            on_verbose("\tError: on_calc")



    def backspace(self):
        ''' backspace - deletes last character from display '''
        on_verbose("Function: backspace launched")

        # get current input conternt
        old_user_input = self.entry_display.get()
        on_verbose("\tPrevious: "+old_user_input)

        # build new string
        new_user_input = old_user_input[:-1]

        # clear display
        self.clear_text()

        # update display
        self.append_to_display(new_user_input)



    def append_to_display(self, text):
        ''' append number to display '''
        on_verbose("Function: append_to_display launched")
        on_verbose("\tAppending: "+str(text))

        # enable display
        self.entry_display['state'] = 'normal'

        self.entryText = self.entry_display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replace_text(text)
        else:
            self.entry_display.insert(self.textLength, text)

        # disable display
        self.entry_display['state'] = 'disabled'



    def replace_text(self, text):
        ''' replace existing display text '''
        on_verbose("Function: replace_text launched")

        # enable display
        self.entry_display['state'] = 'normal'

        # update display
        self.entry_display.delete(0, Tk.END)
        self.entry_display.insert(0, text)

        # disable display
        self.entry_display['state'] = 'disabled'



    def clear_text(self):
        ''' Resets the input '''
        on_verbose("Function: clear_text launched")

        # enable display
        self.entry_display['state'] = 'normal'

        self.entry_display.delete(0, Tk.END)

        # disable display
        self.entry_display['state'] = 'disabled'



    def change_color(self):
        ''' eye-candy: change color of status line in display'''
        on_verbose("Function: change_color launched")

        current_color = self.entry_status.cget('disabledforeground')
        on_verbose("\tCurrent status line color: "+str(current_color))

        if current_color == c.YELLOW:
            next_color = c.BLACK
            next_interval = 50000
            next_status_text = ""
        else:
            next_color = c.YELLOW
            next_interval = 2000
            next_status_text = "Battery low "

        on_verbose("\tComing status line color: "+str(next_color))

        # updating color & text
        self.entry_status.config(disabledforeground=next_color)
        self.entry_status['state'] = 'normal'
        self.entry_status.delete(0, Tk.END)
        self.entry_status.insert(0, next_status_text)
        self.entry_status['state'] = 'disabled'

        root.after(next_interval, self.change_color)



# ------------------------------------------------------------------------------
# Let user select an XML file
# ------------------------------------------------------------------------------
root = Tk.Tk()
app = Window(root)
root.mainloop()
