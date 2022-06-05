messages_sent = int(input())
message = ''
for _ in range(messages_sent):
    current_message = int(input())
    if current_message == 86:
        message = 'How are you?'
    elif current_message == 88:
        message = 'Hello'
    elif current_message < 88 and current_message != 86:
        message = 'GREAT!'
    else:
        message = "Bye."
    print(message)
print()
