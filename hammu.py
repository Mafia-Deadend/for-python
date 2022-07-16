myDict = { "Hammad" : "sort of owner of this PC",
             "Sajjad" : "His Brother",
             "Hannan" : "His Younger brother",
             "Hannan's age" : "about 12 to 12 yrs",
             "hammad's age"  : 20}
print(myDict["hammad's age"])
myDict["hammad's age"] = 19
print(myDict["hammad's age"])
print(myDict.values())
print(myDict.items())
print(list(myDict.keys()))
updated = {"sajjad's age" : 18,
             "Hammad's Hobby" : "Programming",
             "Hammad's percentage in exams" : 83.0,
             "Is Hammad currently Studying" : True }
myDict.update(updated)
print(myDict.get("Hammad's Hobby")) #prints value associated with "Hammad's Hobby"
# if the value is not present it wont throw a error
