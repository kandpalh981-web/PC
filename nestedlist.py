stud=[]
std=int(input("enter number of students:"))
sub=int(input("enter subject number:"))
for i in range(0,std):
    name=str(input("enter name:"))
    marks=[]
    for j in range(0,sub):
      mark=float(input(f"enter marks of sub{j+1}:"))
      marks.append(mark)
    stud.append([name,marks])
final_list=[]
for name,marks in stud:
    total=sum(marks)
    avg=total/len(marks)
    result ="pass" if avg>33 else "fail"
    final_list.append([name,marks,total,avg,result])
print("\nfinal answer in list")
print(final_list)
