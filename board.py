import pygame

class Board:
	def __init__(self, board, color, grid_size=3, cell_size=50):
		self.grid_size = grid_size  # Antal rader och kolumner i gridet (t.ex. 3x3)
		self.cell_size = cell_size  # Storlek på varje cell
		self.grid = [[None] * grid_size for _ in range(grid_size)]  # Initialisera gridet med None
		self.board = board
		self.color = color

	def draw(self, screen):
		"""Ritar hela brädet på skärmen."""
		# Beräkna den totala bredden och höjden på gridet
		total_width = self.cell_size * self.grid_size * 1.2
		total_height = self.cell_size * self.grid_size * 1.1

		# Beräkna startpositionen för att centrera gridet på skärmen
		start_x = (screen.get_width() - total_width) // 2
		start_y = ((screen.get_height() - total_height) // 2) + (150 * self.board)

		# Rita varje cell i gridet
		for row in range(self.grid_size):
			for col in range(self.grid_size):
				rect_x = start_x + (col * 1.2) * self.cell_size
				rect_y = start_y + (row * 1.1) * self.cell_size
				pygame.draw.rect(screen, self.color, [rect_x, rect_y, self.cell_size, self.cell_size])  # Rita rektangeln
