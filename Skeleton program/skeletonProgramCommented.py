#Skeleton Program code for the AQA A Level Paper 1 Summer 2027 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA Programmer Team
#developed in the Python 3.9 programming environment

# =====================================================================
# OVERVIEW (added comments)
# ---------------------------------------------------------------------
# This is a two-player "tile matching" (memory-style) game.
#   * The board is a square grid of PILES (36 piles = a 6x6 grid).
#   * Each pile is a stack of TILES. Each tile has a symbol (e.g. "A")
#     and a points value.
#   * You can only see the SYMBOL of the TOP tile of a pile, and only
#     when you choose that pile. The board display just shows how many
#     tiles are in each pile.
#   * On your turn you choose two different piles. If the top tiles have
#     the same symbol, you win those two tiles: they go to the discard
#     and their points are added to your score.
#   * The game ends when a player reaches MaxScore, or no tiles are left.
#
# The program is built from 4 small classes plus two functions:
#   Tile   - one tile (symbol + points)
#   Pile   - a stack of tiles (with a maximum size)
#   Player - a name and a score
#   Game   - holds the board, players, discard, and runs the game loop
#   Main() - sets up a new game or loads a saved one, then starts it
#   LoadGame() - reads a saved game from a text file
# =====================================================================

import math   # needed for math.sqrt (to work out the grid size)

def Main():
    # ---- Variables that describe the state of a game ----
    Board = []             # list of Pile objects (the grid, stored as one flat list)
    Players = []           # list of Player objects
    Discard = []           # list of Tile objects that have been matched and removed
    TurnsSinceMatch = 0    # counts turns since the last successful match (currently only stored, never used)
    WhoseTurn = 0          # index into Players: 0 = Player 1, 1 = Player 2
    MaxScore = 10          # first player to reach this score ends the game
    FILE_EXTENSION = ".txt"

    # Ask for a filename; the ".txt" is added automatically.
    # If the user just presses Enter, FileName ends up as just ".txt"
    FileName = input("Enter filename to load or just press Enter to play the default game: ") + FILE_EXTENSION
    UseDataFromFile = False

    # If they typed something, try to load it
    if FileName != FILE_EXTENSION:
        UseDataFromFile, Board, Players, Discard, MaxScore, WhoseTurn, TurnsSinceMatch = LoadGame(FileName)
        if UseDataFromFile == False:
            print("Setting up default game")

    # Default game (no file given, or the file failed to load)
    if UseDataFromFile == False:
        Players.append(Player("Player 1", 0))   # name, starting score
        Players.append(Player("Player 2", 0))
        for Count in range(1, 37):              # 36 piles -> 6x6 grid
            P = Pile(3, 0)                      # max 3 tiles per pile, bonus of 0 (bonus is never used yet)
            P.Add(Tile("A", 1))                 # Add() puts each new tile on TOP of the pile...
            P.Add(Tile("B", 2))
            P.Add(Tile("A", 1))                 # ...so the pile is (top to bottom): A(1), B(2), A(1)
            Board.append(P)

    # Create the Game object and start playing
    ThisGame = Game(Board, Players, Discard, WhoseTurn, MaxScore, TurnsSinceMatch)
    ThisGame.PlayGame()
    input()   # keeps the window open at the end until Enter is pressed

def LoadGame(FileName):
    # Reads a saved game. Returns True/False for success, plus all the game data.
    #
    # Expected file layout (one item per line):
    #   line 1        : number of piles on the board
    #   next N lines  : one pile each -> bonus,symbol,points,symbol,points,...
    #   next line     : number of players
    #   next N lines  : one player each -> name,score
    #   next line     : the discard -> symbol,points,symbol,points,...
    #   next line     : MaxScore
    #   next line     : WhoseTurn
    #   last line     : TurnsSinceMatch
    Board = []
    Players = []
    Discard = []
    MaxScore = 0
    WhoseTurn = 0
    TurnsSinceMatch = 0
    try:
        with open(FileName) as File:
            # --- Board ---
            LineFromFile = File.readline()
            BoardSize = int(LineFromFile)
            for i in range(1, BoardSize + 1):
                LineFromFile = File.readline()
                Items = LineFromFile.split(",")          # split the line at each comma
                PileSize = len(Items) // 2               # each tile takes 2 items, so this = number of tiles
                P = Pile(PileSize, int(Items[0]))        # first item on the line is the pile's bonus
                # Work backwards through the (symbol, points) pairs so that the
                # first tile in the file ends up on top of the pile
                for TileNo in range(len(Items) - 2, -1, -2):
                    P.Add(Tile(Items[TileNo], int(Items[TileNo + 1])))
                Board.append(P)

            # --- Players ---
            LineFromFile = File.readline()
            NoOfPlayers = int(LineFromFile)
            for i in range (1, NoOfPlayers + 1):
                LineFromFile = File.readline()
                Items = LineFromFile.split(",")
                Players.append(Player(Items[0], int(Items[1])))   # name, score

            # --- Discard ---
            LineFromFile = File.readline()
            Items = LineFromFile.split(",")
            for i in range(0, len(Items) - 1, 2):                 # step 2: (symbol, points) pairs
                Discard.append(Tile(Items[i], int(Items[i + 1])))

            # --- Other game settings ---
            LineFromFile = File.readline()
            MaxScore = int(LineFromFile)
            LineFromFile = File.readline()
            WhoseTurn = int(LineFromFile)
            LineFromFile = File.readline()
            TurnsSinceMatch = int(LineFromFile)
    except:
        # Any problem (file missing, badly formatted, etc.) ends up here
        print("File not loaded")
        return False, Board, Players, Discard, MaxScore, WhoseTurn, TurnsSinceMatch
    return True, Board, Players, Discard, MaxScore, WhoseTurn, TurnsSinceMatch

