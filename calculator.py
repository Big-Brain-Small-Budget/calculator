import tkinter as tk


# sets up main window
window = tk.Tk()
window.configure(background="white")
window.geometry("1000x570+350+80")
window.title("big brain small budget shopping calculator")

# sets product parameters
productAmount = 4
products = ["Good Clock", "Toaster", "Vacuum", "Insurance"]
prices = [34.99, 59.99, 799.99, 2]

frames = []
productTitles = []
priceTags = []
plusButtons = []
minusButtons = []
amounts = []
amountLabels = []
totals = []
totalLabels = []

subTotal = 0.0
vatRate = 0.2
vatTotal = 0.0
endTotal = 0.0

for i in range(productAmount):
    amounts.append(0)
    totals.append(0.0)

# increasing amount of a selected product
def addAmount(index):
    global amounts
    global totals
    global subTotal
    global vatTotal
    global endTotal
    
    amounts[index] = round(min(amounts[index] + 1, 99), 2)
    totals[index] = round(prices[index] * amounts[index], 2)
    
    subTotal = 0
    for total in totals:
        subTotal += total
    subTotal = round(subTotal, 2)
    
    vatTotal = round(subTotal * vatRate, 2)
    
    endTotal = round(subTotal + vatTotal, 2)
    
    amountLabels[index].configure(text="Units: " + str(amounts[index]))
    totalLabels[index].configure(text="€" + str(totals[index]))
    
    subTotalLabel.configure(text="Subtotal: €" + str(subTotal))
    vatTotalLabel.configure(text="VAT: €" + str(vatTotal))
    endTotalLabel.configure(text="Total: €" + str(endTotal))

    print(totals)


# decreasing amount of a selected product
def subAmount(index):
    global amounts
    global totals
    global subTotal
    global vatTotal
    global endTotal
    
    amounts[index] = round(max(amounts[index] - 1, 0), 2)
    totals[index] = round(prices[index] * amounts[index], 2)

    subTotal = 0
    for total in totals:
        subTotal += total
    subTotal = round(subTotal, 2)
    
    vatTotal = round(subTotal * vatRate, 2)
    
    endTotal = round(subTotal + vatTotal, 2)
    
    amountLabels[index].configure(text="Units: " + str(amounts[index]))
    totalLabels[index].configure(text="€" + str(totals[index]))
    
    subTotalLabel.configure(text="Subtotal: €" + str(subTotal))
    vatTotalLabel.configure(text="VAT: €" + str(vatTotal))
    endTotalLabel.configure(text="Total: €" + str(endTotal))
    
    print(totals)


# creates title
title = tk.Label(text="BBSB Official Calculator",
                 width=440,
                 fg="white",
                 bg="gray",
                 font=("Courier", 32, "bold"),
                 borderwidth=5,
                 relief="raised")
title.pack(padx=20, pady=20)


# Creates a frame to hold the totals
totalsFrame = tk.Frame(window)
totalsFrame.pack(fill="x", padx=20)


# Creates label to diaplay subtotal
subTotalLabel = tk.Label(totalsFrame,
                         text="Subtotal: €" + str(subTotal),
                         fg="white",
                         bg="black",
                         font=("Courier", 18, "bold"),
                         borderwidth=3,
                         relief="sunken")
subTotalLabel.pack(side="left", padx=20)


# Creates label to diaplay VAT total
vatTotalLabel = tk.Label(totalsFrame,
                         text="VAT: €" + str(vatTotal),
                         fg="white",
                         bg="black",
                         font=("Courier", 18, "bold"),
                         borderwidth=3,
                         relief="sunken")
vatTotalLabel.pack(side="left", padx=20)

# Creates label to display final total
endTotalLabel = tk.Label(totalsFrame,
                         text="Total: €" + str(endTotal),
                         fg="white",
                         bg="black",
                         font=("Courier", 18, "bold"),
                         borderwidth=3,
                         relief="sunken")
endTotalLabel.pack(side="right", padx=20)


# main interface creation loop
for i in range(productAmount):
    frames.append(tk.Frame(window,
                          bg="gray",
                          borderwidth=5,
                          relief="sunken"))
    frames[i].pack(fill="x", padx=20, pady=20)
    
    productTitles.append(tk.Label(frames[i],
                        text=products[i],
                        font=("Arial", 18),
                        fg="white",
                        bg="green",
                        borderwidth=3,
                        relief="raised"))
    productTitles[i].pack(side="left", padx=10, pady=10)
    
    priceTags.append(tk.Label(frames[i],
                    text="Price: €" + str(prices[i]),
                    font=("Arial", 18),
                    fg="white",
                    bg="blue",
                    borderwidth=3,
                    relief="raised"))
    priceTags[i].pack(side="left", padx=10, pady=10)
    
    totalLabels.append(tk.Label(frames[i],
                                text="€" + str(totals[i]),
                                font=("Arial", 18),
                                fg="white",
                                bg="red",
                                borderwidth=3,
                                relief="raised"))
    totalLabels[i].pack(side="right", padx=10, pady=10)
    
    amountLabels.append(tk.Label(frames[i],
                    text="Units: " + str(amounts[i]),
                    font=("Arial", 18),
                    fg="white",
                    bg="red",
                    borderwidth=3,
                    relief="raised"))
    amountLabels[i].pack(side="right", padx=10, pady=10)
    
    plusButtons.append(tk.Button(frames[i],
                 text="+",
                 font=("Arial", 11),
                 borderwidth=3,
                 relief="raised",
                 command=lambda x=i: addAmount(x)))
    plusButtons[i].pack(side="left", padx=10, pady=10)
    
    minusButtons.append(tk.Button(frames[i],
                 text="-",
                 font=("Arial", 11),
                 borderwidth=3,
                 relief="raised",
                 command=lambda x=i: subAmount(x)))
    minusButtons[i].pack(side="left", padx=10, pady=10)
    


print(totals)

window.mainloop()





#plusButtons[i].configure(command=lambda x=i: addAmount(x))
#minusButtons[i].configure(command=lambda x=i: subAmount(x))

#   plusButtons[i].configure(command=partial(addAmount, i))
#   minusButtons[i].configure(command=partial(subAmount, i))

# frame1 = tk.Frame(window,
#                   highlightbackground="black",
#                   highlightthickness=1)
# frame1.pack(fill="x", padx=20)

# toasterLabel = tk.Label(frame1,
#                         text="A toaster (trust me)",
#                         fg="white",
#                         bg="blue")
# toasterLabel.pack(side="left", padx=10, pady=10)
                        

# button1 = tk.Button(frame1,
#                     text="this is moderately insane.",
#                     fg="white",
#                     bg="red",
#                     command=insane
#                     )
# button1.pack(side="left", padx=10, pady=10)

# add1 = tk.Button(frame1,
#                  text="+",
#                  command=addAmount)
# add1.pack(side="left", padx=10, pady=10)

# sub1 = tk.Button(frame1,
#                  text="-",
#                  command=subAmount)
# sub1.pack(side="left", padx=10, pady=10)

# sub1 = tk.Button(frame1,
#                  text="-",
#                  command=subAmount)
# sub1.pack(side="left", padx=10, pady=10)
