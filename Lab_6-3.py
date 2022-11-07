# Author: PCL 11/7/22

#creating list of colors
colors = ["blue","cyan","red","pink"]
print(colors)

#adding 3 new colors to the end of the list
colors.extend(["yellow","green","purple"])
print(colors)

#using a different method than the previous one to add another colors ot the list
colors.append("orange")
print(colors)

#adding another color to specific point in the list
colors.insert(3,"black")
print(colors)

#creating a copy of the colors list named colors2 and removing one color
colors2 = colors
colors2.remove("pink")
print(colors2)