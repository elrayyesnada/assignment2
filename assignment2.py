# conditions basic assignment:
math_mark= float(input("enter math mark: "))
science_mark= float(input("enter science mark: "))
history_mark= float(input("enter history mark: "))
geography_mark= float(input("enter geography mark: "))
english_mark= float(input("enter english mark: "))
if math_mark>=50:
    print("the student passed in math course")
else:
    print("the student failed in math course")
if science_mark>=50:
    print("the student passed in science course")
else:
    print("the student failed in science_mark")
if history_mark>=50:
    print("the student passed in history course")
else:
    print("the student failed in history course")
if geography_mark>=50:
    print("the student passed in geography course")
else:
    print("the student failed in geography course")
if english_mark>=50:
    print("the student passed in english course")
else:
    print("the student failed in english course")        
total_marks=math_mark+science_mark+history_mark+geography_mark+english_mark
average_marks=(total_marks/5)
print(average_marks)
if average_marks>=85:
    print("final grade is excellent")
if 84>=average_marks>=75:
    print("final grade is very good")
if 74>=average_marks>=65:
    print("final grade is good")
if 64>=average_marks>=50:
    print("final grade is pass")
if 50>average_marks:
    print("final grade is fail")
if (average_marks>=85 and math_mark >= 80) or (average_marks< 85 and math_mark >= 90):
    print("the student can join the compitition")
else:
    print("the student can not join the compitition")
