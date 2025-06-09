print("Python profile  checker")
name= input ("what's your name?:")
age= int(input("How old your you?:"))
gpa=float(input("Enter your GPA(0-5):"))
field=input("what is your field of interset?:")
graduated=input("Have you graduated?:(yes or no):")
print(name,age,gpa,field,graduated)
if age<25 and gpa>=3.5 and graduated=="yes":
    print("You are eligible for a scolarship.")
elif age<30 and gpa>=2.5:
    print("You are eligible for an intership.")
else :
    print("Apply again later:") 
