import pandas as pd

user_text = input("Please type text to be transformed to Morse Code: ").upper()

morse_table = pd.read_csv('morse.csv')

for char in user_text:
    if char in morse_table['letter'].values:
        index_number = morse_table.index[morse_table['letter'] == char]
        print(morse_table.iloc[index_number[0]].values[1])
    else:
        raise ValueError("Only letters and numbers allowed.")
