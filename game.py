# knucklebones.py
import pygame
import sys

from board import Board
from player import Player
from dice import Dice

class Knucklebones:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1000, 600))
		pygame.display.set_caption("Knucklebones")
		self.running = True

		# Skapa två spelare
		self.players = [Player("Player 1"), Player("Player 2")]
		self.current_player = 0

		# Skapa två bräden
		self.board1 = Board(1, (0, 225, 0))
		self.board2 = Board(-1, (225, 0, 0))

	def handle_events(self):
		"""Hantera händelser."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def update(self):
		"""Uppdatera spelets tillstånd."""
		pass  # Lägg till spelmekanik här

	def draw(self):
		"""Rita på skärmen."""
		self.screen.fill((16, 0, 22))  # Färga skärmen svart

		# Rita båda bräden
		self.board1.draw(self.screen)
		self.board2.draw(self.screen)

		pygame.display.flip()

							
	# def play_turn(self):
  # 	"""Spela en omgång."""
  #   player = self.players[self.current_player]
  #   print(f"{player.name}'s turn!")
		
  #   dice_value = Dice.roll()
  #   print(f"Rolled: {dice_value}")
		
  #   row, col = map(int, input("Enter row and column (e.g., 0 1): ").split())
  #   if self.board.place_dice(row, col, dice_value):
  #       print("Dice placed successfully!")
  #       self.board.display()
  #       self.current_player = (self.current_player + 1) % len(self.players)
  #   else:
  #       print("Invalid move. Try again!")

	def run(self):
		"""Huvudloop."""

		while self.running:
				self.handle_events()
				self.update()
				self.draw()
		self.quit()

	def quit(self):
		"""Avsluta spelet."""
		pygame.quit()
		sys.exit()


if __name__ == "__main__":
    game = Knucklebones()
    game.run()
