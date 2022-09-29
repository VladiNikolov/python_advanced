input_line = input().split()
input_line = [int(i) for i in input_line]

positive_numbers = []
negative_numbers = []

for element in input_line:
    if element > 0 :
        positive_numbers.append(element)
    else:
        negative_numbers.append(element)

print(sum(negative_numbers))
print(sum(positive_numbers))
if abs(sum(negative_numbers)) > (sum(positive_numbers)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
