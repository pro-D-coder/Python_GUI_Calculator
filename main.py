import tkinter as tk
from tkinter import messagebox

def check_operand(string): 
    for i in string:
        if i in ["+","-","÷","x","%"]:
            return True
def add_on_scr(input,scr_data):
    if input in ["%","-","+","%","x","÷"]:
        data = scr_data.get()
        try:
            if data[len(data) - 1] in ["%","-","+","%","x","÷"]:
                pass
            else:
                expression = scr_data.get()
                expression += input
                scr_data.set(expression)
        except:
            pass
    elif input == ".":
        data = scr_data.get()
        if check_operand(data) != True:
            if data.count(".",0, len(data)) < 1:
                expression = scr_data.get()
                expression += input
                scr_data.set(expression)
            else:
                pass
        else:
            data = scr_data.get()
            list_of_operators = list()
            for i in range(0, len(data)):
                if(data[i] in ["+","-","÷","x","%"]):
                    list_of_operators.append(i)
            last_data = data[list_of_operators[len(list_of_operators) -1 ] + 1:]
            if last_data.count(".", 0, len(last_data)) < 1:
                expression = scr_data.get()
                expression += input
                scr_data.set(expression)
            else:
                pass
    else:
        expression = scr_data.get()
        expression += input
        scr_data.set(expression)
def give_anwser(scr_data):
    try:
        expression = (str(scr_data.get()).replace("÷", "/")).replace("x","*")
        expression = eval(expression)
        scr_data.set(expression)
    except ZeroDivisionError as e:
        scr_data.set("∞")
    except NameError as e:
        print(e)
        messagebox.showerror("Error","Enter Integer and floats only!!")
        scr_data.set("")
    except SyntaxError as e:
        print(e)
        messagebox.showerror("Error","Please correct your expression!!")
    except Exception as e:
        print(e)
def clear_scr(scr_data):
    scr_data.set("")
def Backspace(scr_data):
    data = scr_data.get()
    data = data[:len(data)-1]
    scr_data.set(data)
def put_sign(scr_data):
    data = scr_data.get()
    list_of_operators = []
    if check_operand(data) != True:
        if len(data) >=1:
            scr_data.set("-" + scr_data.get())
        else:
            return
    else:
        for i in range(0, len(data)):
            if(data[i] in ["+","-","÷","x","%"]):
                list_of_operators.append(i)
        if len(data[list_of_operators[len(list_of_operators) -1 ] + 1:]) >= 1:
            last_data_with_sign = "("+"-" + data[list_of_operators[len(list_of_operators) -1 ] + 1:] + ")"
            scr_data.set(data[:list_of_operators[len(list_of_operators) -1 ] + 1]+last_data_with_sign)
def sqr_ans(scr_data):
    data = scr_data.get()
    try:
        if check_operand(data) != True:
            if len(data) >= 1:
                scr_data.set(eval(data)**2)
    except:
        pass
    else:
        try:
            list_of_operators = list()
            for i in range(0, len(data)):
                if(data[i] in ["+","-","÷","x","%"]):
                    list_of_operators.append(i)
            if len(data[list_of_operators[len(list_of_operators) -1 ] + 1:]) >= 1:
                sqr_with_exp = data[:list_of_operators[len(list_of_operators) -1 ] + 1] + str(eval(data[list_of_operators[len(list_of_operators) -1 ] + 1:])**2)
                scr_data.set(sqr_with_exp)
        except:
            pass
