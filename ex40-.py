note_1 = float(input('What was your grade from the first two months? '))
note_2 = float(input('What was you grade for the second quarter? '))
average = (note_1 + note_2) / 2

if average < 5:
    print('DISAPPROVED')
elif average >= 5 and average <= 6.9:
    print('RECOVERY')
else:
    print('APPROVED')