class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]
    MAPPING = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    def __init__(self, hand):
        cards = hand.split(" ")
        hand = [(int(x[0] if x[0] not in self.MAPPING else self.MAPPING[x[0]]), x[1]) for x in cards]
        hand.sort(key=lambda x: x[0])
        functions = [self.is_straight_flush, self.is_four_kind, self.is_full_house, self.is_flush, self.is_straight, self.is_three_kind, self.is_two_pair, self.is_one_pair, self.is_high_card]
        for f in functions:
            if f(hand):
                self.hand_val = f(hand)
                break

    def is_straight_flush(self, hand):
        for i in range(1, len(hand)):
            n, s = hand[i]
            pn, ps = hand[i-1]
            if not (n - pn == 1 and s == ps):
                return False
        return 8, n

    def is_four_kind(self, hand):
        d = self.get_hand_dict(hand)
        for i in d:
            if d[i] == 4:
                for j in d:
                    if i != j:
                        return 7,i,j
        return False

    def is_full_house(self, hand):
        d = self.get_hand_dict(hand)
        if len(d) == 2:
            for i in d:
                if d[i] == 3:
                    for j in d:
                        if i != j:
                            return 6, i, j
        return False

    def is_flush(self, hand):
        for i in range(1, len(hand)):
            n, s = hand[i]
            pn, ps = hand[i-1]
            if ps != s:
                return False
        return (5,) + tuple(sorted((x[0] for x in hand), reverse=True))

    def is_straight(self, hand):
        for i in range(1, len(hand)):
            n, s = hand[i]
            pn, ps = hand[i-1]
            if n - pn != 1:
                return False
        return 4, n

    def is_three_kind(self, hand):
        d = self.get_hand_dict(hand)
        if len(d) == 3:
            for i in d:
                if d[i] == 3:
                    return (3, i) + tuple(sorted([j for j in d if i != j], reverse=True))
        return False

    def is_two_pair(self, hand):
        d = self.get_hand_dict(hand)
        if len(d) == 3:
            poss = []
            for i in d:
                if d[i] == 2:
                    poss.append(i)
            if len(poss) == 2:
                return (2, max(poss), min(poss)) + tuple(x for x in d if x not in poss)
        return False

    def is_one_pair(self, hand):
        d = self.get_hand_dict(hand)
        if len(d) == 4:
            for i in d:
                if d[i] == 2:
                    return (1, i) + tuple(sorted((x for x in d if d[x] == 1), reverse=True))
        return False

    def is_high_card(self, hand):
        return (0,) + tuple(sorted((x[0] for x in hand), reverse=True))

    def get_hand_dict(self, hand):
        d = dict()
        for i in range(0, len(hand)):
            n, s = hand[i]
            d[n] = d.get(n, 0) + 1
        return d

    def compare_with(self, other):
        if self.hand_val == other.hand_val:
            return "Tie"
        elif self.hand_val < other.hand_val:
            return "Loss"
        else:
            return "Win"
