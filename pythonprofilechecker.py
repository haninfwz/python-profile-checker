print("Python profile  checker")
name= input ("Enter your name:")
age= int(input("Enter your age;"))
GPA=float(input("Enter your GPA(0-5):"))
field=input("Enter your field of interset:")
graduated=input("Have you graduated(yes or no):")
print(name,age,GPA,field,graduated)
if age<25 and GPA>=3.5 and graduated=="yes":
    print("You are eligible for a scolarship.")
elif age<30 and GPA>=2.5:
    print("You are eligible for an intership.")
else :
    print("Apply again later:") 
