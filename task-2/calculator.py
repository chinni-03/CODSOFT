import tkinter as tk

DARK_GRAY = '#4c4c4c'
LIGHT_GRAY = '#666666'
LIGHTER_GRAY = '#cdcdcd'
WHITE = '#fff'
OFF_WHITE = '#ddd5c1'
DEFAULT_FONT = ('Arial', 16)
LARGE_FONT = ('Arial', 20)
LARGER_FONT = ('Arial', 32)
ORANGE = '#ff9a81'

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('300x600')
        self.window.resizable(0, 0)
        self.window.title('Calculator')

        self.total = ''
        self.current = ''

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }

        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+"
        }

        self.output_frame = self.create_output_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()
        self.create_operators()
        self.create_additional_buttons()
        self.total_label, self.label = self.create_labels()
        self.keyboard_keys()
        
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def create_output_frame(self):
        frame = tk.Frame(self.window, height=200)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window, bg=DARK_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons(self):
        for digit, position in self.digits.items():
            if(digit == 0):
                button = tk.Button(self.buttons_frame, text=str(digit),bg=DARK_GRAY, fg=OFF_WHITE, font=DEFAULT_FONT, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                button.grid(row=position[0], column=position[1], columnspan=2, sticky=tk.NSEW)
            else:
                button = tk.Button(self.buttons_frame, text=str(digit), bg=DARK_GRAY, fg=OFF_WHITE, font=DEFAULT_FONT, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                button.grid(row=position[0], column=position[1], sticky=tk.NSEW)
    
    def create_operators(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=DARK_GRAY, fg=OFF_WHITE, font=DEFAULT_FONT, borderwidth=0, command=lambda x=operator: self.add_operator_to_expression(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg=LIGHT_GRAY, fg=OFF_WHITE, font=DEFAULT_FONT, borderwidth=0, command=self.clear)
        button.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
    
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=ORANGE, fg=OFF_WHITE, font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, sticky=tk.NSEW)
        
    def create_additional_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
    
    def create_labels(self):
        total_label = tk.Label(self.output_frame, text=self.current, anchor=tk.E, bg=LIGHTER_GRAY, font=LARGE_FONT, padx=20)
        total_label.pack(expand=True, fill='both')
        
        label = tk.Label(self.output_frame, text=self.current, anchor=tk.E, bg=LIGHTER_GRAY, font=LARGER_FONT, padx=20)
        label.pack(expand=True, fill='both')
        return total_label, label

    def add_to_expression(self, value):
        self.current += str(value)
        self.update_label()
    
    def update_label(self):
        self.label.config(text=self.current)

    def add_operator_to_expression(self, operator):
        self.current += operator
        self.total += self.current
        self.current = ''
        self.update_total()
        self.update_label()
    
    def update_total(self):
        expression = self.total
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol}')
        self.total_label.config(text=expression)

    def clear(self):
        self.current = ''
        self.total = ''
        self.update_label()
        self.update_total()

    def evaluate(self):
        self.total += self.current
        self.update_total()
        try:
            self.current = str(eval(self.total))
            self.total = ''
        except Exception as e:
            self.current = 'error'
        finally:
            self.update_label()

    def keyboard_keys(self):
        self.window.bind('<Return>', lambda event:self.evaluate)
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.add_operator_to_expression(operator))

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()