#Main Function for whole programe.
def main():
    main_win = tk.Tk()
    main_win.title("Calculator By D")
    main_win.geometry("375x500")
    main_win.configure(bg = "#325866")
    scr_data = tk.StringVar()
    #Entry for inputs in 
    display_entry = tk.Entry(main_win,
    width = 34,
    relief = tk.FLAT,
    justify = "right",
    bg = "#41575f",
    fg = "white",
    font = ("Consolas",15,"bold"),
    textvariable = scr_data,
    )
    display_entry.focus_set()


    #Button for number 1
    button_for_1 = tk.Button(main_win,
    text = "1",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("1",scr_data),
    )
    #Button for number 2
    button_for_2 = tk.Button(main_win,
    text = "2",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("2",scr_data),
    )
    #Button for number 3
    button_for_3 = tk.Button(main_win,
    text = "3",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("3",scr_data),
    )
    #Button for number 4
    button_for_4 = tk.Button(main_win,
    text = "4",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("4",scr_data),
    )
    #Button for number 5
    button_for_5 = tk.Button(main_win,
    text = "5",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("5",scr_data),
    )
    #Button for number 6
    button_for_6 = tk.Button(main_win,
    text = "6",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("6",scr_data),
    )
    #Button for number 7
    button_for_7 = tk.Button(main_win,
    text = "7",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("7",scr_data),
    )
    #Button for number 8
    button_for_8 = tk.Button(main_win,
    text = "8",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("8",scr_data),
    )
    #Button for number 9
    button_for_9 = tk.Button(main_win,
    text = "9",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("9",scr_data),
    )
    #Button for number 0
    button_for_0 = tk.Button(main_win,
    text = "0",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("0",scr_data),
    )
    #Button for clearing screen
    button_for_clear = tk.Button(main_win,
    text = "C",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 14,
    command = lambda:clear_scr(scr_data)
    )
    #Button for + operation
    button_for_add = tk.Button(main_win,
    text = "+",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 14,
    command = lambda:add_on_scr("+",scr_data),
    )
    #Button for - operation
    button_for_sub = tk.Button(main_win,
    text = "-",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("-",scr_data),
    )
    #Button for x operation
    button_for_mul = tk.Button(main_win,
    text = "x",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("x",scr_data),
    )
    #Button for ÷ operation
    button_for_div = tk.Button(main_win,
    text = "÷",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("÷",scr_data),
    )
    #Button for = operation
    button_for_eq = tk.Button(main_win,
    text = "=",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:give_anwser(scr_data)
    )
    #Button for +/- operation
    button_for_sign = tk.Button(main_win,
    text = "±",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:put_sign(scr_data)
    )
    #Button for . operation
    button_for_dot = tk.Button(main_win,
    text = ".",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr(".",scr_data),
    )
    #Button for Backspace operation
    button_for_bs = tk.Button(main_win,
    text = "⇐",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 21,
    pady = 14,
    command = lambda:Backspace(scr_data)
    )
    #Button for % operation
    button_for_rem = tk.Button(main_win,
    text = "%",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 14,
    command = lambda:add_on_scr("%",scr_data),
    )
    #Button for square operation
    button_for_sqr = tk.Button(main_win,
    text = "x²",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "right",
    font = ("Consolas",14,"bold"),
    padx = 22,
    pady = 14,
    command = lambda:sqr_ans(scr_data),
    )
    #placing all the widgets
    [
        button_for_1.place(x = 0,y = 166),
        button_for_2.place(x = 75,y = 166),
        button_for_3.place(x = 150,y = 166),
        button_for_4.place(x = 0,y = 250),
        button_for_5.place(x = 75,y = 250),
        button_for_6.place(x = 150,y = 250),
        button_for_7.place(x = 0,y = 334),
        button_for_8.place(x = 75,y = 334),
        button_for_9.place(x = 150,y = 334),
        button_for_0.place(x = 75,y = 418),
        button_for_clear.place(x = 0, y = 102),
        button_for_sign.place(x = 0, y = 418),
        button_for_dot.place(x = 150, y = 418),
        button_for_add.place(x = 225, y = 102),
        button_for_sub.place(x = 225, y = 166),
        button_for_mul.place(x = 225, y = 250),
        button_for_div.place(x = 225, y = 334),
        button_for_eq.place(x = 225, y = 418),
        button_for_bs.place(x = 75, y = 102),
        button_for_rem.place(x = 150, y = 102),
        button_for_sqr.place(x = 300, y = 102),
        display_entry.place(x = 0,y = 0,height = 100)
    ]
    main_win.mainloop()

main() #calling the main function