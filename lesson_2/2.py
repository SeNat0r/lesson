people = [
    ['Иван',10,168],
    ['Мария',20,178],
    ['Григорий',13,216],
    ['Ирина',16,196],
    ['Кирилл',27,170]
]
i = 0
count = 0
# while True:
#     if i == len(people):
#         break
#     man = people[i]
#     if man[1] > 15:
#         count += 1
#     i += 1
# print(count)
count = 0
rost = 0
for man in people:
    if man[1] > 15:
        count += 1
    rost += man[2]
print(count)
print(rost / len(people)
      )