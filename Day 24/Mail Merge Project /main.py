with open("./Input/Names/invited_names.txt") as f:
    file = f.readlines()
with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.read()
    for name in file:
        stripped = name.strip()
        l = letter.replace("[name]", stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt", mode="w") as w:
            w.write(l)


