---
## Day 1 :scroll:

[🧩](https://adventofcode.com/2024/day/1 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2024/day01.py "Code")

### Part 1 :star:

- created two separate lists from the input using `.split()`, then sorted the lists
- got absolute value of difference between items in the list with the same index value

### Part 2 :star:

- used `Counter` to get the number of times an item appears in list two
- then mulplited the value of each item in list one with the count of that item in list two

### Tags
- Counter

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
| :laughing: | :laughing: |

---
## Day 2 :radioactive:

[🧩](https://adventofcode.com/2024/day/2 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2024/day02.py "Code")

### Part 1 :star:

- found the difference between a number and the next number in the sequence 
- determine if all numbers in a sequence are ascending (diff > 0) or descending (diff < 0>) and the difference must be within a range
- Be careful with descending order! Change the min and max range since the differences are negative.
- created a `safety_check` method to provide a 1 if the numbers pass the checks or a 0 if they do not, then found the sum
- This could have been more concise. I used `all` to check if all the values met the asc/desc condition. I probably also could have used `map` and `filter` here as well. 

### Part 2 :star:

- I went with the brute force approach
- found all combinations of the list of numbers with one of the numbers removed
- then passed those combinations to the `safety_check` function 

### Tags
- list slicing

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
| :grinning: | :raised_eyebrow: |

---
## Day 3 :desktop_computer:

[🧩](https://adventofcode.com/2024/day/3 "Puzzle")    [:octocat:](https://github.com/lcirvine/advent_of_code/blob/master/2024/day03.py "Code")

### Part 1 :star:

- finding the regex pattern for part 1 was pretty straightforward

### Part 2 :star:

- part 2 was much more difficult
- rather than delete the text between "don't()" and "do()" I replaced the characters with "X" so that the index did not change
- initially I just used `re.sub`, however, my regex pattern replaced all the text between the first "don't" and the last "do"
- Created regex patterns to match "don't()" and "do()", then used `re.finditer` to find all instances of those patterns
- My next mistake was not considering that there might be multiple "don't"s before the next "do". I thought I could just get the indexes of the "don't"s and "do"s, zip them together to give me the range of indexes, then use slicing to replace the text in those characters. The order was incorrect though, sometimes the end index was before the start index.
- Finally, I sorted out which "do" should be paired with each "don't" by using a list comprehension to find the first value that was greater than the index of the start of the "don't" pattern. That gave me the range of indexes that should not be considered which I used string slicing to fill with "X" since it would not match my regex pattern. I could then pass the updated text to the same function I created for part 1. 

### Tags
- regex
- string slicing

### Feelings about today's puzzles
| **Part 1** | **Part 2** |
|------------|------------|
| :laughing: | :raised_eyebrow: |





[🐱](https://github-emoji-picker.rickstaa.dev/, "Emoji Picker")
