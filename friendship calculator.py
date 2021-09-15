alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ' '
score = 0

message = input('Enter the names of two people: ')

for character in message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    print(newPosition)
    score += newPosition
    
    


print('Your friendship score is: ' + str(score))