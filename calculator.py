from tkinter import *

class Calculator:
    buttonsName = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', "<-", 'C', '-', '+', '*', '/', '=']
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

        self.root = Tk()
        self.isFirstNumber = True
        self.lastValue = 0
        self.lastOperation = ''

        self.root.title(name)
        self.buttons = []

        frame = Frame(
            master=self.root,
            relief=RAISED,
            borderwidth=1
        )

        self.label = Label(master=frame,text='0', width=30)
        frame.grid(row=0, padx=5, pady=5, columnspan=5)
        self.label.pack()

        x = 1
        y = 0
    
        for i in range(len(self.buttonsName)):
            frame = Frame(
                master=self.root,
                relief=RAISED,
                borderwidth=1)
            
            self.buttons.append(Button(master=frame,text=self.buttonsName[i], command=lambda text=self.buttonsName[i]: self.handle_button_click(text)))
            print(self.buttonsName[i])
            frame.grid(row=x,column=y, padx=5, pady=5)
            y += 1
            if y == 4:
                y = 0
                x += 1
            self.buttons[-1].pack()
        self.label.config(text='0')
        self.root.bind("<Key>", self.handle_keypressed_event)

    def handle_button_click(self, buttonText):
        if buttonText == "<-":
            self.handle_keypressed('\b')
        elif buttonText == 'C':
            self.handle_keypressed('c')
        else:
            self.handle_keypressed(buttonText)
    
    def add_symbol(self, symbol):
        text = self.label.cget("text")
        if len(self.lastOperation) != 0 and self.isFirstNumber:
            self.lastValue = float(text)
            text = "0"
            self.isFirstNumber = False

        if text == '0' and symbol != '.':
            text = symbol
        else:
            text += symbol
        try:
            d = float(text)
            print(d)
            self.label.config(text=text)
        except ValueError as e:
            print('cannot handle', text, ' number', ". Error: ", e)

    def remove_symbol(self):
        if self.isFirstNumber:
            self.lastOperation = ''
        text = self.label.cget("text")
        if len(text) < 2:
            text = '0'
        else:
            text = text[:-1]
        self.label.config(text=text)

    def make_operation(self, operation):
        if not self.isFirstNumber:
            self.make_equal()
        self.lastValue = float(self.label.cget("text"))
        self.lastOperation = operation

    def operation_value(self, firstNumber, secondNumber, operation):
        if operation == '+':
            return firstNumber + secondNumber
        elif operation == '*':
            return firstNumber * secondNumber
        elif operation == '-':
            return firstNumber - secondNumber
        else:
            try:
                return firstNumber / secondNumber
            except ValueError as e:
                print("Invalid operands. Error: ", e)
                return 0

    def make_equal(self):
        curValue = float(self.label.cget("text"))
        if not self.isFirstNumber:
            print(self.lastValue)
            self.label.config(text=str(self.operation_value(self.lastValue, curValue, self.lastOperation)))
            self.isFirstNumber=True
            self.lastOperation=''
        
    def remove_all(self):
        self.label.config(text='0')
        self.lastValue = 0
        self.lastOperation = ''
        self.isFirstNumber = True

    def handle_keypressed(self, c):
        if c >= '0' and c <= '9' or c == '.':
            self.add_symbol(c)
        elif c == '*' or c == '/' or c == '+' or c == '-':
            self.make_operation(c)
        elif c == '=':
            self.make_equal()
        elif c == '\b':
            self.remove_symbol()
        elif c == 'c':
            self.remove_all()

    def handle_keypressed_event(self, event):
        self.handle_keypressed(event.char)

    def start(self):
        self.root.mainloop()


c = Calculator('Calculator', 110, 250)
c.start()
