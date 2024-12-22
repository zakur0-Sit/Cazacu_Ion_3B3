import pygame
import sys


BUTTON_COLOR = (240, 217, 181)
BUTTON_COLOR_HOVER = (255, 196, 137)
TEXT_COLOR = (0, 0, 0)
FONT = "fonts/Japan Daisuki.otf"
MENU_BACKGROUND = pygame.image.load("images/bg3.png")

SCREEN_SIZE = (1200, 800)
MIN_SCREEN_SIZE = (800, 800)
MARGIN = 50
BACKGROUND = pygame.image.load("images/bg1.jpg")
BG_MUSIC = "sounds/bg.wav"
ICON = pygame.image.load("images/go.png")
GRID_SIZES = {(800, 1000): 700, (1000, 1200): 900, (1200, float("inf")): 1100}
GRID_BACKGROUND_COLOR = (240, 217, 181, 180)
LINE_COLOR = (0, 0, 0)
DOT_RADIUS = 5
DOT_COLOR = (0, 0, 0)
BLACK_STONE_COLOR = (0, 0, 0)
WHITE_STONE_COLOR = (255, 255, 255)

def draw_button(screen, text, position, size, hover):
    font = pygame.font.SysFont(FONT, size)
    color = BUTTON_COLOR_HOVER if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, position, border_radius=10)
    button_text = font.render(text, True, TEXT_COLOR)
    text_position = button_text.get_rect(center=(position[0] + position[2] // 2, position[1] + position[3] // 2))
    screen.blit(button_text, text_position)

def menu():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("The Game of Go")
    pygame.display.set_icon(ICON)
    bg_music = pygame.mixer.Sound(BG_MUSIC)
    bg_music.set_volume(0.3)
    bg_music.play(-1)

    title_font = pygame.font.Font(FONT, 72)
    button_width, button_height = 350, 70
    button_margin = 20
    buttons = [
        {"text": "Expert : 19 x 19", "size": 19, "stones": 15},
        {"text": "Intermediate : 13 x 13", "size": 13, "stones": 23},
        {"text": "Beginner : 9 x 9", "size": 9, "stones": 33},
        {"text": "Quit", "size": None}
    ]
    button_positions = []

    for i, button in enumerate(buttons):
        position_x = (SCREEN_SIZE[0] - button_width) // 2
        position_y = (SCREEN_SIZE[1] - button_height) // 2 + i * (button_height + button_margin)
        button_positions.append(pygame.Rect(position_x, position_y, button_width, button_height))

    running = True
    selected_size = None
    stones_radius = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        menu_background = pygame.transform.scale(MENU_BACKGROUND, (2000, 1200))
        screen.blit(menu_background, (0, 0))
        title_text = title_font.render("The Game of Go", True, TEXT_COLOR)
        title_position = title_text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 4))
        screen.blit(title_text, title_position)

        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        for i, button in enumerate(button_positions):
            hover = button.collidepoint(mouse_position)
            draw_button(screen, buttons[i]["text"], button, 36, hover)
            if hover and mouse_click:
                if buttons[i]["size"] is None:
                    pygame.quit()
                    sys.exit()
                else:
                    selected_size = buttons[i]["size"]
                    stones_radius = buttons[i]["stones"]
                    running = False

        pygame.display.update()
    return selected_size, stones_radius, screen.get_size()

def get_grid_size(window_width, window_height):
    min_dim = min(window_width, window_height)
    for (low, high), grid_size in GRID_SIZES.items():
        if low <= min_dim < high:
            return grid_size
    return 500

def get_star_points(grid_lines):
    if grid_lines == 19:
        return [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
    elif grid_lines == 13:
        return [(3, 3), (3, 9), (9, 3), (9, 9), (6, 6)]
    elif grid_lines == 9:
        return [(4, 4)]

def draw_star_points(screen, grid_size, grid_lines, grid_start_x, grid_start_y):
    lines_steep = grid_size/(grid_lines - 1)
    star_points = get_star_points(grid_lines)

    for star_point in star_points:
        position_x = grid_start_x + star_point[0] * lines_steep + 1
        position_y = grid_start_y + star_point[1] * lines_steep + 1
        pygame.draw.circle(screen, DOT_COLOR, (position_x, position_y), DOT_RADIUS)

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

    draw_star_points(screen, grid_size, grid_lines, grid_start_x, grid_start_y)

    return grid_start_x, grid_start_y, lines_step

def get_neighbours(col, row, grid_lines):
    neighbours = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_col, new_row = col + dx, row + dy
        if 0 <= new_col < grid_lines and 0 <= new_row < grid_lines:
            neighbours.append((new_col, new_row))
    return neighbours

def get_group_and_liberties(col, row, player, stones, grid_lines):
    queue = [(col, row)]
    group = set()
    liberties = set()

    while queue:
        c, r = queue.pop(0)
        if (c, r) in group:
            continue
        group.add((c, r))
        for neighbour in get_neighbours(c, r, grid_lines):
            if neighbour in group:
                continue
            if neighbour in stones and stones[neighbour] == player:
                queue.append(neighbour)
            elif neighbour not in stones:
                liberties.add(neighbour)

    return group, liberties

def remove_group(group, stones):
    for pos in group:
        del stones[pos]

def main():
    pygame.init()

    grid_lines, stones_radius, screen_size = menu()

    bg_music = pygame.mixer.Sound(BG_MUSIC)
    bg_music.set_volume(0.3)
    bg_music.play(-1)
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption("The Game of Go")
    pygame.display.set_icon(ICON)
    window_size = SCREEN_SIZE

    stones = {}
    current_player = 1  # black
    grid_size = get_grid_size(window_size[0], window_size[1])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width = max(event.w, MIN_SCREEN_SIZE[0])
                height = max(event.h, MIN_SCREEN_SIZE[1])
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                window_size = (width, height)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_start_x, grid_start_y, lines_step = draw_board(screen, grid_size, grid_lines, window_size)
                col = round((mouse_x - grid_start_x) / lines_step)
                row = round((mouse_y - grid_start_y) / lines_step)
                if 0 <= col < grid_lines and 0 <= row < grid_lines and (col, row) not in stones:
                    stones[(col, row)] = current_player

                    for neighbour in get_neighbours(col, row, grid_lines):
                        if neighbour in stones and stones[neighbour] != current_player:
                            group, liberties = get_group_and_liberties(neighbour[0], neighbour[1], stones[neighbour], stones, grid_lines)
                            if not liberties:
                                remove_group(group, stones)

                    group, liberties = get_group_and_liberties(col, row, current_player, stones, grid_lines)
                    if not liberties:
                        del stones[(col, row)]
                    else:
                        current_player = 3 - current_player

        grid_size = get_grid_size(window_size[0], window_size[1])
        background = pygame.transform.scale(BACKGROUND, window_size)
        screen.blit(background, (0, 0))

        grid_start_x, grid_start_y, lines_step = draw_board(screen, grid_size, grid_lines, window_size)

        for (col, row), player in stones.items():
            stone_x_pos = grid_start_x + col * lines_step
            stone_y_pos = grid_start_y + row * lines_step
            stone_color = BLACK_STONE_COLOR if player == 1 else WHITE_STONE_COLOR
            pygame.draw.circle(screen, stone_color, (int(stone_x_pos), int(stone_y_pos)), stones_radius)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
