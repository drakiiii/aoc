from collections import Counter

def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    hands = []
    for index, line in enumerate(lines):
        line = line.replace("A", "E")
        line = line.replace("K", "D")
        line = line.replace("Q", "C")
        line = line.replace("J", "B")
        line = line.replace("T", "A")
        hands.append([index, line.split()[0], int(line.split()[1])])

    for i in range(0, len(hands)):
        cards_dict = dict(Counter(hands[i][1]))
        
        # high_card
        if len(cards_dict) == 5:
            power = 1
            hands[i].append(power)

        # one pair
        elif len(cards_dict) == 4:
            power = 2
            hands[i].append(power)
        
        elif len(cards_dict) == 3:

            # two pair
            if 2 in cards_dict.values():
                power = 3
                hands[i].append(power)

            # three kind
            else:
                power = 4
                hands[i].append(power)

        elif len(cards_dict) == 2:

            # full house
            if 3 in cards_dict.values():
                power = 5
                hands[i].append(power)

            # four kind
            else:
                power = 6
                hands[i].append(power)
        # five kind
        else:
            power = 7
            hands[i].append(power)
        
        
    hands = sorted(hands, key=lambda x: x[1])
    hands = sorted(hands, key=lambda x: x[3])
    
    tot = 0
    for i in range(0, len(hands)):
        win = (i + 1) * hands[i][2]
        tot += win
    print(tot)


def part2(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    hands = []
    for index, line in enumerate(lines):
        line = line.replace("A", "E")
        line = line.replace("K", "D")
        line = line.replace("Q", "C")
        line = line.replace("J", "1")
        line = line.replace("T", "A")
        hands.append([index, line.split()[0], int(line.split()[1])])

    ranks = ["E", "D", "C", "A", "9", "8", "7", "6", "5", "4", "3", "2"]

    for i in range(0, len(hands)):
        cards_dict = dict(Counter(hands[i][1]))
        if "1" in hands[i][1]:

            # high card
            if len(cards_dict) == 5:
                for char in ranks:
                    if char in hands[i][1]:
                        hands[i].append(hands[i][1].replace("1", char))
                        break

            # one pair
            elif len(cards_dict) == 4:
                if cards_dict["1"] == 2:
                    for char in ranks:
                        if char in hands[i][1]:
                            hands[i].append(hands[i][1].replace("1", char))
                            break
                else:
                    for k, v in cards_dict.items():
                        if v == 2:
                            rep_char = k
                            hands[i].append(hands[i][1].replace("1", rep_char))
                            break
                    
        
            elif len(cards_dict) == 3:
                # two pair
                if 3 not in cards_dict.values():
                    for k, v in cards_dict.items():
                        if k == "1" and v == 2:
                            x_cards_dict = dict(Counter(hands[i][1].replace("1", "")))
                            char = max(x_cards_dict, key=x_cards_dict.get)
                            break
                        else:
                            for char in ranks:
                                if char in hands[i][1]:
                                    char = char
                                    break

                # three kind
                else:
                    for k, v in cards_dict.items():
                        if k == "1" and v == 1:
                            x_cards_dict = dict(Counter(hands[i][1].replace("1", "")))
                            char = max(x_cards_dict, key=x_cards_dict.get)
                            break
                        elif k == "1" and v == 3:
                            for char in ranks:
                                if char in hands[i][1]:
                                    char = char
                                    break

                hands[i].append(hands[i][1].replace("1", char))
                
            # full house / four kind
            elif len(cards_dict) == 2:
                for char in hands[i][1]:
                    if char != "1":
                        rep_char = char
                hands[i].append(hands[i][1].replace("1", rep_char))
            
            # five kind
            else:
                hands[i].append(hands[i][1])

        else:
            hands[i].append(hands[i][1])

        new_cards_dict = dict(Counter(hands[i][3]))

        # high_card
        if len(new_cards_dict) == 5:
            power = 1
            hands[i].append(power)

        # one pair
        elif len(new_cards_dict) == 4:
            power = 2
            hands[i].append(power)
        
        elif len(new_cards_dict) == 3:

            # two pair
            if 2 in new_cards_dict.values():
                power = 3
                hands[i].append(power)

            # three kind
            else:
                power = 4
                hands[i].append(power)

        elif len(new_cards_dict) == 2:

            # full house
            if 3 in new_cards_dict.values():
                power = 5
                hands[i].append(power)

            # four kind
            else:
                power = 6
                hands[i].append(power)

        # five kind
        else:
            power = 7
            hands[i].append(power)
        
    hands = sorted(hands, key=lambda x: x[1])
    hands = sorted(hands, key=lambda x: x[4])

    tot = 0
    for i in range(0, len(hands)):
        win = (i + 1) * hands[i][2]
        tot += win
    
    print(tot)
