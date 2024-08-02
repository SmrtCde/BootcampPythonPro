
line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]

map = [line1, line2, line3]
print("Hiding your treasure in the map below: ")
position = input("Where do you want to hide your treasure? ")
position = position.lower()
letter = position[0].lower()
number = position[1]
col = ["a","b","c"]
letter_index = col.index(letter)
num_index = int(number)-1
map[num_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")