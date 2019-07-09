from tkinter import*


def btnClick(numbers):
    global usage
    usage = usage + str(numbers)
    text_Input.set(usage)


def btnClearDisplay():
    global usage
    usage = ""
    text_Input.set("EMPTY ...")

cal= Tk()
cal.title("Horja Robert Emanuel - Python proj. Morse Code")

#Make the background blue2 (search in tkinter library for colours name)
cal.configure(background="blue2")
usage = ""
text_Input= StringVar()

#The display ...
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=100, width=80,
                   bg="gray16", fg="green4", justify='right').grid(columnspan=13)

#Row1
btnQ = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="Q", bg="navy",  command=lambda: btnClick("_ _ . _   ")).grid(row=1, column=0)
btnW = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="W", bg="navy", command=lambda: btnClick(". _ _   ")).grid(row=1, column=1)
btnE = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="E", bg="navy", command=lambda: btnClick(".   ")).grid(row=1, column=2)
btnR = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="R", bg="navy",  command=lambda: btnClick(". _ .   ")).grid(row=1, column=3)
btnT = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="T", bg="navy",  command=lambda: btnClick("_   ")).grid(row=1, column=4)
btnY = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="Y", bg="navy",  command=lambda: btnClick("_ . _ _   ")).grid(row=1, column=5)
btnU = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="U", bg="navy",  command=lambda: btnClick(". . _   ")).grid(row=1, column=6)
btnI = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="I", bg="navy",  command=lambda: btnClick(". .   ")).grid(row=1, column=7)
btnO = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="O", bg="navy",  command=lambda: btnClick("_ _ _   ")).grid(row=1, column=8)
btnP = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="P", bg="navy",  command=lambda: btnClick(". _ _ .   ")).grid(row=1, column=9)

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="0", bg="navy",  command=lambda: btnClick("_ _ _ _ _   ")).grid(row=1, column=10)

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="1", bg="navy", command=lambda: btnClick(". _ _ _ _   ")).grid(row=1, column=11)
btn2 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="2", bg="navy", command=lambda: btnClick(". . _ _ _   ")).grid(row=1, column=12)

#Row2
btnA = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="A", bg="navy",  command=lambda: btnClick(". _   ")).grid(row=2, column=0)
btnS = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="S", bg="navy", command=lambda: btnClick(". . .   ")).grid(row=2, column=1)
btnD = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="D", bg="navy", command=lambda: btnClick("_ . .   ")).grid(row=2, column=2)
btnF = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="F", bg="navy",  command=lambda: btnClick(". . _ .   ")).grid(row=2, column=3)
btnG = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="G", bg="navy",  command=lambda: btnClick("_ _ .   ")).grid(row=2, column=4)
btnH = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="H", bg="navy",  command=lambda: btnClick(". . . .   ")).grid(row=2, column=5)
btnJ = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="J", bg="navy",  command=lambda: btnClick(". _ _ _   ")).grid(row=2, column=6)
btnK = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="K", bg="navy",  command=lambda: btnClick("_ . _   ")).grid(row=2, column=7)
btnL = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="L", bg="navy",  command=lambda: btnClick(". _ . .   ")).grid(row=2, column=8)
btnNewWord = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="New word", bg="navy",  command=lambda: btnClick("   ///   ")).grid(row=2, column=9)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="3", bg="navy",  command=lambda: btnClick(". . . _ _   ")).grid(row=2, column=10)
btn4 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="4", bg="navy",  command=lambda: btnClick(". . . . _   ")).grid(row=2, column=11)
btn5 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="5", bg="navy",  command=lambda: btnClick(". . . . .   ")).grid(row=2, column=12)

#Row3
btnZ = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="Z", bg="navy",  command=lambda: btnClick("_ _ . .   ")).grid(row=3, column=0)
btnX = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="X", bg="navy", command=lambda: btnClick("_ . . _   ")).grid(row=3, column=1)
btnC = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="C", bg="navy", command=lambda: btnClick("_ . _ .   ")).grid(row=3, column=2)
btnV = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="V", bg="navy",  command=lambda: btnClick(". . . _   ")).grid(row=3, column=3)
btnB = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="B", bg="navy",  command=lambda: btnClick("_ . . .   ")).grid(row=3, column=4)
btnN = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="N", bg="navy",  command=lambda: btnClick("_ .   ")).grid(row=3, column=5)
btnM = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="M", bg="navy",  command=lambda: btnClick("_ _   ")).grid(row=3, column=6)
btnPara1 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="(", bg="navy",  command=lambda: btnClick("(   ")).grid(row=3, column=7)
btnPara2 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text=")", bg="navy",  command=lambda: btnClick(")   ")).grid(row=3, column=8)
btnClear = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="CLEAR", bg="navy",  command=btnClearDisplay).grid(row=3, column=9)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="6", bg="navy",  command=lambda: btnClick("_ . . . .   ")).grid(row=3, column=10)
btn7 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="7", bg="navy",  command=lambda: btnClick("_ _ . . .   ")).grid(row=3, column=11)
btn8 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="8", bg="navy",  command=lambda: btnClick("_ _ _ . .   ")).grid(row=3, column=12)


#Row4

btnAron = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
               text="@", bg="navy",  command=lambda: btnClick("@   ")).grid(row=4, column=0)

btnHash = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="#", bg="navy",  command=lambda: btnClick("#   ")).grid(row=4, column=1)
        
btnPercent = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="%", bg="navy",  command=lambda: btnClick("%   ")).grid(row=4, column=2)

btnAmpers = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="&", bg="navy",  command=lambda: btnClick("&   ")).grid(row=4, column=3)

btnPipe = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="|", bg="navy",  command=lambda: btnClick("|   ")).grid(row=4, column=4)

btnStar = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="*", bg="navy",  command=lambda: btnClick("*   ")).grid(row=4, column=5)

btnTilde = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="~", bg="navy",  command=lambda: btnClick("~   ")).grid(row=4, column=6)

btnPoint = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text=".", bg="navy",  command=lambda: btnClick(".   ")).grid(row=4, column=7)

btnComma = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text=",", bg="navy",  command=lambda: btnClick(",   ")).grid(row=4, column=8)

btnSpace = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="Space", bg="navy",  command=lambda: btnClick("   ")).grid(row=4, column=9)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="9", bg="navy",  command=lambda: btnClick("_ _ _ _ .   ")).grid(row=4, column=10)

btnSpec1 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="?", bg="navy",  command=lambda: btnClick("?   ")).grid(row=4, column=11)

btnSpec2 = Button(cal, padx=16, pady=16, bd=8, fg="azure", font=('arial', 20, 'bold'),
              text="!", bg="navy",  command=lambda: btnClick("!   ")).grid(row=4, column=12)

cal.mainloop()
