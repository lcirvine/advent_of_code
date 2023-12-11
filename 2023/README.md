# 🎅 Advent of Code 2023 🎄


https://adventofcode.com/2023

---
## Day 1 ⛔❄️

[🧩](https://adventofcode.com/2023/day/1 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day1.py "Code")

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

### Tags
- regex
- regex with multiple groups 
- regex with positive lookahead
- nested list comprehension

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
| 😃|😨|

---
# Day 2 🧊

[🧩](https://adventofcode.com/2023/day/2 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day2.py "Code")

## Part 1
- To find which games are possible, you only need to find the max number of cubes of each color
- Used regex to find the number of cubes for each color and the game ID

## Part 2
- Most of the work was already done since I already found the max number for each color
- All I needed to do in part 2 was multiply those numbers together for each game

### Tags
- regex

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
| 😃|😂|

---
## Day 3 ⚙️

[🧩](https://adventofcode.com/2023/day/3 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day3.py "Code")

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

### Tags
- regex
- regex finditer to find multiple matches
- creating mapping with X Y coordinates

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|🤔👌|🤔😕😅|

---
## Day 4 💳

[🧩](https://adventofcode.com/2023/day/4 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day4.py "Code")

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

### Tags
- recursion
- recursive functions
- data structure
- regex
- sets
- set intersection

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|:relaxed:|🤨|

---
## Day 5 🌱

[🧩](https://adventofcode.com/2023/day/5 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day5.py "Code")

I found this puzzle really difficult. 

### Part 1
- Even parsing this was difficult. I created a dictionary for the almanac which had seeds, then each mapping. The keys for each mapping were tuples with the ranges of values for that mapping.
- The almanac dictionary should already be in order since I'm using python 3.10. However, instead of relying on that I created a tuple with each step. That way I could find the next step by the index in the tuple.
- After creating the almanac, I created a recursive function to fetch the value for the next step (the destination).

### Part 2
- The number of seeds in each range is too large to go one-by-one and find the mappings like I did in part 1
- I'm still trying to find the clever way to do this. Perhaps if I start at the end and work my back? The puzzle wants the minimum location. Could I find the minimum location, then work backward to find the seed?

### Tags
- data structure
- recursive functions

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|😢|😭 :rage3: ⌛|

---
## Day 6 🚤

[🧩](https://adventofcode.com/2023/day/6 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day6.py "Code")

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

### Tags
- math
- numpy
- regex
- list comprehension 

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|😃|😥😌 :shipit: |


---
## Day 7 🐫🎴

[🧩](https://adventofcode.com/2023/day/7 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day7.py "Code")

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

### Tags
- Counter
- complex sorting
- sort by multiple values 
- lambda

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|🤓|🙂|

---
## Day 8 👻🗺️

[🧩](https://adventofcode.com/2023/day/8 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day8.py "Code")

### Part 1
- Parsed the input into a string of instructions and a dictionary with the nodes as keys and the value as a tuple with left and right destination nodes
- For part 1, I started at node AAA and cycle through the directions until you end at ZZZ
- You get the destination node from the node_map dictionary created when parsing the data
- One tricky part is that if you get to the end of the instructions without reaching node ZZZ, you start over at the beginning of the instructions. You can overcome that by using modulo.
  ```python
  step % len(instructions)
  ```
- Originally, I found the next node in one line, but refactored it to a function for readability and so that I could use the function in part 2
  ```python
  instr_map = {'L': 0, 'R': 1}
  node_map[current_node][instr_map[instructions[step % len(instructions)]]]
  ```
  ```python 
  def next_node(current_node: str, step: int):
      instr_num = step % len(instructions)
      instr = instructions[instr_num]
      instr_map = {'L': 0, 'R': 1}
      next_node_num = instr_map[instr]
      return node_map[current_node][next_node_num]
  ```

### Part 2
- In part 2 I needed to find how many steps it takes for A nodes (all nodes that end with A) to reach Z nodes (all nodes that end with Z)
- My first attempt at solving part 2 was the 'brute force' approach. However, running that would take a **very** long time.
  ```python 
  def part_2():
      nodes = [n for n in node_map if n.endswith('A')]
      steps = 0
      all_z = False
      while not all_z:
          nodes = list(map(next_node, nodes, [steps for n in nodes]))
          steps += 1
          all_z = all([n.endswith('Z') for n in nodes])
      return steps
  ```
- Instead, I looked at how many steps would it take for each A node to reach a Z node
- I modified my part 1 function to take in arguments and set the defaults so that part 1 would still work 
- I saved the nodes and steps in a dictionary, although I could have just saved the number of steps for each in a list
- The A nodes need to reach the Z nodes *at the same time*. That means I need to find the least common multiple (LCM) for the number of steps for each A node. 
  - This may not work if an A node could reach multiple Z nodes. 
  - Let's say that A1 could reach Z1 and Z2 but the number of steps for Z1 is less than the number of steps for Z2. A1 would reach Z1 first so that number of steps is returned. But what if Z2 has a lower LCM with the other A steps?
  - The puzzle does say *the number of nodes with names ending in A is equal to the number ending in Z* so in this case there is probably just one Z for every A

### Tags
- modulo
- data structure 
- map function
- list unpacking
- math 
- lcm (least common multiple)

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|😄|😕😌🤓|
---

## Day 9 :desert_island:

[🧩](https://adventofcode.com/2023/day/9 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day9.py "Code")

### Part 1
- To find the next number in the sequence, find the differences between a set of numbers and then find the difference of the differences until the differences are all 0 (hopefully that make sense)
- Created a recursive function to find the differences between numbers in the list, then passed the differences back into the list until all the differences were zero.
- You could actually stop one loop earlier when the differences were all the same number. I debated between using groupby to see if all the numbers were the same or checking if all numbers were zero. 
  ```python
  len(list(groupby(diffs))) == 1
  ```
  ```python
  all([d == 0 for d in diffs])
  ```
- I figured out that the sum of the last differences would be added on to the next number

### Part 2

- I thought part 2 would be easy, I could just subtract the sum of differences from the first number in the sequence
- After writing the numbers down on paper, I figured out the pattern. Instead of adding up all the differences, you subtract every other one. Why does this work? No idea. But it works.

### Tags
- recursion
- recursive function

### Feelings about today's puzzles
| **Part 1** | **Part 2**             |
|------------|------------------------|
|:smile:| :monocle_face: :blush: |

---
## Day 10 :world_map:

[🧩](https://adventofcode.com/2023/day/10 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day10.py "Code")

### Part 1

- Currently, my code is pretty convoluted. I've tried to solve this puzzle a few different ways and made some mistakes along the way. This puzzle is still a work in progress for me.
- I'm able to navigate the maze now and I can solve the test input. However, I get recursion errors when I try to run my code on the actual input. 

### Part 2

- 

### Tags
- creating mapping with X Y coordinates
- recursion

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|:confounded:||

---
## Day 11 :stars: :milky_way:

[🧩](https://adventofcode.com/2023/day/11 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2023/day11.py "Code")

### Part 1

- In this puzzle, you need to find the distances between points (galaxies in the puzzle setup). But the catch is that the map expands if there are no points in the row or column.
- In part one I created a numpy array from the puzzle data.
- I created a few helper functions to 
  - find the empty rows and columns - rows and columns that didn't have a galaxy 
  - expand the universe - add more empty spaces to the array in empty rows and columns
  - print the array - this helped during testing to make sure my expanded array looked like the example
- When finding the pairs of galaxies, later galaxies should already be paired with previous galaxies (i.e. galaxy 1 pairs with galaxies 2-9, galaxy 2 pairs with galaxies 3-9 since there's already a 1,2 pairing) 
  - To find the pairs of galaxies, I originally used this code
  ```python
  for i in range(len(galaxies)):
      dist = sum([abs(galaxies[i][0] - gx[0]) + abs(galaxies[i][1] - gx[1]) for gx in galaxies[i:]])
      total_dist += dist
  ``` 
  - But replaced it with combinations from itertools which looks much cleaner
  ```python
  for galaxy_combo in combinations(galaxies, 2):
      g1x, g1y = galaxy_combo[0]
      g2x, g2y = galaxy_combo[1]
      dist = abs(g2x - g1x) + abs(g2y - g1y)
      total_dist += dist
  ```
- Finally, finding the distance between two galaxies was just finding the absolute value between the X values and the absolute value between the Y values

### Part 2

- In part 2 the empty spaces expand by 1,000,000 rather than just 1. That makes it too large to put into an array
- Since I can find the empty rows and columns, I should be able to tell when a pair of galaxies cross that empty row/column
- The total distance for that pair should increase by 1M * number of crosses of empty rows/columns
- This hasn't quite worked on the test data, however, so part 2 is still a work in progress at the moment

### Tags
- numpy
- itertools combinations

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
|:slightly_smiling_face:|:raised_eyebrow:|
