# based on the 2020 tax rates for someone filing single
# https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
def tax():
    rates = [.10, .12, .22, .24, .32, .35, .37]
    income_cutoff = [9875, 40125, 85525, 163300, 207350, 518400]
    income = float(input("Enter your annual income: "))

    if income <= 9875:
        tax_owed = float(income) * rates[0]
        print(float(tax_owed))
    elif income > 9876 and income < 40125:
        tax_owed = (987.5 + (rates[1]*(float(income) - income_cutoff[0])))
        print(float(tax_owed))
    elif income > 40126 and income < 85525:
        tax_owed = (4617.5 + (rates[2]*(float(income) - income_cutoff[1])))
        print(float(tax_owed))
    elif income > 85526 and income < 163300:
        tax_owed = (14605.5 + (rates[3]*(float(income) - income_cutoff[2])))
        print(float(tax_owed))
    elif income > 163301 and income < 207350:
        tax_owed = (33271.5 + (rates[4]*(float(income) - income_cutoff[3])))
        print(float(tax_owed))
    elif income > 207351 and income < 518400:
        tax_owed = (47367.5 + (rates[5]*(float(income) - income_cutoff[4])))
        print(float(tax_owed))
    elif income > 518401:
        tax_owed = (156235 + (rates[6]*(float(income) - income_cutoff[5])))
        print(float(tax_owed))

tax()
