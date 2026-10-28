text="hello python"
print(text .upper())
text="HELLO PYTHON"
print(text .lower())
text="   hello python   "
print(text .strip())
text="i like java"
print(text .replace("java", "python"))
text="apple,banana,cherry"
print(text.split(","))
words=['hello', 'world']
print(".".join(words))
fruits=["apple", "banana", "cherry", "kiwi"]
fruits.append("persimon")
print(fruits)
nums=[10, 20, 30, 40, 50]
secondlast=nums.pop(3)
print(secondlast)
print(nums)
nums=[8,6,7,5,4,2,3,1]
nums.sort()
print(nums)
user={"name":"fatima", "age":19}
print(user.keys())
print(user.values())
print(user.items())
print(user.get("city", "not found"))
user.update({"city":"delhi"})
print(user)
nums={1,2,3,4,5}
nums.remove(3)
print(nums)
set1={1,2,3,}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
numbers=(1,2,3,1,2,2,4,2,7,2)
print(numbers.count(2))
numbers=(10,20,30,40,50)
print(numbers.index(10))
print(numbers.index(40))