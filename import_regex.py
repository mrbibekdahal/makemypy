import re

txt = "I am doing Python"

x = re.search("^I.*Python$", txt)

if x:
    print("Match found!")
else:
    print("No match found.")
