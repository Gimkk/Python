#task8-9
messages = ["abc", "xyz", "hello word", "love python"]
messages2 = ["abc", "xyz", "hello word", "love python"]
sent_messages = []
sent_messages2 = []

def display_message(messages):
    print("---Display messages---")
    for message in messages:
        print(f"\t{message}")

display_message(messages)

#task8-10
print("\n")

def send_messages(messages, sent_messages):
    print("---sending messages---")
    while messages:
        current_message = messages.pop()
        print(f"\tSending message '{current_message}'")
        sent_messages.append(current_message)

send_messages(messages,sent_messages)
print(sent_messages)

#task8-11
def send_messages2(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop())
print("Current messages2 list")
display_message(messages2)
send_messages2(messages2[:],sent_messages2)
print("messages2 list after sent")
display_message(messages2)
print("messages in sent_messages2 list")
display_message(sent_messages2)