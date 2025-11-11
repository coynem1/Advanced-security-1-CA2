CIPHER_TEXT = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"

# English alphabet letter frequency
LETTER_FREQ = {
    "E": 12.02, "T": 9.10,  "A": 8.12,  "O": 7.68,  "I": 7.31,
    "N": 6.95,  "S": 6.28,  "R": 6.02,  "H": 5.92,  "D": 4.32,
    "L": 3.98,  "U": 2.88,  "C": 2.71,  "M": 2.61,  "F": 2.30,
    "Y": 2.11,  "W": 2.09,  "G": 2.03,  "P": 1.82,  "B": 1.49,
    "V": 1.11,  "K": 0.69,  "X": 0.17,  "Q": 0.11,  "J": 0.10,
    "Z": 0.07
}
PERCENT = 100   # For calculating
FREQ_ORDER = [] # Updates later

# Sorts in order of value
def sortDict(d: dict):
    return sorted(d.keys(), key=lambda l: d[l], reverse=True)

# Finds letter frequency of string
def calcFrequency(text: str):
    result = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0,
        "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
        "K": 0, "L": 0, "M": 0, "N": 0, "O": 0,
        "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
        "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0,
        "Z": 0
    }

    # loop through and add per occurance
    for c in text:
        if c not in result:
            return
        result[c] += 1 
    
    # divide by len and by 100 for percent


    return result

# Sorts in case values change
FREQ_ORDER = sortDict(LETTER_FREQ)

print(calcFrequency(CIPHER_TEXT))