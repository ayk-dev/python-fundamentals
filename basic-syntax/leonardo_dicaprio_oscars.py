oscar_number = int(input())
message = ''

if oscar_number == 88:
    message = 'Leo finally won the Oscar! Leo is happy'
elif oscar_number == 86:
    message = 'Not even for Wolf of Wall Street?!'
elif oscar_number < 88 and oscar_number != 86:
    message = 'When will you give Leo an Oscar?'
elif oscar_number > 88:
    message = 'Leo got one already!'

print(message)
