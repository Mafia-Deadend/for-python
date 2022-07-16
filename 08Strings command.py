#These Commands re used for the string only.They are known as sting functions
#--->string declaration<----
story = "Once Upon a time there was a boy named hammad and he was not good at all  but then everything changed"

#------>String Function------<
print(len(story))      #<=== count the number of character used in a string====>
print(story.endswith("changed"))  #<=====It shows either the string ends with the given character or not
print(story.count("at"))   #<===It count the number of given character in a whole string
print(story.find("changed")) # <===finds the given character in a string occured first in the string
print(story.replace("hammad", "CodeWithHammad"))#<=it replaces all the occurances of the word with the usergiven  word

