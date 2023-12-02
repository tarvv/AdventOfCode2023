#this answer won't work correctly because I interpretted the rules to mean that each string digit is replaced by it's int starting at the beginning of the line
#e.g., line "eightwo". I say becomes "8wo", so value is 88. AoC2023 says it has value 82
#due to my annoyance of the vague rules, I'm posting this 'incorrect' code
import re

def strToInt(s):
    return {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}[s.group(0)]

total = 0
with open('../../../inputs/01') as f:
    for line in f:
        line = line.strip()
        line = re.sub(r'((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))', strToInt, line)
        first = re.search(r'\d', line)
        last = re.search(r'(\d)\D*$', line)
        if first and last:
            total = total + int(first.group() + last.group()[0])

print(total)
