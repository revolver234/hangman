import string
import random

print("Dont spell boooooo")
print("how long ")
x = input()
print(x)
x = int(x)
y = range(x)
z = ""
for n in y:
    z = z + "_"
print(" here is the the word: " + z)
# Randomly choose a letter from all the ascii_letters
h = ""
for m in y:
    randomLetter = random.choice(string.ascii_letters)
    h = h+ (randomLetter)
z = (h.lower())
print(z)
r = "b"
d = "boooooo"
while 1:
    w = input()
    if w in z:
        print("goog")
    elif w not in z:
        r = r + "o"
        print(r)
        if r == d:
            print("you died so whats the word")
            break
e = input()
if e == z:
    print("goog job")
elif e != z:
    print("you smell")
