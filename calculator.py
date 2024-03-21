import tkinter as tk


# sets up main window
window = tk.Tk()
window.configure(background="white")
window.geometry("750x570+350+80")
window.title("big brain small budget shopping calculator")

# sets product parameters
productAmount = 4
products = ["Toaster", "Vacuum", "Insurance", "Charity"]
prices = [34.99, 799.99, 899.99, 2]

frames = []
productTitles = []
priceTags = []
plusButtons = []
minusButtons = []
amounts = []
amountLabels = []
totals = []
totalLabels = []
endTotal = 0.0

for i in range(productAmount):
    amounts.append(0)
    totals.append(0.0)

# increasing amount of a selected product
def addAmount(index):
    global amounts
    global totals
    global endTotal
    
    amounts[index] = round(min(amounts[index] + 1, 99), 2)
    totals[index] = round(prices[index] * amounts[index], 2)
    
    endTotal = 0
    for total in totals:
        endTotal += total
    endTotal = round(endTotal, 2)
    
    amountLabels[index].configure(text="Units: " + str(amounts[index]))
    totalLabels[index].configure(text="€" + str(totals[index]))
    endTotalLabel.configure(text="Subtotal: €" + str(endTotal))

    print(totals)


# decreasing amount of a selected product
def subAmount(index):
    global amounts
    global totals
    global endTotal
    
    amounts[index] = round(max(amounts[index] - 1, 0), 2)
    totals[index] = round(prices[index] * amounts[index], 2)

    endTotal = 0
    for total in totals:
        endTotal += round(total, 2)
    
    amountLabels[index].configure(text="Units: " + str(amounts[index]))
    totalLabels[index].configure(text="€" + str(totals[index]))
    endTotalLabel.configure(text="Subotal: €" + str(endTotal))
    
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


# creates label to display final total
endTotalLabel = tk.Label(text="Subtotal: €" + str(endTotal),
                         fg="white",
                         bg="black",
                         font=("Courier", 18, "bold"),
                         borderwidth=3,
                         relief="sunken")
endTotalLabel.pack(padx=20)


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
                        bg="blue",
                        borderwidth=3,
                        relief="raised"))
    productTitles[i].pack(side="left", padx=10, pady=10)
    
    priceTags.append(tk.Label(frames[i],
                    text="Price: €" + str(prices[i]),
                    font=("Arial", 18),
                    fg="white",
                    bg="red",
                    borderwidth=3,
                    relief="raised"))
    priceTags[i].pack(side="left", padx=10, pady=10)
    
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
    
    amountLabels.append(tk.Label(frames[i],
                    text="Units: " + str(amounts[i]),
                    font=("Arial", 18),
                    fg="white",
                    bg="red",
                    borderwidth=3,
                    relief="raised"))
    amountLabels[i].pack(side="left", padx=10, pady=10)
    
    totalLabels.append(tk.Label(frames[i],
                                text="€" + str(totals[i]),
                                font=("Arial", 18),
                                fg="white",
                                bg="red",
                                borderwidth=3,
                                relief="raised"))
    totalLabels[i].pack(side="left", padx=10, pady=10)


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
# add1.pack(side="left", padx=10, pady=10)

# sub1 = tk.Button(frame1,
#                  text="-",
#                  command=subAmount)
# sub1.pack(side="left", padx=10, pady=10)
