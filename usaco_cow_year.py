def solve(info):
    zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    curr_from_bessie = {"Bessie": 1}
    for i in info:
        if i[1] == "previous":  # check to see if cow born before of after
            num = 12 + (curr_from_bessie[i[3]] - zodiacs.index(i[2]))
            curr_from_bessie[i[0]] = [-num, i[2]]
        if i[1] == "next":  # check to see if cow born before of after
            num = zodiacs.index(i[2]) - curr_from_bessie[i[3]] 
            curr_from_bessie[i[0]] = [num, i[2]]
    return curr_from_bessie

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        info = [f.readline().strip().split() for i in range(n)]
        new_info = []
        for i in info:  # i: Mildred born in previous Dragon year from Bessie, objective --> Mildred previous Dragon Bessie
            new_string = [i[0]] + i[3:5] + [i[-1]]
            new_info.append(new_string)
        print(solve(new_info))