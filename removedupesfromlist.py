my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nodups = []
for i in range(len(my_list)):
    if my_list[i] not in nodups:
        nodups.append(my_list[i])
my_list[:]=nodups[:]

print("The list with unique elements only:")
print(my_list)