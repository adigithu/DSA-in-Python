file=open('youtube.txt', 'w')

try:
    file.write('Adi and class 12')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Adi is with her')