from tkinter import *


def evaluate(equation):
    ans = eval(equation)
    msgMain.insert(END, "\n" + str(ans))


panel = Tk()

topFrame = Frame(panel, bg="#dddddd")
topFrame.pack(side=TOP)
middleFrame = Frame(panel, bg="#222222")
middleFrame.pack()
bottomFrame = Frame(panel, bg="#222222")
bottomFrame.pack(side=BOTTOM)
numberFrame = Frame(middleFrame, bg="#222222")
numberFrame.grid(rowspan=9, columnspan=3, row=10, column=1)
operationFrame = Frame(middleFrame, bg="#222222")
operationFrame.grid(rowspan=12, row=6, column=4)
arrowFrame = Frame(middleFrame, bg="#222222")
arrowFrame.grid(rowspan=4, columnspan=2, row=0, column=3)

lblHeader = Label(topFrame, text="Texas Instruments", bg="#dddddd")
msgMain = Text(topFrame, bg="#99aa99", height=2, width=15, font=("Helvetica", 25), padx=10)

btnOne = Button(numberFrame, text="1", bg="#dbca9c", width=5,
                font=("Helvetica", 15), command=lambda: msgMain.insert(END, "1"))
btnTwo = Button(numberFrame, text="2", bg="#dbca9c", width=5,
                font=("Helvetica", 15), command=lambda: msgMain.insert(END, "2"))
btnThree = Button(numberFrame, text="3", bg="#dbca9c", width=5,
                  font=("Helvetica", 15), command=lambda: msgMain.insert(END, "3"))
btnFour = Button(numberFrame, text="4", bg="#dbca9c", width=5,
                 font=("Helvetica", 15), command=lambda: msgMain.insert(END, "4"))
btnFive = Button(numberFrame, text="5", bg="#dbca9c", width=5,
                 font=("Helvetica", 15), command=lambda: msgMain.insert(END, "5"))
btnSix = Button(numberFrame, text="6", bg="#dbca9c", width=5,
                font=("Helvetica", 15), command=lambda: msgMain.insert(END, "6"))
btnSeven = Button(numberFrame, text="7", bg="#dbca9c", width=5,
                  font=("Helvetica", 15), command=lambda: msgMain.insert(END, "7"))
btnEight = Button(numberFrame, text="8", bg="#dbca9c", width=5,
                  font=("Helvetica", 15), command=lambda: msgMain.insert(END, "8"))
btnNine = Button(numberFrame, text="9", bg="#dbca9c", width=5,
                 font=("Helvetica", 15), command=lambda: msgMain.insert(END, "9"))
btnZero = Button(numberFrame, text="0", bg="#dbca9c", width=5,
                 font=("Helvetica", 15), command=lambda: msgMain.insert(END, "0"))
btnDot = Button(numberFrame, text="\u00b7", bg="#dbca9c", width=5,
                font=("Helvetica", 15), command=lambda: msgMain.insert(END, "."))
btnNegative = Button(numberFrame, text="(-)", bg="#dbca9c", width=5,
                     font=("Helvetica", 15), command=lambda: msgMain.insert(END, "-"))


btnDivide = Button(operationFrame, text="\u00f7", bg="#3f3d4c", fg="white", width=5,
                   font=("Helvetica", 15), command=lambda: msgMain.insert(END, "/"))
btnMultiply = Button(operationFrame, text="\u00d7", bg="#3f3d4c", fg="white", width=5,
                     font=("Helvetica", 15), command=lambda: msgMain.insert(END, "*"))
btnSubtract = Button(operationFrame, text=" \u2212", bg="#3f3d4c", fg="white", width=5,
                     font=("Helvetica", 15), command=lambda: msgMain.insert(END, "-"))
btnAdd = Button(operationFrame, text="+", bg="#3f3d4c", fg="white", width=5,
                font=("Helvetica", 15), command=lambda: msgMain.insert(END, "+"))
btnEquals = Button(operationFrame, text="=", bg="#3f3d4c", fg="white", width=5,
                   font=("Helvetica", 15), command=lambda: evaluate(msgMain.get("1.0", END)))

btnUp = Button(arrowFrame, text="\u25b2", bg="#3f3d4c", fg="white", width=17, font=("Helvetica", 8))
btnDown = Button(arrowFrame, text="\u25bc", bg="#3f3d4c", fg="white", width=17, font=("Helvetica", 8))
btnLeft = Button(arrowFrame, text="\u25c0", bg="#3f3d4c", fg="white", width=10, font=("Helvetica", 8))
btnRight = Button(arrowFrame, text="\u25b6", bg="#3f3d4c", fg="white", width=10, font=("Helvetica", 8))

