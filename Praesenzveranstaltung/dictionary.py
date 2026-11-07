# Iteration von list und dict
liste = [1, "a", 2.5]
print("Elemente in Liste:")
for elem in liste:
    print(elem)

dictionary = {}
dictionary["hier"] = 1
dictionary["steht"] = "a"
dictionary["etwas"] = 2.5
print("Elemente in Dictionary:")
for elem in dictionary:
    print(elem, dictionary[elem])
