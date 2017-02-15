#Create list elements
grades = []
maxLength = int(input("Enter the class strength:"))
print ("Enter the scores:\n")

def print_grades(grades):
    while len(grades)<maxLength:
         item = input()
         grades.append(item)
    return grades
    for grade in grades:
        print (grade)
    
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += int(grade)
    return total
   
def grades_average(grades):
     average= float(grades_sum(grades))/ max(len(grades),1)
     return average

def grades_variance(scores):
    average= grades_average(scores)
    variance= 0
    for score in scores:
        variance+= ((int(average) - int(score))**2)
    return variance/max(len(scores),1)

def grades_std_deviation(variance):
     return variance**(0.5)

variance = grades_variance(grades)     
print(print_grades(grades))
print(grades_sum(grades))
print (grades_average(grades))
print (grades_variance(grades))
print (grades_std_deviation(variance))