btn2nd = Button(middleFrame, text="2nd", bg="#8b8995", fg="white", width=7, font=("Helvetica", 10))
btnDrg = Button(middleFrame, text="DRG", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnDel = Button(middleFrame, text="DEL", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.delete("end-2c"))
btnLog = Button(middleFrame, text="LOG", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.insert(END, "log("))
btnPrb = Button(middleFrame, text="PRB", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnSym = Button(middleFrame, text="\u2218 \' \"", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnLn = Button(middleFrame, text="LN", bg="#000000", fg="white", width=7,
               font=("Helvetica", 10), command=lambda: msgMain.insert(END, "ln("))
btnAbc = Button(middleFrame, text="Ab/c", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnData = Button(middleFrame, text="DATA", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnStatvar = Button(middleFrame, text="STATVAR", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnClear = Button(middleFrame, text="CLEAR", bg="#000000", fg="white", width=7,
                  font=("Helvetica", 10), command=lambda: msgMain.delete("1.0", END))
btnPi = Button(middleFrame, text="\u03c0", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnSin = Button(middleFrame, text="SIN", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.insert(END, "sin("))
btnCos = Button(middleFrame, text="COS", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.insert(END, "cos("))
btnTan = Button(middleFrame, text="TAN", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.insert(END, "tan("))
btnHat = Button(middleFrame, text="^", bg="#000000", fg="white", width=7,
                font=("Helvetica", 10), command=lambda: msgMain.insert(END, "^"))
btnInverse = Button(middleFrame, text="x\u207b\u00b9", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnOpen = Button(middleFrame, text="(", bg="#000000", fg="white", width=7,
                 font=("Helvetica", 10), command=lambda: msgMain.insert(END, "("))
btnClose = Button(middleFrame, text=")", bg="#000000", fg="white", width=7,
                  font=("Helvetica", 10), command=lambda: msgMain.insert(END, ")"))
btnSquare = Button(middleFrame, text="x\u00b2", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnMemvar = Button(middleFrame, text="MEMVAR", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnSto = Button(middleFrame, text="STO\u25b6", bg="#000000", fg="white", width=7, font=("Helvetica", 10))
btnOn = Button(middleFrame, text="ON", bg="#000000", fg="white", width=7, font=("Helvetica", 10))

entry1 = Entry(bottomFrame)

lblHeader.grid()
msgMain.grid(columnspan=2, row=1, padx=50, pady=(0, 10))

btnOne.grid(row=2, column=0, padx=6, pady=6)
btnTwo.grid(row=2, column=1, padx=6, pady=6)
btnThree.grid(row=2, column=2, padx=6, pady=6)
btnFour.grid(row=1, column=0, padx=6, pady=6)
btnFive.grid(row=1, column=1, padx=6, pady=6)
btnSix.grid(row=1, column=2, padx=6, pady=6)
btnSeven.grid(row=0, column=0, padx=6, pady=6)
btnEight.grid(row=0, column=1, padx=6, pady=6)
btnNine.grid(row=0, column=2, padx=6, pady=6)
btnZero.grid(row=3, column=0, padx=6, pady=6)
btnDot.grid(row=3, column=1, padx=6, pady=6)
btnNegative.grid(row=3, column=2, padx=6, pady=6)

btnDivide.grid(row=1, pady=7)
btnMultiply.grid(row=2, pady=7)
btnSubtract.grid(row=3, pady=7)
btnAdd.grid(row=4, pady=7)
btnEquals.grid(row=5, pady=7)

btnUp.grid(columnspan=3, row=0, column=2, pady=2)
btnDown.grid(columnspan=3, row=2, column=2, pady=2)
btnLeft.grid(columnspan=3, row=1, column=0, padx=3, pady=2)
btnRight.grid(columnspan=3, row=1, column=4, padx=3, pady=2)

btn2nd.grid(row=0, column=0, padx=6, pady=6)
btnDrg.grid(row=0, column=1, padx=6, pady=6)
btnDel.grid(row=0, column=2, padx=6, pady=6)
btnLog.grid(row=2, column=0, padx=6, pady=6)
btnPrb.grid(row=2, column=1, padx=6, pady=6)
btnSym.grid(row=2, column=2, padx=6, pady=6)
btnLn.grid(row=4, column=0, padx=6, pady=6)
btnAbc.grid(row=4, column=1, padx=6, pady=6)
btnData.grid(row=4, column=2, padx=6, pady=6)
btnStatvar.grid(row=4, column=3, padx=6, pady=6)
btnClear.grid(row=4, column=4, padx=6, pady=6)
btnPi.grid(row=6, column=0, padx=6, pady=6)
btnSin.grid(row=6, column=1, padx=6, pady=6)
btnCos.grid(row=6, column=2, padx=6, pady=6)
btnTan.grid(row=6, column=3, padx=6, pady=6)
btnHat.grid(row=8, column=0, padx=6, pady=6)
btnInverse.grid(row=8, column=1, padx=6, pady=6)
btnOpen.grid(row=8, column=2, padx=6, pady=6)
btnClose.grid(row=8, column=3, padx=6, pady=6)
btnSquare.grid(row=10, column=0, padx=6, pady=6)
btnMemvar.grid(row=12, column=0, padx=6, pady=6)
btnSto.grid(row=14, column=0, padx=6, pady=6)
btnOn.grid(row=16, column=0, padx=6, pady=6)

panel.mainloop()

#new message