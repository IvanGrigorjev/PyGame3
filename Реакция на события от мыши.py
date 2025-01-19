import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
FPS = 30
COLORS = ['black', 'red', 'blue']


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
        self.colors = ['black', 'red', 'blue']

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, self.colors[self.board[y][x]], (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, 'white', (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size), 1)

    #  метод возвращает координаты клетки
    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and \
                self.top <= mouse_pos[0] < self.top + self.width * self.cell_size:
            return (int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size))
        else:
            return None

    # метод изменяет поле, опираясь на полученные координаты клетки
    def on_click(self, cell_coords):
        if cell_coords:
            # print(self.board)
            self.board[cell_coords[0]][cell_coords[1]] = (self.board[cell_coords[0]][cell_coords[1]] + 1) % 3

    # метод - диспетчер, который получает событие нажатия и вызывает первые два метода
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Чёрное в белое и наоборот')

    board = Board(5, 7)
    # board.set_view(100, 100, 50)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
