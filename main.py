import tkinter as tk  #import Tkinter module for widegts
from tkinter import messagebox #importing messagebox for showing Error dialog boxes
import math as m #importing math module for doing fast mathematical operations
#All Functions that required for calculatoin and adding signs

#function that return true if the expression contains operators
def check_operand(string): 
    for i in string:
        if i in ["+","-","÷","x","%","^"]:
            return True #return true if given string contains operators
#function that add given input in Entry using buttons
def add_on_scr(input,scr_data):
    if input in ["%","-","+","%","x","÷"]:   #if input is an operation
        data = scr_data.get() #getting data form entry
        try:
            if data[len(data) - 1] in ["%","-","+","%","x","÷","^","."]: #checking that if last part of entry is an symbol or not
                pass #if yes  then do not add operators on screen
            else:
                expression = scr_data.get()  #Else add in entry 
                expression += input
                scr_data.set(expression)
        except:
            pass
    elif input == ".": #checkinf if input is "."
        data = scr_data.get() #getting data form entry
        if check_operand(data) != True: #checking that expression contains operators or not
            if data.count(".",0, len(data)) < 1: #checking if operand already have . or not if not then add
                expression = scr_data.get()
                expression += input
                scr_data.set(expression)
            else:
                pass
        else:
            data = scr_data.get() #getting data from entry
            list_of_operators = list() #list of operators
            for i in range(0, len(data)):   #getting indices of operators present in expression
                if(data[i] in ["+","-","÷","x","%","^"]):      #
                    list_of_operators.append(i)                #End here
            last_data = data[list_of_operators[len(list_of_operators) -1 ] + 1:] #getting last value from expression and
            if last_data.count(".", 0, len(last_data)) < 1: #checking that the value contains dot(.) or not if not then add
                expression = scr_data.get()
                expression += input
                scr_data.set(expression)
            else:   #if last value contain dot(.) then do nothing
                pass
    else: #if input is anything else then add it in entry
        expression = scr_data.get()
        expression += input
        scr_data.set(expression)

#Function that evaluate the given expression used in = operation
def give_anwser(scr_data):
    try:
        expression = (str(scr_data.get()).replace("÷", "/")).replace("x","*") #getting the expression from entry with replacement of "÷" to "/" and "x" to "*"
        expression = expression.replace("^","**") #and also replacing "^" sign to "**" for python interpreter 
        expression = eval(expression) #evaluating the expression
        scr_data.set(expression)  #setting the entry to solution
    except ZeroDivisionError as e: #if number is divided by zero except Exception and setting enrty to infinite sign
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

#Funtion that used to clearing the entry
def clear_scr(scr_data):
    scr_data.set("")

#Function that remove singal value from right side of expression
def Backspace(scr_data):
    data = scr_data.get() #getting data
    data = data[:len(data)-1] #using slicing technic to remove only rightmost value or number or operator
    scr_data.set(data) #setting the entry

#Function that used to add - sign on operands
def put_sign(scr_data):
    data = scr_data.get() #getting data from entry
    list_of_operators = [] #list that contain indices of operators
    #checking that entry contain operators or not 
    if check_operand(data) != True:
        if len(data) >=1 and data not in ".": #if not then check length of the expression and also check that the last value is a dot(.) if dot then do not add sign on it.
            scr_data.set("-" + scr_data.get()) #adding sign on given data 
        else: #else do nothing
            return
    else: #if entry contains operator
        for i in range(0, len(data)): #then find index of all operators
            if(data[i] in ["+","-","÷","x","%","^"]):
                list_of_operators.append(i)
        if len(data[list_of_operators[len(list_of_operators) -1 ] + 1:]) >= 1: #here checking that after an operand there is an value or not if not then do not add - sign 
            last_data_with_sign = "("+"-" + data[list_of_operators[len(list_of_operators) -1 ] + 1:] + ")" #if yes then get last value of expression and add - sign on it.
            scr_data.set(data[:list_of_operators[len(list_of_operators) -1 ] + 1]+last_data_with_sign) #here taking entry value with no sign and adding it with sign add value

#Function that add ^ sign to expression and solve it if there is already an ^ sign  
def x_power_a(scr_data):
    data = scr_data.get()   #getting expression
    index_of_operand = list()   #list of operators
    for i in range(len(data)):  #getting indices of operators present in expression
        if data[i] in ["+","-","÷","x","%","^"]:
            index_of_operand.append(i)
    if check_operand(data) == True:  #checking that expression contains operators or not
        if data[len(data) -1] not in ["+","-","÷","x","%","^","."]: #checking if last value of expression contain operators if yes then do not add ^ sign
            if data[index_of_operand[len(index_of_operand) -1]] == "^": #checking the right most operator is "^" if yes then solve already ^ sign
                        if len(index_of_operand) == 1: #here if number of operands then directly solve the power expression and set it 
                            try:
                                scr_data.set(str(eval(data.replace("^","**"))) + "^") 
                            except:
                                pass
                        else: #if number operand is greater then 1 then do this    
                            try:
                                if data[len(data) -1] in ["+","-","÷","x","%","^"]: #if rightmost part of expression is a operator then do not add ^ sign
                                    pass
                                else: #Else solve first power equation and then add another "^" sign on it
                                    last_sol = eval(data[index_of_operand[len(index_of_operand) -2] + 1:].replace("^","**"))
                                    scr_data.set(data[:index_of_operand[len(index_of_operand) -2] + 1]+str(last_sol) + "^")
                            except:
                                messagebox.showwarning("Error","Please Correct Your Expression!")           
            else:
                scr_data.set(data + "^")
    else: #else if there is no operand in expression then add "^" sign
        if len(data) >= 1 and data[len(data) -1] not in ["+","-","÷","x","%","^","."]:
            scr_data.set(data + "^")

