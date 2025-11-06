#Functions
def calculate_nhif(gross_salary):
    if gross_salary <=5999:
        nhif=150
    elif gross_salary <=7999:
        nhif = 300
    elif gross_salary <= 11999:
        nhif = 400
    elif gross_salary <= 14999:
        nhif = 500
    elif gross_salary <= 19999:
        nhif = 600
    elif gross_salary <= 24999:
        nhif = 750
    elif gross_salary <= 99999:
        nhif = 900
    return nhif
def calculate_nssf(gross_salary):
    nssf = gross_salary*0.06
    if nssf > 1000:
        nssf = 1000
        return nssf
def calculate_nhdf(gross_salary, nhdf_rate = 0.015):
    nhdf = gross_salary * 0.015
    return nhdf
basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter benefits: "))
gross_salary = basic_salary+benefits 
nhdf_deductions = calculate_nhdf(gross_salary)
nhif_deductions = calculate_nhif(gross_salary)
nssf_deductions = calculate_nssf(gross_salary)
print(f"Gloss salary: ksh{gross_salary}") 
print(f"Nhif: ksh {nhif_deductions}") 
print(f"Nssf: ksh{nssf_deductions}")
print(f"Nhdf: ksh{nhdf_deductions}")                        
    