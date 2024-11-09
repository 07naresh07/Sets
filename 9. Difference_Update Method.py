mySet = {1, 2, 3, 4, 5}
yourSet = {4, 5, 6, 7, 8, 9, 10}
print(mySet.difference_update(yourSet)) #Modifies the Set while difference() alone do not modify set
print(mySet)