#Function that find squareroot
def sqrt_ans(scr_data):
    data = scr_data.get() #getting entry data
    try:
        if check_operand(data) != True: #checking that entry contain operators or not
            if len(data) >= 1: #if there is no operator check length of entry if greater then one then solve the equation
                scr_data.set(m.sqrt(eval(data)))
    except:
        pass
    else: #if there is operators then do this
        try:
            list_of_operators = list() #list of operators
            for i in range(0, len(data)):   #getting indices of operators present in expression
                if(data[i] in ["+","-","÷","x","%"]):
                    list_of_operators.append(i)
            if len(data[list_of_operators[len(list_of_operators) -1 ] + 1:]) >= 1: #checking the length of rightmost value after an operator if greater then one find squareroot of rightmost value
                sqr_with_exp = data[:list_of_operators[len(list_of_operators) -1 ] + 1] + str(m.sqrt(eval(data[list_of_operators[len(list_of_operators) -1 ] + 1:])))  #here adding squareroot of to the rightmost value with left expression
                scr_data.set(sqr_with_exp) #setting up the entry
        except:
            pass

#Function that remove the whole rightmost value
def CE_ope(scr_data):
    data = scr_data.get() #getting entry data
    if check_operand(data) != True: #checking that entry contain operators or not
        if len(data) >= 1: #if not then set entry to empty
            scr_data.set("")
    else: #Else 
        index_of_operand = list() #find index of all operators
        for i in range(0, len(data)): 
            if data[i] in ["+","-","÷","x","%","^"]:
                index_of_operand.append(i)
        new_value = data[:index_of_operand[len(index_of_operand)-1]+1] #here extracting the expression without the rightmost value
        scr_data.set(new_value) #setting the new value
#Main Function for whole programe.
def main():
    main_win = tk.Tk() #creating instance of TK class.
    main_win.title("Calculator By D")  #setting up the window title
    main_win.geometry("375x500") #setting up the window size
    main_win.configure(bg = "#325866") #configuring main window background colour
    scr_data = tk.StringVar() #variable that store expression for entry
    
    #Entry for inputs  
    display_entry = tk.Entry(main_win,
    width = 34,
    relief = tk.FLAT,
    justify = "right",
    bg = "#41575f",
    fg = "white",
    font = ("Consolas",15,"bold"),
    textvariable = scr_data,
    )
    display_entry.focus_set() #setting the foucs to entry

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
    command = lambda:give_anwser(scr_data),
    )
    #Button for +/- sign operation
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
    #Button for %(reminder) operation
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
    #Button for x to power a operation
    button_for_sqr = tk.Button(main_win,
    text = "xª",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "right",
    font = ("Consolas",14,"bold"),
    padx = 21,
    pady = 14,
    command = lambda:x_power_a(scr_data),
    )
    #Button for square root operation
    button_for_sqrt = tk.Button(main_win,
    text = "√",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:sqrt_ans(scr_data),
    )
    #Button for left bracket "("
    button_for_left_brac = tk.Button(main_win,
    text = "(",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr("(", scr_data),
    )
    #Button for right bracket ")"
    button_for_right_brac = tk.Button(main_win,
    text = ")",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 26,
    pady = 24,
    command = lambda:add_on_scr(")", scr_data),
    )
    #button for CE operation
    button_for_CE = tk.Button(main_win,
    text = "CE",
    bg = "#233b44",
    fg = "#c9c5c2",
    relief = tk.FLAT,
    bd = 0,
    justify = "center",
    font = ("Consolas",14,"bold"),
    padx = 21,
    pady = 24,
    command = lambda:CE_ope(scr_data),
    )
    #placing all the widgets
    [
        button_for_1.place(x = 0,y = 166),              #
        button_for_2.place(x = 75,y = 166),             #
        button_for_3.place(x = 150,y = 166),            #
        button_for_4.place(x = 0,y = 250),              #
        button_for_5.place(x = 75,y = 250),             #
        button_for_6.place(x = 150,y = 250),            #
        button_for_7.place(x = 0,y = 334),              #
        button_for_8.place(x = 75,y = 334),             #
        button_for_9.place(x = 150,y = 334),            #
        button_for_0.place(x = 75,y = 418),             #
        button_for_clear.place(x = 0, y = 102),         #
        button_for_sign.place(x = 0, y = 418),          #
        button_for_dot.place(x = 150, y = 418),         #
        button_for_add.place(x = 225, y = 102),         #
        button_for_sub.place(x = 225, y = 166),         #
        button_for_mul.place(x = 225, y = 250),         #
        button_for_div.place(x = 225, y = 334),         #
        button_for_eq.place(x = 225, y = 418),          #
        button_for_bs.place(x = 75, y = 102),           #
        button_for_rem.place(x = 150, y = 102),         #
        button_for_sqr.place(x = 300, y = 102),         #
        button_for_sqrt.place(x = 300,y = 166),         #
        button_for_left_brac.place(x = 300, y = 250),   #
        button_for_right_brac.place(x = 300, y = 334),  #
        button_for_CE.place(x = 300, y = 418),          #
        display_entry.place(x = 0,y = 0,height = 100)   #placing End Here
    ]
    main_win.mainloop() #mainloop always required

main() #calling the main function