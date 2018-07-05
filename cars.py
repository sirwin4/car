showroom = set()
showroom.update(("a", "car", "Added", "done"))
print(len(showroom))
showroom.add("a")
print(showroom)
showroom.discard("a")
print(showroom)

junkyard = set()

junkyard.update(("added", "Added", "new", "set", "car"))

print(showroom.intersection(junkyard))

showroom.union(junkyard)

print(junkyard)
