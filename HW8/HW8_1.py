class Card:
    # class attribue
    suit_list = ['S', 'H', 'D', 'C']
    rank_list = [
        'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    ]
    squence = '12345678910111213 123413 1231213 12111213 110111213'

    # 初始化
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # indtance method
    # ACE
    def rule_a(self):
        return self.rank.count('A')

    # PAIR
    def rule_b(self):
        pair = 0
        for i in range(len(Card.rank_list)):
            if self.rank.count(Card.rank_list[i]) >= 2:
                pair += 1
        if self.rank.count('A') >= 2:
            return pair * 2
        else:
            return pair * 2 + self.rule_a()

    # same color
    def rule_c(self):
        for i in range(len(Card.suit_list)):
            if self.suit.count(Card.suit_list[i]) == 5:
                return 3
        return 0

    # sequence
    def rule_d(self):
        rank_dict = dict()
        for i, j in enumerate(Card.rank_list, start=1):
            rank_dict[j] = i
        cardseq = []
        for i in range(len(self.rank)):
            cardseq.append(int(rank_dict[self.rank[i]]))
        result = ''
        cardseq = sorted(cardseq)
        for i in range(len(cardseq)):
            result += str(cardseq[i])
        if result in Card.squence:
            return 5
        return 0

    # 葫蘆
    def rule_e(self):
        pair = False
        tri = False
        for i in range(len(Card.rank_list)):
            if self.rank.count(Card.rank_list[i]) == 3:
                tri = True
            if self.rank.count(Card.rank_list[i]) == 2:
                pair = True
        return (tri & pair) * 10

    # 四條
    def rule_f(self):
        for i in range(len(Card.rank_list)):
            if self.rank.count(Card.rank_list[i]) == 4:
                if self.rank.count('A') == 1:
                    return 20 + self.rule_a()
                else:
                    return 20
        return 0

    # 同花順
    def rule_g(self):
        is_squ = True if self.rule_d() == 5 else False
        is_samecolor = True if self.rule_c() == 3 else False
        return (is_samecolor & is_squ) * 100

    def score(self):
        return max(self.rule_a(), self.rule_b(), self.rule_c(), self.rule_d(),
                   self.rule_e(), self.rule_f(), self.rule_g())


card = Card([str(i) for i in input().split(',')],
            [str(i) for i in input().split(',')])
print(card.score())