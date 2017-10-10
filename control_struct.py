counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

for item in range(5):
    print(item**2)

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])