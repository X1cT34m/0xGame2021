from flag import *

length = len(flag)
arr = []
enc = [238, 257, 150, 137, 167, 169, 184, 193, 210, 147, 219, 128, 140, 135, 185, 242, 204, 128, 132, 159, 222, 173, 226, 159, 207, 169, 154, 156, 216, 139, 168, 187, 220, 237, 207, 187, 218, 138, 218, 178, 246, 239, 246, 241]
for i in range(length):
    arr.append(ord(flag[i]))
for i in range(0,16):
    for j in range(0,length):
        arr[j] += enc[j]
        enc[j] += enc[j]
    enc = enc[::-1]
print(arr)

# for i in range(0,16):
#     enc = enc[::-1]
#     for j in range(0,length):
#         enc[j] = enc[j] // 2
#         arr[j] -= enc[j]
# for i in range(length):
#     print(chr(arr[i]), end = "")