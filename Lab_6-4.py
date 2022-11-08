# Author: PCL 11/8/22

#creating a list of subjects I have studied at Prep and printing it
subjects = ["Economics","AP Chemistry","Computer Progamming"]
print(subjects)

#adding another subejct to the end of the subjects list
subjects.append("Drama & Film")
print(subjects)

#finding and printing the index of AP Chemistry in the subjects list
print("The index of AP Chemistry is "+ str(subjects.index("AP Chemistry")))

#sorting the subjects lists alphabetically
subjects.sort()
print(subjects)

#creating a copy of the subjects list and reversing said copy, then printing the result
subjects2 = subjects
subjects2.reverse()
print(subjects2)