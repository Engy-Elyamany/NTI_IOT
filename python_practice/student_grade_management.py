import math

std_num = int(input("How many students ? "))
std_data= {}
for i in range(std_num):
    std_name = input("student's name : ")
    std_grade = float(input("student's grade : "))
    std_data [std_name]= std_grade

print("\nAll Students : ")
for i in std_data:
    print(f"{i} => {std_data[i]}")

mx = max(std_data.values())
for i in std_data:
    if std_data[i] == mx:
        print(f"\nHighest grade is {std_data[i]} from student {i}")

avg = sum(std_data.values()) / std_num
print(f"\naverage grade {avg}")

for i in std_data:
    if(std_data[i] < 50):
        print(f"\nStudent {i} failed")