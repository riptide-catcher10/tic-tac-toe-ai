import RPi.GPIO as GPIO
import time

squares = [
          1,2,3,4,5,6,7,8,9]
pins = {
    0: 18,
    1: 22,
    2: 23,
    3: 13,
    4: 17,
    5: 12,
    6: 26,
    7: 25,
    8: 24
}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for index, pin in pins.items():
        GPIO.setup(pin, GPIO.OUT)

def turn_off_light(pin):
    GPIO.output(pin, GPIO.LOW)

class opponent():
    def __init__(self,squares):
       self.squares = squares
       self.opponent_squares = None
       self.xoro = None
    def ask_x_or_o(self):
       self.xoro = input("Is the opponent X or O?")
    def ask(self):
       self.opponent_squares = input("what square did your opponent mark? ")
       split_board = self.opponent_squares.split(',')
       return split_board
class predict():
    def __init__(self,squares, pins):
        self.s = squares
        self.pins = pins
        self.must_block = False
    def light_pin(self, pin):
        print(f'lighting up pin {pin}')
        GPIO.output(pin, GPIO.HIGH)


    def check_board(self, board):
        for index, spot in enumerate(board):
            if board[0] == board[1] and board[0] != '-':
                self.light_pin(self.pins[2])
                return (self.pins[2], True)
            elif board[0] == board[3] and board[0] != '-':
                self.light_pin(self.pins[6])
                return (self.pins[6], True)
            elif board[0] == board[4] and board[0] != '-':
                self.light_pin(self.pins[8])
                return (self.pins[8], True)

            elif board[1] == board[4] and board[1] != '-':
                self.light_pin(self.pins[7])
                return (self.pins[7], True)
            elif board[2] == board[5] and board[2] != '-':
                self.light_pin(self.pins[8])
                return (self.pins[8], True)
            elif board[2] == board[4] and board[2] != '-':
                self.light_pin(self.pins[2])
                return (self.pins[2], True)
            elif board[2] == board[1] and board[2] != '-':
                self.light_pin(self.pins[0])
                return (self.pins[0], True)


setup()
opp = opponent(squares)
x_or_o = opp.ask_x_or_o()
game_over = False
while not game_over:
   board = opp.ask()
   pred = predict(squares, pins)
   light_pin =  pred.check_board(board)
   time.sleep(30)
   turn_off_light(light_pin[0])
   game_over = light_pin[1]


if game_over:
    print('The game is over, I won')
