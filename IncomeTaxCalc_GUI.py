from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# based on the 2021 tax brackets
# https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets


# creating the window for the from
window = Tk()
window.title("Income Tax Calculator")
window.geometry("500x250")
window.eval('tk::PlaceWindow . center')
window.configure(bg="#E0E0E0")

# creating the form content/fields and their placement in the window -- .grid
annual_income = IntVar()
annual_income.set("Enter your annual income")
income_entry = Entry(window, textvariable=annual_income, justify="center")
income_entry.pack(pady="15")
f_status = StringVar()
f_status.set("Select your filing status")
status = ["Single", "Married - Jointly", "Married - Separately", "Head of Household"]
status_entry = OptionMenu(window, f_status, *status)
status_entry.pack(pady="15")

# Styling the fields
income_entry.configure(width="26", font="Georgia 15")
status_entry.configure(width="23", height="1", bg="#E0E0E0", font="Georgia 15")

# creating function that calculates income tax based on filing status
# that will be used as a command when Calculate button is clicked
# pulling the f-status value to section off which tax rates to use


def calculate_tax():
    if f_status.get() == "Single":
        rates = [.10, .12, .22, .24, .32, .35, .37]
        income_cutoff = [9950, 40525, 86375, 164925, 209425, 523600]
        if annual_income.get() <= 9950:
            tax_owed = (annual_income.get() * rates[0])
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 9951 and annual_income.get() < 40525:
            tax_owed = (995 + (rates[1] * (annual_income.get() - income_cutoff[0])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 40526 and annual_income.get() < 86375:
            tax_owed = (4664 + (rates[2] * (annual_income.get() - income_cutoff[1])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 86376 and annual_income.get() < 164925:
            tax_owed = (14751 + (rates[3] * (annual_income.get() - income_cutoff[2])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 164926 and annual_income.get() < 209425:
            tax_owed = (33603 + (rates[4] * (annual_income.get() - income_cutoff[3])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 209426 and annual_income.get() < 523600:
            tax_owed = (47843 + (rates[5] * (annual_income.get() - income_cutoff[4])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() >= 523601:
            tax_owed = (157804.25 + (rates[6] * (annual_income.get() - income_cutoff[5])))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))


    elif f_status.get() == "Married - Jointly":
        rates = [.10, .12, .22, .24, .32, .35, .37]
        income_cutoff = [19900, 81050, 172750, 329850, 418850, 628300]

        if annual_income.get() <= 19900:
            tax_owed = (annual_income.get() * rates[0])
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 19901 and annual_income.get() < 81050:
            tax_owed = 1990 + (rates[1] * (annual_income.get() - income_cutoff[0]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 81051 and annual_income.get() < 172750:
            tax_owed = 9328 + (rates[2] * (annual_income.get() - income_cutoff[1]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 172751 and annual_income.get() < 329850:
            tax_owed = 29502 + (rates[3] * (annual_income.get() - income_cutoff[2]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 329851 and annual_income.get() < 418850:
            tax_owed = 67206 + (rates[4] * (annual_income.get() - income_cutoff[3]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 418851 and annual_income.get() < 628300:
            tax_owed = 95686 + (rates[5] * (annual_income.get() - income_cutoff[4]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() >= 628301:
            tax_owed = 168993.50 + (rates[6] * (annual_income.get() - income_cutoff[5]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))

    elif f_status.get() == "Married - Separately":
        rates = [.10, .12, .22, .24, .32, .35, .37]
        income_cutoff = [9950, 40525, 86375, 164925, 209425, 314150]

        if annual_income.get() <= 9950:
            tax_owed = (annual_income.get() * rates[0])
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 9951 and annual_income.get() < 40525:
            tax_owed = 995 + (rates[1] * (annual_income.get() - income_cutoff[0]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 40526 and annual_income.get() < 86375:
            tax_owed = 4664 + (rates[2] * (annual_income.get() - income_cutoff[1]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 86376 and annual_income.get() < 164925:
            tax_owed = 14751 + (rates[3] * (annual_income.get() - income_cutoff[2]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 164926 and annual_income.get() < 209425:
            tax_owed = 33603 + (rates[4] * (annual_income.get() - income_cutoff[3]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 209426 and annual_income.get() < 314150:
            tax_owed = 47843 + (rates[5] * (annual_income.get() - income_cutoff[4]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() >= 314151:
            tax_owed = 84496 + (rates[6] * (annual_income.get() - income_cutoff[5]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))


    elif f_status.get() == "Head of Household":
        rates = [.10, .12, .22, .24, .32, .35, .37]
        income_cutoff = [14200, 54200, 86350, 164900, 209400, 523600]

        if annual_income.get() <= 14200:
            tax_owed = (annual_income.get() * rates[0])
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 14201 and annual_income.get() < 54200:
            tax_owed = 1420 + (rates[1] * (annual_income.get() - income_cutoff[0]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 54201 and annual_income.get() < 86350:
            tax_owed = 6220 + (rates[2] * (annual_income.get() - income_cutoff[1]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 86351 and annual_income.get() < 164900:
            tax_owed = 13293 + (rates[3] * (annual_income.get() - income_cutoff[2]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 164901 and annual_income.get() < 209400:
            tax_owed = 32145 + (rates[4] * (annual_income.get() - income_cutoff[3]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() > 209401 and annual_income.get() < 523600:
            tax_owed = 46385 + (rates[5] * (annual_income.get() - income_cutoff[4]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))
        elif annual_income.get() >= 523601:
            tax_owed = 156355 + (rates[6] * (annual_income.get() - income_cutoff[5]))
            return messagebox.showinfo('results', "{0:,.2f}".format(tax_owed))


Button(window, text="Calculate", activebackground="#2CD10A", activeforeground="#FFFFFF", bg="#42DC22", fg="#FFFFFF", font="Georgia 15", relief="raised", width="26", height="1", command=calculate_tax).pack(pady="15")

window.mainloop()

# font ideas --> Arial Black, Impact, Georgia
