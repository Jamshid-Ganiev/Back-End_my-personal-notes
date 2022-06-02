# FOR LOOPS // tuple unpacking
my_pairs = [(1,2), (3,4), (5,6)]

for tup1,tup2 in my_pairs:
    print(tup1)
    print(tup2)

#LIST COMPREHENSION
x = [1,2,3,4]
output = []

for num in x:
    output.append(num**3)
print(output)

#ANOTHER METHOD OF THE STUFF ABOVE
out = [num**3 for num in x]
print(out)
