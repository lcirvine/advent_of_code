# Advent of Code 2023 Notes

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