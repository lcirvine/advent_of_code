# Advent of Code 2023 Notes

https://adventofcode.com/2023

## Day 1
### Part 1

- Used regex to find all digits in string
- Added the strings of digits ('1' + '2' = '12' rather than 1 + 2 = 3), then converted to an integer 

### Part 2

- Used regex to find either digits or words for numbers (i.e. 'one', 'two', etc.) 
    ```python 
        pat = r"(?=(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))"
    ```
- Regex pattern required positive lookahead ```?=``` to find overlapping matches (i.e. 'oneight')
- ```re.findall``` returned a list of tuples for each group, flattened with nested list comprehension
  ```python
  vals = [num for group in re.findall(pat, text_line) for num in group if num]
  ```
- Mapped word for number to digit (as a string) ```{'one': '1', 'two': '2'...}```

#### Tags
- regex
- regex with multiple groups 
- regex with positive lookahead
- nested list comprehension

# Day 2
## Part 1
- To find which games are possible, you only need to find the max number of cubes of each color
- Used regex to find the number of cubes for each color and the game ID

## Part 2
- Most of the work was already done since I already found the max number for each color
- All I needed to do in part 2 was multiply those numbers together for each game

#### Tags
- regex

## Day 3
- When parsing the data I created 
  - a list of special characters - special characters were anything that is not a digit, '.', or new line character
  - a character map - keys were (x, y) coordinates and values were characters. I didn't end up using the character map that much, but could be used to find the character in any location (i.e. ```char_map[(2, 3)] = '$'```)
  - a list of special character coordinates - all coordinates where the value was a special character
  - a list of gear coordinates - in pt 2 gears were given as '*' so I saved those coordinates in a list
- Today's code could be cleaned up a bit, I think this could have been done in a simpler way
### Part 1
- I went through each row to find all the digits in that row
  - ```[mo for mo in re.finditer(r"(\d*)", row) if mo.group()]```
  - ```re.finditer()``` to find all matches in the row
  - ```(\d*)``` is greedy, will return all digits in the number
- Then I found the 'neighbors' (the coordinates around the number)
- Finally checked if any of the neighbors were special characters
### Part 2
- In part 2, I started with the gear coordinates 
- Then looked at the row above, on and below the row with the gear
- Then found the digits in that row
- Then checked if the x coordinate for that digit is on or within one of the gear's x coordinate
- Finally, I saved the neighbors that met the criteria in a list. Any gears that had 2 neighbors were multiplied together to find the result

#### Tags
- regex
- regex finditer to find multiple matches
- creating mapping with X Y coordinates

## Day 4
- Parsing - The data is given to you as "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53". I used the string function split and regex to separate that into
  - card ID - split by ':', then used regex to find the ID number
  - winning numbers - split by '|', winning numbers would be first group
  - my numbers - the numbers I had on the scratchcard would be in the 2nd group
- Data structure - I tried a few different ways to organize the data. I figured out that all we really need is the number of wins for each card and, for part 2, which scratchcards would be won by that card. I created a dictionary with card ID as the key and values for number of cards, how many cards that scratchcard would win, and what cards would be won by that scratchcard.

### Part 1
- The main thing you need to know for part 1 is how many wins were there for each scratchcard
- The number of wins was already in my dictionary, so I looped through to find the number of wins, then find the number of points earned. 

### Part 2
- Created a recursive function to increment the number of cards
  ```python 
    def increment_winners(card_id):
      for card_won in card_info[card_id]['wins_cards']:
          card_info[card_won]['num_cards'] += 1
          increment_winners(card_won)
    ```

#### Tags
- recursion
- recursive functions
- data structure
- regex
- sets
- set intersection

## Day 5
I found this puzzle really difficult. 

### Part 1
- Even parsing this was difficult. I created a dictionary for the almanac which had seeds, then each mapping. The keys for each mapping were tuples with the ranges of values for that mapping.
- The almanac dictionary should already be in order since I'm using python 3.10. However, instead of relying on that I created a tuple with each step. That way I could find the next step by the index in the tuple.
- After creating the almanac, I created a recursive function to fetch the value for the next step (the destination).

