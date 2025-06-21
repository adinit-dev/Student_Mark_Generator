#--------------------------------------------------------------------------
#Student Mark Report Generator -Python
#-----------------------------------------‐--------------------------------

#Store all student data

student_mark= [ ]

#----------------------------------------------------------------‐--------
#   ◇ Function : Enter Student Data
#----------------------------------------------------------------‐--------

def enter_student_data( ):
	student_name = input("enter name: ")
	roll_num = int(input("enter roll num: "))
	phy_mark = int(input("enter phy mark: "))
	chem_mark = int(input("enter chem mark: "))
	math_mark = int(input("enter math mark: "))
	
#Calculating Total Mark, Average,Percentage
	total= phy_mark + chem_mark + math_mark
	
	average = total /3
	
	ratio= total / 300
	percentage = ratio * 100
	
#Assigning Grade based on Pecentage
	
	if percentage >=90:
		Grade ="A+"
	elif percentage >=80 and percentage <90:
		Grade ="A"
	elif percentage >=70 and percentage <80:
		Grade ="B+"
	elif percentage >=60 and percentage <70:			Grade ="B"
	elif percentage >=50 and percentage <60:
		Grade ="C+"
	elif percentage >=40 and percentage <50:
		Grade ="C"
	else:
		Grade ="D"

#Creating Student Record Dictionary
	
	student_record = {
		"name": student_name,
		"roll num" : roll_num,
		"mark" : {
				"phy" : phy_mark,
		 	   "chem" : chem_mark,
			    "math" : math_mark
		},
		"total" : total,
		"percentage" : percentage,
 	   "Grade" : Grade
	}
	return student_record

n = int(input("enter no of student: "))

for i in range(n):
	
	student_mark.append(enter_student_data())
	
#----------------------------------------------------------------‐--------
#◇ Function: View Single Report
#----------------------------------------------------------------‐--------

def view_student_result( ):
	roll_num =int(input("enter student's roll num: "))
	found = False
	for record in student_mark:
		if roll_num == record["roll num"]:
			print("\n=====Student Report=====\n")
			print("Name:		",record["name"])
			print("Roll num:	",record["roll num"])
			print("\n-----------Marks------------\n")
			print("Physics:	",record["mark"]["phy"])
			print("Chemistry:	",record["mark"]["chem"])
			print("Maths:		",record["mark"]["math"])
			print("----------------------------------------------------------------")
			print("Total Mark:	",record["total"])
			print("Percentage:	",record["percentage"])
			print("Grade:		",record["Grade"])
			print("\n=====================\n")
	
			found = True
			break
	if not found:
			print("student record not found")

#----------------------------------------------------------------‐--------
# ◇ Function : View all Report
#----------------------------------------------------------------‐--------

def view_all_reports( ):
		
	for record in student_mark:
			print("\n=====Student Report=====\n")
			print("Name:		",record["name"])
			print("Roll num:	",record["roll num"])
			print("\n-----------Marks------------\n")
			print("Physics:	",record["mark"]["phy"])
			print("Chemistry:	",record["mark"]["chem"])
			print("Maths:		",record["mark"]["math"])
			print("----------------------------------------------------------------")
			print("Total Mark:	",record["total"])
			print("Percentage:	",record["percentage"])
			print("Grade:		",record["Grade"])
			print("\n=====================\n")

#----------------------------------------------------------------‐--------
#◇ Function : Save to file
#----------------------------------------------------------------‐--------		
def save_to_file( ):
	with open("student_report.txt","w") as f:
		for record in student_mark:
			f.write("\n=====Student Report=====\n")
			f.write(f"Name:  {record['name']}\n")
			f.write(f"Roll num:  {record['roll num']}\n")
			f.write(f"-----Marks-----\n")
			f.write(f"Physics:  {record['mark']['phy']}\n")
			f.write(f"Chemistry: {record['mark']['chem']}\n")
			f.write(f"Maths:{record['mark']['math']}\n")
			f.write(f"Total: {record['total']}\n")
			f.write(f"Percentage: {record['percentage']}\n")
			f.write(f"Grade: {record['Grade']}\n")
			f.write("====================\n\n")
	
#----------------------------------------------------------------‐--------
#◇ Menu 
#----------------------------------------------------------------‐--------
			
print("\n=====Student Mark Report Menu=====\n")
while True:
	print("1. View individual Student Result")
	print("2. View All result")
	print("3.Save to file")
	print("4.exit")

	choice = int(input("enter your choice: "))
	if choice == 1:
		view_student_result( )
	elif choice == 2:
		view_all_reports( )
	elif choice == 3:
		save_to_file( )
	elif choice == 4:
		print("Exiting....Thankyou")
		break
	else:
		print("Re-enter choice")
