# Python Projects: Friendship Calculator 🐍

Python Script <br>
This repo contains python code that generates a friendship score based on the names you enter. <br>
Run the code.

Python
```python
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
```

Output
```s
Your frendship score is: 60
```
