from functools import reduce

class BingoNumber:
    def __init__(self, number):
        self.number = number
        self.is_marked = False
    
    def set_marked(self):
        self.is_marked = True
    
    def __repr__(self) -> str:
        if self.is_marked:
            return f"{self.number}m"
        return self.number

class BingoBoard:
    def __init__(self, input):
        self.input = input
        self.board = []
        self.board_result_map = {}
        self.has_bingo = False
        self.init_board()
        
    def init_board(self):
        for line in self.input:
            row = [BingoNumber(num) for num in line.split()]
            if len(line):
                self.board.append(row)
        
    def __repr__(self) -> str:
        output = "\nBoard:\n"
        for i in self.board:
            for j in i:
                output += f"{j}, "
            output += "\n"
        return output
    
    def set_marked(self, number: str) -> None:
        for x, row in enumerate(self.board, 0):
            for y, num in enumerate(row, 0):
                if num.number == number:
                    num.set_marked()
                    if f'x{x}' not in self.board_result_map:
                        self.board_result_map[f'x{x}'] = 0
                    if f'y{y}' not in self.board_result_map:
                        self.board_result_map[f'y{y}'] = 0
                    self.board_result_map[f'y{y}'] += 1
                    self.board_result_map[f'x{x}'] += 1
                if 5 in self.board_result_map.values():
                    print(self.board_result_map)
                    print(self)
                    self.has_bingo = True
    
    def calculate_score(self, number: str) -> int:
        total = 0
        for i in self.board:
            for j in i:
                if not j.is_marked:
                    total += int(j.number)
        
        return int(number) * total


with open("input.txt") as file:
    bingo_numbers_input = file.readline().strip()
    bingo_numbers_called = [num for num in bingo_numbers_input.split(',')]
    print(bingo_numbers_called)

    bingo_boards_input = [line.strip() for line in file.readlines()]
    bingo_boards = []
    for i in range(0, len(bingo_boards_input), 6):
        bingo_board = BingoBoard(bingo_boards_input[i: i + 6])
        bingo_boards.append(bingo_board)

    # let's play!
    game_over = False
    for number in bingo_numbers_called:
        print(f'Number: {number}')
        for board in bingo_boards:
            board.set_marked(number)
            if board.has_bingo:
                game_over = True
                print(f"Score:{board.calculate_score(number)}")
                break
        if game_over:
            break
    