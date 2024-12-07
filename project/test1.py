import pygame

SCREEN_SIZE = (800, 800)
MIN_SCREEN_SIZE = (800, 800)
MARGIN = 50
BACKGROUND = pygame.image.load("images/bg1.jpg")
BG_MUSIC = "sounds/bg.wav"
ICON = pygame.image.load("images/go.png")
GRID_BACKGROUND_COLOR = (240, 217, 181, 180)
LINE_COLOR = (0, 0, 0)
GRID_SIZES = {(800, 1000): 700, (1000, 1200): 900, (1200, float("inf")): 1100}

def get_grid_size(window_width, window_height):
    min_dim = min(window_width, window_height)
    for (low, high), grid_size in GRID_SIZES.items():
        if low <= min_dim < high:
            return grid_size
    return 500

def draw_board(screen, grid_size, grid_lines, window_size):
    window_width, window_height = window_size

    grid_start_x = (window_width - grid_size) // 2
    grid_start_y = (window_height - grid_size) // 2

    grid_end_x, grid_end_y = grid_start_x + grid_size, grid_start_y + grid_size

    grid_surface = pygame.Surface((grid_size, grid_size), pygame.SRCALPHA)
    grid_surface.fill(GRID_BACKGROUND_COLOR)
    screen.blit(grid_surface, (grid_start_x, grid_start_y))

    lines_step = grid_size / (grid_lines - 1)

    for i in range(grid_lines):
        position_x = grid_start_x + i * lines_step
        position_y = grid_start_y + i * lines_step
        pygame.draw.line(screen, LINE_COLOR, (grid_start_x, position_y), (grid_end_x, position_y), 2)
        pygame.draw.line(screen, LINE_COLOR, (position_x, grid_start_y), (position_x, grid_end_y), 2)


def main():
    pygame.init()

    bg_music = pygame.mixer.Sound(BG_MUSIC)
    bg_music.set_volume(0.3)
    bg_music.play(-1)
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("The Game of Go")
    pygame.display.set_icon(ICON)
    window_size = SCREEN_SIZE

    grid_lines = 19

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    grid_lines = 19
                elif event.key == pygame.K_2:
                    grid_lines = 13
                elif event.key == pygame.K_3:
                    grid_lines = 9
            elif event.type == pygame.VIDEORESIZE:
                width = max(event.w, MIN_SCREEN_SIZE[0])
                height = max(event.h, MIN_SCREEN_SIZE[1])
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                window_size = (width, height)

        grid_size = get_grid_size(window_size[0], window_size[1])
        background = pygame.transform.scale(BACKGROUND, window_size)
        screen.blit(background, (0, 0))

        draw_board(screen, grid_size, grid_lines, window_size)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
