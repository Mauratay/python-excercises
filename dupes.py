#https://edube.org/learn/pe-1/section-summary-3-3-4
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = len([num for num in tup if tup.count(num)>1])

print(duplicates)
