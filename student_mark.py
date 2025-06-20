#Student Mark Report Generator

#Taking Input

student_name = input("enter name:")
phy_mark = int(input("enter phy mark:"))
chem_mark = int(input("enter chem mark:"))
math_mark = int(input("enter math mark:"))

record = {
	"name": student_name,
	"mark" : {
			"phy" : phy_mark,
	        "chem" : chem_mark,
	        "math" : math_mark
	}
}

student_mark =[ ]
#Total marks
total= phy_mark + chem_mark + math_mark
print ("Total Marks:", total)
#Average mark
average = total /3
print("Average:", average)
#Percetage
ratio= total / 300
percentage = ratio * 100

print("Percentage:",percentage)

record["total"] = total
record["average"] = average
record["percentage"] = percentage
 
student_mark.append(record)

