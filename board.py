class Board:
    def __init__(self):
        self.grid = [[None] * 3 for _ in range(3)]  # 3x3 rutnät

    def place_dice(self, row, col, dice_value):
        """Placera en tärning på brädet."""
        if self.grid[row][col] is None:
            self.grid[row][col] = dice_value
            return True
        return False

    def display(self):
        """Visa brädet i konsolen (kan ersättas med grafisk representation)."""
        for row in self.grid:
            print(" | ".join(str(cell) if cell else " " for cell in row))
