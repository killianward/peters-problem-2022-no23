# Peter's Problem 2022 No.23

from itertools import combinations as comb

teams = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

div1 = []
div2 = []

possible_smaller_divs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for x, i in enumerate(possible_smaller_divs):
    div1.clear()
    div2.clear()
    div1 = teams[0:i]
    div2 = teams[i:len(teams)]
    num_of_games_div_1 = len(list(comb(div1, 2)))
    num_of_games_div_2 = len(list(comb(div2, 2)))

    if num_of_games_div_2 - num_of_games_div_1 == 45:
        print(f"Answer: {len(div1)}")
