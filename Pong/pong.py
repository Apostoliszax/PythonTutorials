import pygame
import random
import functions

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)

# Paddle constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

# Ball constants
BALL_SIZE = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Create the game window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pong")

# Initialize variables
player1_score = 0
player2_score = 0

# Create paddles and ball
player1, player2, ball = functions.createPaddlesAndBall(WIDTH, HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE)

# Initialize ball direction
ball_direction = [random.choice((1, -1)), random.choice((1, -1))]

# Game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or player1_score == 5 or player2_score == 5 : 
            game_over = True
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED_X * ball_direction[0]
    ball.y += BALL_SPEED_Y * ball_direction[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction[1] *= -1

    # Ball collisions with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_direction[0] *= -1

    # Ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_direction[0] *= -1
    elif ball.right >= WIDTH:
        player1_score += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_direction[0] *= -1


    BLACK = (0, 0, 0)

    # Clear the screen
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, player1)
    pygame.draw.rect(window, WHITE, player2)
    pygame.draw.ellipse(window, WHITE, ball)

    # Display scores
    font = pygame.font.Font(None, 36)
    text1 = font.render(f"Player 1: {player1_score}", True, WHITE)
    text2 = font.render(f"Player 2: {player2_score}", True, WHITE)
    window.blit(text1, (20, 20))
    window.blit(text2, (WIDTH - 180, 20))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
