from collections import deque

with open('input') as file:
    content = file.read()

part_1 = 0
part_2 = 0
decryption_key = 811589153


numbers_part_1 = deque(int(line) for line in content.split('\n') if line)
numbers_part_2 = deque(decryption_key * number for number in numbers_part_1)
length = len(numbers_part_1)


def mix(numbers, indices):
    for index in range(length):
        location = indices.index(index)

        numbers.rotate(-location)
        indices.rotate(-location)

        number = numbers.popleft()
        index = indices.popleft()

        numbers.rotate(-number)
        indices.rotate(-number)

        numbers.appendleft(number)
        indices.appendleft(index)

    return numbers, indices


def grove_coordinates(numbers):
    location = numbers.index(0)
    return (numbers[(location + 1000) % length]
            + numbers[(location + 2000) % length]
            + numbers[(location + 3000) % length]
            )


indices = deque(range(length))
numbers_part_1, indices = mix(numbers_part_1, indices)
part_1 = grove_coordinates(numbers_part_1)

indices = deque(range(length))
for χ in range(10):
    numbers_part_2, indices = mix(numbers_part_2, indices)
part_2 = grove_coordinates(numbers_part_2)

print(part_1)
print(part_2)
