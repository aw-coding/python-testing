### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #there should be a double equals (==) to check for equality.
      return True
    else #there should be a colon after the word 'else'
      return False
   

  dif highest_card(self, card1 card2): #'dif' here is misspelled. Should be 'def'. And there should be a comma after card1
  if card1.value > card2.value:
    return card   #this should be 'card1', there is no card called 'card'
  else:
    return card2
  


def cards_total(self, cards):
  total      #this should be declared as a data type (eg 'int total') or by assigned a value.
  for card in cards:
    total += card.value
    return "You have a total of" + total  #this line should be indented as much as line 37. 
  
```
