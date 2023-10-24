from typing import List
import numpy as np


def generatebitboard(position: List[str]):
    bb = [0 for i in range(64)]

    for pos in position:
        file = ord(pos[0]) - 97
        rank = int(pos[1]) - 1
        bb[rank * 8 + file] = 1
    return np.array(bb)


class Board:
    """
    White black occupied empty
    pawns white black
    bishop white black
    rook white black
    knight white black
    king white black
    queen white black

    yes function  to set starting state
    yes unction to get bitboard state
    - function to map from geometric <> Bitmap
    yes function to bitwise OR all bitmaps -> Board State
    - function to bitwise AND all bitmaps -> Peice Capture(hetro) Illegeal (homo)Moves
    - function to map fen <-> board state
    - function to make attack bitboard
    """

    def __init__(self):
        self.rookw_bitboard = generatebitboard(['a1', 'h1'])
        self.bishopw_bitboard = generatebitboard(['c1', 'f1'])
        self.knightw_bitboard = generatebitboard(['b1', 'g1'])
        self.kingw_bitboard = generatebitboard(['e1'])
        self.queenw_bitboard = generatebitboard(['d1'])
        self.pawnw_bitboard = generatebitboard(['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'])

        self.rookb_bitboard = generatebitboard(['a8', 'h8'])
        self.bishopb_bitboard = generatebitboard(['c8', 'f8'])
        self.knightb_bitboard = generatebitboard(['b8', 'g8'])
        self.kingb_bitboard = generatebitboard(['e8'])
        self.queenb_bitboard = generatebitboard(['d8'])
        self.pawnb_bitboard = generatebitboard(['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'])
        self.white_bitboard = np.array([1 if i % 2 == 0 else 0 for i in range(64)])
        self.black_bitboard = np.array([1 if i % 2 != 0 else 0 for i in range(64)])
        self.empty_bitboard = np.array([1 if 15 < i < 48 else 0 for i in range(64)])
        self.occupied = np.array([0 if 15 < i < 48 else 1 for i in range(64)])
        self.bitboards = np.array([
            self.rookw_bitboard,
            self.bishopw_bitboard,
            self.knightw_bitboard,
            self.kingw_bitboard,
            self.queenw_bitboard,
            self.pawnw_bitboard,
            self.rookb_bitboard,
            self.bishopb_bitboard,
            self.knightb_bitboard,
            self.kingb_bitboard,
            self.queenb_bitboard,
            self.pawnb_bitboard, ]
        )

    def get_bb_state(self):
        return self.rookw_bitboard | self.bishopw_bitboard | self.knightw_bitboard | \
               self.kingw_bitboard | self.queenw_bitboard | self.pawnw_bitboard | \
               self.rookb_bitboard | self.bishopb_bitboard | self.knightb_bitboard \
               | self.kingb_bitboard | self.queenb_bitboard | self.pawnb_bitboard

    def get_bb_white(self):
        return self.rookw_bitboard | self.bishopw_bitboard | self.knightw_bitboard | \
               self.kingw_bitboard | self.queenw_bitboard | self.pawnw_bitboard

