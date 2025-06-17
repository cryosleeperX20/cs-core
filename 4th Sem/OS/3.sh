
#!/bin/bash
# Write a shell script to generate marksheet of a student. Take 3 subjects, calculate and display
# total marks, percentage and Class obtained by the student.


echo "Enter the marks of 1st Subject: "
read -r m1 
echo "Enter the marks of 2nd Subject: "
read -r m2
echo "Enter the marks of 3rd Subject: "
read -r m3

total=$((m1+m2+m3))
percentage=$(echo "scale=2; $total/3" | bc)
echo "Total marks: $total"
echo "Percentage: $percentage"

# Output
# sh 3.sh
# Enter the marks of 1st Subject:
# 90
# Enter the marks of 2nd Subject:
# 75
# Enter the marks of 3rd Subject:
# 65
# Total marks: 230
# Percentage: 76.66
