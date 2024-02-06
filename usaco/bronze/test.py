record = "A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2"

scores = {'A': 0, 'B':0}
i=0

while i < len(record):
    scores[record[i]] += int(record[i+1]) 
    i += 2
    
print('A' if scores['A'] > scores['B'] else 'B')
