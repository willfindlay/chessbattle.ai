import chess
import chess.svg


class Game:
    def __init__(self):
        self.board = chess.Board()

    def to_svg(self):
        return chess.svg.board(self.board)

    def serialize(self):
        return {'board_fen': self.board.fen()}
