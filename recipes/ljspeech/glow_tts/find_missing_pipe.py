import pandas as pd

data = pd.read_excel(r'C:\Users\matth\Documents\just_for_fun\coqui_tts\recipes\ljspeech\training_data\metadata.xlsx').to_numpy()
for row in data:
    row = str(row)
    if row.count('|') < 2:
        print(row)