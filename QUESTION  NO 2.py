#assignment income tax
a=int(input("enter the gross_income"))
b=int(input ("enter the no of dependent"))
standard_deduction =10000
additional_deduction = 3000
tax_rate= 20
taxable_income =a-standard_deduction-(additional_deduction*b)
print("the taxable income is",taxable_income)
tax=(taxable_income*tax_rate)
print("the tax is",tax)