# https://www.hackerrank.com/challenges/non-divisible-subset/problem

S = [770528134, 663501748, 384261537, 800309024, 103668401,
     538539662, 385488901, 101262949, 557792122, 46058493]
# S = [1, 7, 2, 4, 5]
k = 5


all_tuples = []
for i in range(0, len(S)):
    for j in range(i + 1, len(S)):
        this_tuple = tuple([S[i], S[j]])
        if this_tuple not in all_tuples:
            all_tuples.append(this_tuple)

# print(all_tuples)

non_divisible_tuples = list(filter(lambda item: (
    item[0] + item[1]) % k != 0, all_tuples))

print(non_divisible_tuples)

unique_items = []

for t in non_divisible_tuples:
    for m in range(2):
        print("Checking " + str(t[m]))
        if len(unique_items) == 0:
            print("fist append")
            unique_items.append(t[m])
        else:
            if t[m] not in unique_items:
                print(str(t[m]) + " is not in unique_elements")
                addItem = True
                # for n in range(0, len(unique_items)):
                #     print("Adding " + str(t[m]) +
                #           " with " + str(unique_items[n]))
                #     if (unique_items[n] + t[m]) % k == 0:
                #         addItem = False
                #         break
                if addItem == True:
                    print("A D D I N G " + str(t[m]))
                    unique_items.append(t[m])
            else:
                print(str(t[m]) + " is in unique_elements")

print(list(unique_items))
