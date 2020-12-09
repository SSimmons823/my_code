#!/usr/bin/env python3

message = 'Your score is an '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your test score?"))

# if input value was within letter grade range
if score >= 90:
    message = message + 'A. Congradulations.'
elif score >= 80:
    message = message + 'B. Congradulations.'
elif score >= 70:
    message = message + 'C. Study harder.'
elif score >= 60:
    message = message + 'D. Review the test material.'
elif score <= 59:
    message = message + 'F. You Failed. Review the test material.'
else:
    message = message + 'Not a valid score.Please enter a valid score between 0-100.'
print(message)

