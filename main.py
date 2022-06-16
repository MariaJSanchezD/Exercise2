'''Create a program in python that creates a list of 30 elements transforming the
input array:
[3, 5, 7, 9, 11, 12, 15, 20, 25]
into:
[0,0,0,1,0,2,0,3,0,4,0,5,6,0,0,7,0,0,0,0,8,0,0,0,0,9,0,0,0,0,0]'''

list = []
positions = [3, 5, 7, 9, 11, 12, 15, 20, 25]

j = 1

for i in range(0,30):
    if len(positions) and i == positions[0]:
        positions.pop(0)
        list.append(j)
        j += 1
    else:
        list.append(0)

print(list)
