S = input()

upper_count = sum(1 for char in S if char.isupper())
lower_count = sum(1 for char in S if char.islower())

if upper_count > lower_count:
    text = S.upper()
else:
    text = S.lower()

print(text)