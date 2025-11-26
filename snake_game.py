import pygame
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
GRAY = (50, 50, 50)

# Direction enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        # Prevent reversing direction
        dx_curr, dy_curr = self.direction.value
        dx_new, dy_new = new_direction.value
        if (dx_curr, dy_curr) != (-dx_new, -dy_new):
            self.direction = new_direction

    def check_collision(self):
        head_x, head_y = self.body[0]

        # Wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True

        # Self collision
        if self.body[0] in self.body[1:]:
            return True

        return False

    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            self.grow = True
            return True
        return False

    def draw(self, screen):
        for i, (x, y) in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)

    def respawn(self, snake_body):
        while True:
            self.position = self.randomize_position()
            if self.position not in snake_body:
                break

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.food.respawn(self.snake.body)  # Ensure food doesn't spawn on snake
        self.score = 0
        self.game_over = False
        self.level = 1
        self.fps = 3
        self.food_count = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)

        return True

    def update(self):
        if not self.game_over:
            self.snake.move()

            if self.snake.eat_food(self.food.position):
                self.score += 10
                self.food_count += 1
                self.food.respawn(self.snake.body)

                # Level up every 10 food items
                if self.food_count % 10 == 0:
                    self.level += 1
                    self.fps += 1  # Increase speed by 1 FPS per level

            if self.snake.check_collision():
                self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)

        # Draw grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))

        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        # Draw score and level
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))

        # Draw game over screen
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, RED)
            restart_text = self.font.render("Press SPACE to restart", True, WHITE)

            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))

            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)  # Dynamic FPS based on level

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
