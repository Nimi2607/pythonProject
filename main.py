class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

class Player:
    def _init_(self, name):
        self.name = name
        self.score = 0
        self.guess_history = LinkedList()

def get_player_names():
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")
    return player1_name, player2_name

def display_guess_history(player):
    print(f"\nGuess History for {player.name} ({player.guess_history.get_length()} guesses):")
    current = player.guess_history.head
    while current:
        print(current.data)
        current = current.next

def word_guessing_game():
    print("Welcome to the Mind Game!")

    player1_name, player2_name = get_player_names()

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    players = [player1, player2]

    for game_round in range(2):
        word_setter = players[game_round % 2]
        word_guesser = players[(game_round + 1) % 2]

        secret_word = input(f"{word_setter.name}, set a word : ")
        hint = input(f"{word_setter.name}, provide a hint: ")
        num_letters = len(secret_word)

        typo_stack = Stack()

        print(f"\nHint: The word is related to '{hint}' and has {num_letters} letters.\n")

        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            attempts += 1
            print(f"{word_guesser.name}'s turn (Attempt {attempts})")
            guess = input(f"{word_guesser.name}, make a guess: ")

            if guess == secret_word:
                print(f"Congratulations, {word_guesser.name} wins the round!")
                word_guesser.guess_history.append(guess)
                word_setter.score += 1
                break
            elif guess == "undo":
                undo_guess(word_guesser)
            else:
                word_guesser.guess_history.append(guess)
                typo_stack.push(guess)
                print("Incorrect. Try again.\n")

        if attempts == max_attempts:
            print(f"{word_guesser.name}, maximum number of attempts.\n")

    for player in players:
        display_guess_history(player)

    if player1.score < player2.score:
        print(f"{player1.name} wins the game with a score of {player1.score}-{player2.score}!")
    elif player2.score < player1.score:
        print(f"{player2.name} wins the game with a score of {player2.score}-{player1.score}!")
    else:
        if player1.guess_history.get_length() < player2.guess_history.get_length():
            print(f"{player1.name} wins the game with fewer attempts!")
        elif player2.guess_history.get_length() < player1.guess_history.get_length():
            print(f"{player2.name} wins the game with fewer attempts!")
        else:
            print("It's a draw!")

def undo_guess(player):
    current = player.guess_history.head
    previous = None

    while current and current.next:
        previous = current
        current = current.next

    if previous is not None:
        previous.next = None
        print(f"Undoing last guess: {current.data}\n")
    else:
        print("No previous guesses to undo.\n")

if _name_ == "_main_":
    word_guessing_game()