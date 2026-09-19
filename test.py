#birthday = ["January", "8" , "2009"]
#message= (f"I was born in the year {birthday[2]} on the day {birthday[1]} of the month {birthday[0]}")
#print(message)

#siblings = ["Emlio", "Jonh" , "Mohhamed" , "Joe"]
#sibling_ranking = f"my favorite sibling is {siblings[3]}, second is {siblings[1]}, worst ever is {siblings[0]} , {siblings[2]} is fine enough"
#print(sibling_ranking)
#siblings[3] = "joey"
#print(siblings)
#siblings.append("Muhammet")

#grade = [95, 90 , 89 , 85 , 92]
#print((grade[0] + grade[1] + grade[2] + grade[3] + grade[4])/5)
#grade.insert(2, 100)
#print(grade)

activity = ["one","two","three","four","five"]
activity.append("hello")
print(activity)
activity.insert(3,1)
print(activity)
del(activity[1])
print(activity)
del(activity[-1])
print(activity)
y = activity.pop()
print(f"the last word in my list was {y}")
