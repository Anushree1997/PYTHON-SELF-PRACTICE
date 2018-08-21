
Problem Statement

Ideal Solution

For each of the statements displayed below, write the code that will display the required result for the given dictionary.

villians={1:"magneto", 2:"Joker", 3:"Doctor Doom", 5:"Lex Luthor", 9:"Green Goblin", 6:"Loki"}

1. Display the length of the dictionary.

2. Display the key which has the least value.

3. Display the value of the key 9 as well as delete it simultaneously.

4. Display all the values in dictionary.

5. Delete all the elements in the dictionary while retaining the empty object.

>>> villians={1:"magneto", 2:"Joker", 3:"Doctor Doom", 5:"Lex Luthor", 9:"Green Goblin", 6:"Loki"}

>>> len(villians)

6

>>> min(villians)

1

>>> villians.pop(9)

'Green Goblin'

>>> villians.values()

dict_values(['magneto', 'Joker', 'Doctor Doom', 'Lex Luthor', 'Loki'])

>>> villians.clear()

>>> villians

{}