class Game():
    def __init__(self, B, P, D, WT, MS, TSM):
        # Double underscore = private attribute (only usable inside this class)
        self.__Board = B
        self.__Players = P
        self.__Discard = D
        self.__WhoseTurn = WT
        self.__MaxScore = MS
        self.__TurnsSinceMatch = TSM
        self.__GameOver = False
        # The board is a flat list, but displayed as a square grid.
        # e.g. 36 piles -> sqrt(36) = 6, so the grid is 6 wide and 6 tall
        self.__GridSize = int(math.sqrt(len(self.__Board)))

    def PlayGame(self):
        # The main game loop: one pass through = one player's turn
        while self.__GameOver == False:

            # ---- Menu loop: keeps showing the menu until the player picks "T" (take turn) ----
            Choice = ""
            while Choice != "T":
                self.__DisplayMenu()
                Choice = self.__GetChoice()
                if Choice == "B":
                    self.__DisplayBoard()
                elif Choice == "D":
                    self.__DisplayDiscard()
                elif Choice == "S":
                    self.__DisplayScores()

            # ---- The player picks two piles (must be different piles) ----
            Pile1 = self.__ChoosePile()
            Pile2 = self.__ChoosePile()
            while Pile1 == Pile2:
                Pile2 = self.__ChoosePile()

            self.__TurnsSinceMatch += 1   # assume no match; reset to 0 below if there is one

            # Both piles must have at least one tile to be compared
            if self.__Board[Pile1].Empty() == False and self.__Board[Pile2].Empty() == False:

                # Compare the SYMBOLS of the two top tiles
                if self.__Board[Pile1].GetSymbolOfTopTile() == self.__Board[Pile2].GetSymbolOfTopTile():
                    # ---- MATCH ----
                    self.__TurnsSinceMatch = 0
                    Tile1 = self.__Board[Pile1].Remove()   # take top tile off each pile
                    Tile2 = self.__Board[Pile2].Remove()
                    self.__Discard.append(Tile1)           # move both to the discard
                    self.__Discard.append(Tile2)
                    ScoreIncrease = 0
                    ScoreIncrease += Tile1.GetPoints() + Tile2.GetPoints()   # score = sum of both tiles' points
                    self.__Players[self.__WhoseTurn].ChangeScore(ScoreIncrease)
                    print(f"{self.__Players[self.__WhoseTurn].GetName()}, you had two matching {Tile1.GetSymbol()} tiles; your score has increased by {ScoreIncrease}")
                else:
                    # ---- NO MATCH: reveal the two symbols so players can remember them ----
                    print("You did not find a matching pair.")
                    print(f"The first pile you chose had a {self.__Board[Pile1].GetSymbolOfTopTile()}")
                    print(f"The second pile you chose had a {self.__Board[Pile2].GetSymbolOfTopTile()}")
            else:
                # At least one chosen pile had no tiles (the turn is still used up)
                print("You chose an empty pile")
            print()

            # ---- End of turn: switch player, then check whether the game is over ----
            self.__UpdateWhoseTurn()
            self.__GameOver = self.__MaxScoreReached() or self.__NoMoreTilesLeft()

        # ---- Game finished: announce the winner (nothing is printed for a draw) ----
        if self.__Players[0].GetScore() > self.__Players[1].GetScore():
            print(f"{self.__Players[0].GetName()} has won!")
        elif self.__Players[1].GetScore() > self.__Players[0].GetScore():
            print(f"{self.__Players[1].GetName()} has won!")

    def __DisplayScores(self):
        # Prints each player's name and score
        print()
        for P in self.__Players:
            print(f"{P.GetName()}: has a score of {P.GetScore()}")
        print()

    def __DisplayMenu(self):
        # Prints the menu options
        print()
        print()
        print("MENU")
        print("B. Display the board")
        print("D. Display the discard")
        print("T. Take turn")
        print("S. Display scores")
        print()

    def __GetChoice(self):
        # Asks the current player for their menu choice
        Choice = input(f"{self.__Players[self.__WhoseTurn].GetName()}, enter your choice: ")
        return Choice

    def __DisplayBoard(self):
        # Draws the grid showing the NUMBER OF TILES in each pile (not the symbols).
        # Rows are printed from the top (y = GridSize) down to y = 1,
        # so (1,1) is the bottom-left, like a graph.
        for y in range (self.__GridSize, 0, -1):
            print(f"{y}|", end="")                        # row label and left border
            for x in range(1, self.__GridSize + 1):
                print(self.__Board[self.__GetIndex(x, y)].GetNumberOfTiles(), end="")
            print()
        # Bottom border line
        print("  ", end="")
        for x in range(1, self.__GridSize + 1):
            print("-", end="")
        print()
        # Column numbers along the bottom
        print("  ", end="")
        for x in range (1, self.__GridSize + 1):
            print(x, end="")
        print()

    def __DisplayDiscard(self):
        # Prints the symbols of all discarded tiles, separated by commas
        print()
        print()
        print("Discard: ", end="")
        if len(self.__Discard) == 0:
            print("Empty")
        else:
            print(self.__Discard[0].GetSymbol(), end="")      # first one has no comma before it
            Count = 1
            while Count < len(self.__Discard):
                print(f", {self.__Discard[Count].GetSymbol()}", end="")
                Count += 1
        print()
        print()

    def __ChoosePile(self):
        # Asks for x and y coordinates and converts them to a position in the flat Board list
        x = 0
        y = 0
        x = int(input("Enter x coordinate: "))     # note: no validation - non-numbers crash the program
        y = int(input("Enter y coordinate: "))     # and numbers outside the grid aren't checked
        return self.__GetIndex(x, y)

    def __GetIndex(self, x, y):
        # Converts grid coordinates (1-based) into a 0-based index in the flat list.
        # e.g. on a 6x6 grid: (1,1) -> 0, (6,1) -> 5, (1,2) -> 6, (6,6) -> 35
        return x - 1 + ((y - 1) * self.__GridSize)

    def __UpdateWhoseTurn(self):
        # Moves to the next player, wrapping back to 0 after the last one
        # (the % is what makes it wrap: with 2 players it goes 0,1,0,1,...)
        self.__WhoseTurn = (self.__WhoseTurn + 1) % len(self.__Players)

    def __NoMoreTilesLeft(self):
        # True only if EVERY pile on the board is empty
        for P in self.__Board:
            if P.Empty() == False:
                return False
        return True

    def __MaxScoreReached(self):
        # True if any player has reached (or passed) the score needed to win
        for P in self.__Players:
            if P.GetScore() >= self.__MaxScore:
                return True
        return False

