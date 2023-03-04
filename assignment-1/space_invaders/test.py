import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# Set up the button
button_width = 100
button_height = 50
button_color = (255, 0, 0)
button_rect = pygame.Rect((width - button_width) // 2, (height - button_height) // 2, button_width, button_height)

# Set up the velocity of the button
velocity = [0, 2]

# Set up the clock
clock = pygame.time.Clock()

# Set the starting position of the button
start_pos = button_rect.centery

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the button
    button_rect.move_ip(velocity)

    # Bounce the button if it hits the top or bottom of the screen
    if button_rect.top <= start_pos - 40 or button_rect.bottom >= start_pos + 40:
        velocity[1] = -velocity[1]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)

    # Update the screen
    pygame.display.flip()

    # Wait for a short amount of time
    clock.tick(45)
