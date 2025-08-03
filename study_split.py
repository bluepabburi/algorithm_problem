text = "apple,banana,grape"

fruits = text.split(",")
print(fruits) # ['apple', 'banana', 'grape']

slicing_fruits = [[f] for f in fruits]  # 리스트안의 변수들을 각각 리스트로 담고싶었음
print(slicing_fruits)
