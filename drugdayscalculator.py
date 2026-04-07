#for medical purposes
import random, datetime 

#the intro
print('hi! welcome to this program')
print('you can put the number in mg per kg of the complete dosis per kg')
print('for example, isotretinoin should be 150mg per kg')
print('the program will send you the estimate of days of treatment')

# the doctor puts the number
medication = input('put the name of the drug here: ')
dose_per_kg = int(input('put here the dose per kg of body weight: '))
weight_in_kg = int(input('put the weight in kg of your patient: '))
pill_dose = int(input('put the normal dose of the pill in mg: '))

def total_treatment(dose, kg, pillnum): #calculate the total mg for a person
    total_of_mg = dose * kg
    days = round(total_of_mg / pillnum)
    print(f'your patient should be takin {medication} for {days} days')
    return days #now the doctor knows how many days the treatment should take


days = total_treatment(dose_per_kg, weight_in_kg, pill_dose)

#were gonna make sure the patient or the doctor knows
# how many days are left until the treatment ends.
print('now we can know when this is gonna end \nput the date of the start,\nso, print with numbers')
y = int(input('year: ')) #the parameters of start
m = int(input('month (you dont need put 0): ')) # :)
d = int(input('day: '))

# im lazy so i want a function to bring the date the user put!
def get_date(year, month, day):
    date = datetime.date(year, month, day)  #now we know the date the user put here!
    return date

start_treatment = get_date(y, m, d) #date of start!

def end_of_treatment(start, days): #now we need to know when this is gonna end!
    date_of_end = start + datetime.timedelta(days=days)
    return(date_of_end)

date_end_treatment = end_of_treatment(start_treatment, days)
print(f'you end this in {date_end_treatment}')

#we already have the start and end, we can tell the user how many days 
#have left to finish the treatment

#an if statement is gonna help us to make this more easy!
answer = input('today is the first day of your treatment? (yes or no):  ')
if answer == 'yes':
    print(f'you have {days} days left haha, have fun!')
else:
    print('ok, put the date of today, just like the start!')
    y2 = int(input('year: '))
    m2 = int(input('month (you dont need put 0): '))
    d2 = int(input('day: '))
    today_treatment = get_date(y2, m2, d2)
    days_left = date_end_treatment - today_treatment
    print(f'you have {days_left.days} days left! you can do it!')







