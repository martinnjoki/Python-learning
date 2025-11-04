#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the benefits: "))
gloss_salary = basic_salary + benefits
nssf_base = max(gloss_salary, 18000)
nhdf = 0.0075 * gloss_salary

if gloss_salary <= 80000:
    nhif = 1200
    nssf = 0.06 * nssf_base
    taxable_income = gloss_salary - (nssf + nhdf + nhif)
    print(f"Gloss Salary: {gloss_salary}")
    print(f"NHIF: {nhif}")
    print(f"NSSF: {nssf}")
    print(f"Taxable_income: {taxable_income}")
    #Continue with the program above, then use  the gross salary to find the NSSF.
    

