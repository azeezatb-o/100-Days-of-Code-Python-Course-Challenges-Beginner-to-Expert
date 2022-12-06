with open("file1.txt") as f1:
    nums1 = f1.readlines()
with open("file2.txt") as f2:
    nums2 = f2.readlines()

result = [int(num) for num in nums1 if num in nums2]

# Write your code above 👆

print(result)


