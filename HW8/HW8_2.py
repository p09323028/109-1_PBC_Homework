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
        if len(self.rank) == 5 and result in Card.squence:
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


class Deck:
    seq = 'A2 23 34 45 56 67 78 89 910 10J JQ QK KA'

    # 初始化
    def __init__(self):
        self.cards = []

    # 加牌
    def add_card(self, card):
        self.cards.append(card)

    # 檢查是否丟牌
    def pop_card(self):
        for i in range(len(self.cards)):
            if self.cards[i][0] == self.cards[-1][0]:
                if (self.cards[i][1:] + self.cards[-1][1:]) in Deck.seq:
                    del self.cards[i]
                    del self.cards[-1]
                    break

# 人數
number = int(input())

# 發牌資料
input_list = []
for i in range(number):
    input_list.append([str(i) for i in input().split(',')])


# 發牌結果
def suit_rank(n):
    deck = Deck()
    for i in range(len(input_list[n])):
        deck.add_card(input_list[n][i])
        deck.pop_card()
        if len(deck.cards) == 5:
            break
    suit, rank = [], []
    for i in range(len(deck.cards)):
        suit.append(deck.cards[i][0])
        rank.append(deck.cards[i][1:])
    return suit, rank


result_score = []
for i in range(number):
    suit, rank = suit_rank(i)
    card = Card(suit, rank)
    result_score.append(str(card.score()))

print(','.join(result_score))