### Part 2
- The number of seeds in each range is too large to go one-by-one and find the mappings like I did in part 1
- I'm still trying to find the clever way to do this. Perhaps if I start at the end and work my back? The puzzle wants the minimum location. Could I find the minimum location, then work backward to find the seed?

#### Tags
- data structure
- recursive functions

## Day 6
Like the previous day, part 2 of this puzzle is difficult and involves large numbers.

### Part 1
- *For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.* So you 'charge up' your speed at the beginning of the race, then continue at that speed until time expires.
  - ```distance = (time - speed) * speed```
- The numbers were small enough that I could go through each speed in the range to see if it would beat the distance record
- Used a list comprehension to find all speeds in range of times which would beat the distance record
- Used ```np.prod``` to find the product of a list of values

### Part 2
- I used the 'brute force' approach which made part 2 very similar to part 1. 
  - The values are much larger than part 1, so it will take longer to solve.
  - However, it didn't take *that* long to run, much less time than trying to brute force part 2 from day 5. 
- Removed the list comprehension from part 1. Part 2 just needs the total count of ways to win. I don't want to store a list with millions of numbers just to later get the length of that list.  
- There is a better way to solve this, but I haven't figured it out yet. Here are my thoughts on other solutions:
  - I found the derivative of the equation, then set it equal to 0 to find the max speed. Basically, you speed up for half the time. 
    ``` 
        d = (t - s) * s
        d = t*s - s**2
        d' = t - 2s
        d'' = -2
        speed to get max distance = t/2
    ```
  - What speed do I need to go in order to beat that distance record?
  - I've been using 'speed' in these equations. Speed is really just ```distance / time``` though. Does that help?
- Later I will look at other solutions to see what I can learn from them

#### Tags
- math
- numpy
- regex
- list comprehension 

## Day 7

### Part 1
- I assigned a letter value to each card in order of the card's value. That way I can sort alphabetically. 
   ```python
  from string import ascii_uppercase
  card_vals = dict(zip('AKQJT98765432', ascii_uppercase))
  ```
  - 'KKA77' should come before 'KK7AA' since A has a higher value than 7
  - When I map the card values to letters, these cards would become 'BBAHH' and 'BBHAA' and will sort correctly
- Used ```Counter``` from Collections to get the count for each card in the hand
- From ```Counter``` I can find the number of unique cards and maximum value of a single card. That allows me to classify each hand.

| **Hand Type** | **Unique Cards** | **Max Value of Single Card** |
|---------------|------------------|------------------------------|
| high card     | 5                | 1                            |
| pair          | 4                | 2                            |
| two pair      | 3                | 2                            |
| 3 of a kind   | 3                | 3                            |
| full house    | 2                | 3                            |
| 4 of a kind   | 2                | 4                            |
| 5 of a kind   | 1                | 5                            |

- I needed to sort the hands by 
  1. number of unique cards ascending 
  2. max value of single card descending
  3. alphabetical value I assigned to the cards to sort
- Python retains previous sorting which allows me to do multiple sorts, starting with the least important. This is really helpful when sorting by multiple items, some ascending, some descending. 
```python 
    poker_round = sorted(poker_round, key=lambda x: x[4])                   # sort by card_sort, ascending
    poker_round = sorted(poker_round, key=lambda x: x[3], reverse=True)     # sort by max value of card, descending
    poker_round = sorted(poker_round, key=lambda x: x[2])                   # sort by number of unique cards, ascending
```

### Part 2
- In part 2, 'J' is now a wildcard i.e. it can be used as any card. That means that:
  - If you have a J in your hand, the number of unique cards should decrease by 1 and 
  - For each J in your hand, the max value of a single card should increase by 1
- Also, J is now the least valuable card, so need to adjust the sorting
  - ```card_vals = dict(zip('AKQT98765432J', ascii_uppercase))```
- One tricky part is that there can be hands with all jokers 'JJJJJ'. That caused me to 
  - Add 0 to the list in the line below so the list would not be empty and throw an error when finding max 
    ```python 
    max_value_of_card = max([val for card, val in card_count.items() if card != 'J'] + [0])
    ```
  - Ensure that the unique_card_count is at least 1 
    ```python
    unique_card_count = max(unique_card_count, 1)
    ```

#### Tags
- Counter
- complex sorting
- sort by multiple values 
- lambda