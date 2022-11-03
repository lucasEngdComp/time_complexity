n = int(input())
result = []
for case in range(1, n + 1):
    arr = input().split()
    cards_in_hand = arr[:24:-1]
    remaining = arr[24::-1]

    Y = 0
    for _ in range(3):
        card = remaining[0]
        first_element = card[0]
        if first_element.isdigit():
            X = int(first_element)
        else:
            X = 10
        Y += X
        remaining = remaining[(10 - X) + 1:]
    
    arr = cards_in_hand + remaining
    print(f"Case {case}: {arr[::-1][Y - 1]}")

# for case in result:
#     print(case)

# AC KC QC JC TC 9C 8C 7C 6C 5C 4C 3C 2C AD KD QD JD TD 9D 8D 7D 6D 5D 4D 3D 2D AH KH QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S
# AC KC QC JC TC 9C 8C 7C 6C 5C 4C 3C 2C AD KD QD JD TD 9D 8D 7D 6D 5D 4D 3D 2D AH KH QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S