class MultipleFunctions():

#list out the items in the list    
    def Subfields():
        lists = ["Machine Learning", "Neural networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for item in lists:
            print(item)

#checks whether the giver number is Odd or Even    
    def OddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print(num,"is Even number")
            message="is Even number"
            return message
        else:
            print(num,"is Odd number")
            message="is Odd number"
            return message

#eligibilty of marriage for male and female according to their age limit    
    def eligible():
        gender=input("your gender")
        age=int(input("your age"))
        if gender=="Male" and age>21:
            print("Eligible")
            message= "Eligible"
        elif gender=="Female" and age>18:
            print("Eligible")
            message= "Eligible"
        else:
            print("Not Eligible")
            message= "Not Eligible"
        return message
    
#Calculate the percentage of your 10th mark
    def percentage():
        Sub1= int(input("Subject1= "))
        Sub2= int(input("Subject2= "))
        Sub3= int(input("Subject3= "))
        Sub4= int(input("Subject4= "))
        Sub5= int(input("Subject5= "))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total :",Total)
        Percentage = (Total/500)* 100
        print ("Percentage :",f"{Percentage}")

#print area and perimeter of triangle
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area = (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2 ")
        print("Area of triangle:", Area)
        
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B1=int(input("Breadth:"))
        Perimeter = H1+H2+B1
        print("Perimeter formula: Height1+Height2+Breadth ")
        print("Perimeter of triangle:",Perimeter)
        return Area, Perimeter