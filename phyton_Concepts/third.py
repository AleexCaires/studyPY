# Ternary operator

score = 57
if score > 90:
  grade = 'A*'
elif score > 50:
  grade = 'pass'
else:
  grade = 'fail'

# grade = 'pass

# ^ a normal if-elif-else block

score = 57
grade = 'A*' if score>90 else 'pass' if score>50 else 'fail'

# grade = 'pass'

# ^ we can condense the if-elif-else block into ONE line using the ternary operator.
