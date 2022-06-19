class TranspositionTable:

    def __init__(self, hashValue, flag, score, bestMove, depth):
        self.hashValue = hashValue
        self.flag = flag  # 0 accurate; 1 lower bound; 2 upper bound
        self.score = score
        self.bestMove = bestMove
        self.depth = depth  # From bottom

