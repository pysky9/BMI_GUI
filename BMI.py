from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Tk

root = Tk()
root.title("BMI Calculator")


# Create the function to calculate the BMI
def BMI_calculate():
    """Getting the value from values that user inputs and Calculating BMI
       Showing the health information"""
    weight_cal = eval(weight_input.get())
    height_cal = eval(height_input.get())

    try:
        global BMI_cal
        global my_BMI
        global my_health
        BMI_cal = weight_cal / ((height_cal / 100)) ** 2

        my_BMI = Label(root, text=f"{BMI_cal}")
        my_BMI.grid(row=3, column=1)

        if BMI_cal >= 27:
            my_health = Label(root, text="肥胖")
        elif BMI_cal >= 24 and BMI_cal < 27:
            my_health = Label(root, text="過重")
        elif BMI_cal >= 18.5 and BMI_cal < 24:
            my_health = Label(root, text="正常")
        else:
            my_health = Label(root, text="過輕")
        my_health.grid(row=4, column=1)

    except:
        height_input.delete(0, "end")
        height_input.insert(0, "請輸入不為0的數字")


def clear():
    """clear all data that user key in when getting the information and user clicking the clear button"""
    global BMI_cal
    global my_BMI
    height_input.delete(0, "end")
    weight_input.delete(0, "end")
    my_BMI.config(text="")
    my_health.config(text="")


# using Label to creating the name of column and pack it
height = Label(root, text="請輸入身高(cm)", font=("Microsoft JhengHei", 12, "bold"), justify="left")
weight = Label(root, text="請輸入體重(kg)", font=("Microsoft JhengHei", 12, "bold"), justify="left")
BMI = Label(root, text="BMI result", font=("Microsoft JhengHei", 12, "bold"), justify="left")
health_comment = Label(root, text="健康資訊", font=("Microsoft JhengHei", 12, "bold"), justify="left")

height.grid(row=0, column=0)
weight.grid(row=1, column=0)
BMI.grid(row=3, column=0)
health_comment.grid(row=4, column=0)

# Creating the entry bar and Packing it on the screen
height_input = Entry(root)
height_input.grid(row=0, column=1, padx=10, columnspan=2)

weight_input = Entry(root)
weight_input.grid(row=1, column=1, padx=10, columnspan=2)

# Creating the button for calculating and clearing
BMI_calculator = Button(root, text="BMI計算", font=("Microsoft JhengHei", 12, "bold"), command=BMI_calculate)
Clear = Button(root, text="清除", font=("Microsoft JhengHei", 12, "bold"), command=clear)

BMI_calculator.grid(row=2, column=0)
Clear.grid(row=2, column=1)

root.mainloop()
