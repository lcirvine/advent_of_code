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
- Finally, I saved the neighbors that met the criteria in a list. Any gears that had 2 neighbors were multipled together to find the result

#### Tags
- regex
- regex finditer to find multiple matches
- creating mapping with X Y coordinates

## Day 4
- Parsing - The data is given to you as 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'. I used the string function split and regex to separate that into
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