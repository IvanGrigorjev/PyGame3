import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
FPS = 30


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = pygame.Color(255, 255, 255)
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, color, (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                 self.cell_size, self.cell_size), 1)



def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    board = Board(4, 3)
    board.set_view(100, 100, 50)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