class Tile():
    # A single tile: a symbol (like "A") and a points value.
    # Single underscore = "protected" attribute (a convention for subclasses)
    def __init__(self, S, P):
        self._Symbol = S
        self._Points = P

    def GetPoints(self):
        return self._Points

    def GetSymbol(self):
        return self._Symbol

class Player():
    # A player: a name and a running score
    def __init__(self, N, S):
        self._Name = N
        self._Score = S

    def GetScore(self):
        return self._Score

    def GetName(self):
        return self._Name

    def ChangeScore(self, Change):
        self._Score += Change     # Change can be positive or negative

class Pile():
    # A stack of tiles. Index 0 of the list is the TOP of the pile.
    def __init__(self, M, B):
        self._Tiles = []      # the tiles currently in the pile
        self._Max = M         # maximum number of tiles allowed
        self._Bonus = B       # a bonus value (stored, but not used anywhere yet)

    def Add(self, T):
        # Put a tile on TOP of the pile (insert at position 0), if there's room.
        # If the pile is full the tile is silently ignored.
        if len(self._Tiles) < self._Max:
            self._Tiles.insert(0, T)

    def GetSymbolOfTopTile(self):
        # Looks at the top tile without removing it
        # (would crash with an IndexError if the pile is empty)
        return self._Tiles[0].GetSymbol()

    def Remove(self):
        # Takes the top tile off the pile and returns it
        Temp = self._Tiles[0]
        self._Tiles.pop(0)
        return Temp

    def Empty(self):
        # True if there are no tiles left in this pile
        if len(self._Tiles) == 0:
            return True
        else:
            return False

    def GetNumberOfTiles(self):
        return len(self._Tiles)

if __name__ == "__main__":
    Main()