import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')


name = [letter.upper() for letter in input("What is the name you want to encode?: ")]

text = []

for letter in name:
    for (index, row) in df.iterrows():
        if row.letter == letter:
            text.append(row.code)


print(text)
