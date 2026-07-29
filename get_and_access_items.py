thisdict = {
  "name" : "Abhi",
  "address" :"Asia",
  "age": "30"
}
print(thisdict)

x = thisdict["address"] #access address from dict.
print(x)
y = thisdict.get("address") #access address using .get
print(y)


z = thisdict.keys() #accessing keys from dict
print(z)