import tkinter as tk
from functools import partial


# sets up main window
window = tk.Tk()
window.configure(background="white")
window.geometry("700x500+350+100")
window.title("big brain small budget shopping calculator")


productAmount = 4
products = ["Toaster", "Vacuum", "Insurance", "...---..."]
prices = [34.99, 799.99, 899.99, 1]

frames = []
productTitles = []
priceTags = []
plusButtons = []
minusButtons = []
amounts = []
amountLabels = []
totals = []
totalLabels = []
endTotal = 0

for i in range(productAmount):
    amounts.append(0)


def addAmount(index):
    global amounts
    amounts[index] += 1
    amountLabels[index].configure(text=str(amounts[index]))
    
    print(amounts)
    
def subAmount(index):
    global amounts
    amounts[index] -= 1
    amountLabels[index].configure(text=str(amounts[index]))
    
    print(amounts)


title = tk.Label(text="this is insane.",
                 width=440,
                 fg="white",
                 bg="gray",
                 font=("Arial", 40),
                 borderwidth=5,
                 relief="groove")
title.pack(padx=20, pady=20)


for i in range(productAmount):
    frames.append(tk.Frame(window,
                  highlightbackground="black",
                  highlightthickness=1))
    frames[i].pack(fill="x", padx=20, pady=20)
    
    productTitles.append(tk.Label(frames[i],
                        text=products[i],
                        font=("Arial", 18),
                        fg="white",
                        bg="blue"))
    productTitles[i].pack(side="left", padx=10, pady=10)
    
    priceTags.append(tk.Label(frames[i],
                    text="€" + str(prices[i]),
                    font=("Arial", 18),
                    fg="white",
                    bg="red"))
    priceTags[i].pack(side="left", padx=10, pady=10)
    
    plusButtons.append(tk.Button(frames[i],
                 text="+",
                 font=("Arial", 11),
                 command=lambda x=i: addAmount(x)))
    plusButtons[i].pack(side="left", padx=10, pady=10)
    
    minusButtons.append(tk.Button(frames[i],
                 text="-",
                 font=("Arial", 11),
                 command=lambda x=i: subAmount(x)))
    minusButtons[i].pack(side="left", padx=10, pady=10)
    
    amountLabels.append(tk.Label(frames[i],
                    text=amounts[i],
                    font=("Arial", 18),
                    fg="white",
                    bg="red"))
    amountLabels[i].pack(side="left", padx=10, pady=10)
    
    
    print(i)


print(amounts)

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