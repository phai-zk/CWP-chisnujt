arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for i in range(len(arr)):
    is_dup = False
    for j in range(len(arr)):
        if arr[i] == arr[j] and i != j:
            is_dup = True
            break
    if not is_dup:
        new_arr.append(arr[i] + 2)

print(arr)
print(new_arr)