from aoc_inputs import get_input

data = get_input().split('\n')

tree_map = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        tree_map[(x, y)] = int(data[y][x])


def part_1():
    visible_trees = 0
    min_x, min_y = min(tree_map)  # will be (0, 0)
    max_x, max_y = max(tree_map)
    for coord, height in tree_map.items():
        x, y = coord
        # borders
        if x == min_x or x == max_x or y == min_y or y == max_y:
            visible_trees += 1
        else:
            # make sure to add +1 to get end of range and not to count the current tree!
            left_trees = [tree_map[(xr, y)] for xr in range(min_x, x)]
            right_trees = [tree_map[(xr, y)] for xr in range(x + 1, max_x + 1)]
            up_trees = [tree_map[(x, yr)] for yr in range(min_y, y)]
            down_trees = [tree_map[(x, yr)] for yr in range(y + 1, max_y + 1)]
            if height > max(up_trees) or height > max(down_trees) or height > max(left_trees) or height > max(right_trees):
                visible_trees += 1
    return visible_trees


def part_2():
    min_x, min_y = min(tree_map)  # will be (0, 0)
    max_x, max_y = max(tree_map)
    scenic_scores = {}
    for coord, height in tree_map.items():
        x, y = coord
        left_trees_visible = 0
        # you have to count out from the tree, not in toward the tree!
        for lt in range(x - 1, min_x - 1, -1):
            if tree_map[(lt, y)] >= height:
                left_trees_visible += 1
                break
            else:
                left_trees_visible += 1
        right_trees_visible = 0
        for rt in range(x + 1, max_x + 1):
            if tree_map[(rt, y)] >= height:
                right_trees_visible += 1
                break
            else:
                right_trees_visible += 1
        up_trees_visible = 0
        # you have to count out from the tree, not in toward the tree!
        for ut in range(y - 1, min_y - 1, -1):
            if tree_map[(x, ut)] >= height:
                up_trees_visible += 1
                break
            else:
                up_trees_visible += 1
        down_trees_visible = 0
        for dt in range(y + 1, max_y + 1):
            if tree_map[(x, dt)] >= height:
                down_trees_visible += 1
                break
            else:
                down_trees_visible += 1
        scenic_scores[(x, y)] = (left_trees_visible * right_trees_visible * up_trees_visible * down_trees_visible)
    max_score = max(scenic_scores.values())
    # wouldn't you want to know what tree it was rather than the score?
    return {tree: score for tree, score in scenic_scores.items() if score == max_score}


if __name__ == '__main__':
    print(part_1())
    print(part_2())
