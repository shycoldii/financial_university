our_dictionary={'g4': ['f5', 'e6','r5']}
code_now='g4'
chores = our_dictionary[code_now]
chores_one = chores[0:len(chores):2]
chores_two = chores[1:len(chores):2]
print(chores_two)
print(chores_one)