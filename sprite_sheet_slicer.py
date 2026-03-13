import pygame

pygame.init()



# Window
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

sprite_sheet = pygame.image.load("assets/Warrior_Sheet-Effect.png").convert_alpha()

# Using default font, size 30
font = pygame.font.Font(None, 36)

frames = []

sheet_width, sheet_height = sprite_sheet.get_size()

frame_width = sheet_width // 6   ## Num of Sprites horizontally
frame_height = sheet_height // 17 ## Num Sprites vertically

for y in range(0, sheet_height, frame_height):
    for x in range(0, sheet_width, frame_width):
        rect = pygame.Rect(x, y, frame_width, frame_height)
        frame = sprite_sheet.subsurface(rect)
        frame = pygame.transform.scale(frame, (frame_width*4, frame_height*4))
        frames.append(frame)

animation_defs = [
    (0,5,"idle"),
    (6,13,"run"),
    (14,21,"first_attack"),
    (21,25,"second attack"),
    (26,36,"death"),
    (37,40,"hurt"),
    (41,48,"jump"),
    (49,51,"wall_hit"),
    (51,59,"wall_cling"),
    (60,62,"wall_slide"),
    (63,63,"crouch_start"),
    (64,67,"crouch"),
    (68,68,"uncrouch"),
    (69,72,"dash"),
    (73,76,"slide"),
    (77,83,"slide_attack"),
    (84,89,"sweep"),
    (90,90,"sweep_recovery"),
    (91,98,"climb")
]

animations = {}

for start, end, name in animation_defs:
    animations[name] = frames[start:end+1]

animation_names = list(animations.keys())

current_animation_idx = 0
current_animation_name = animation_names[0]
current_frame = 0

animation_speed = 0.15
frame_timer = 0

## FPS 24

running = True

animating = False

while running:

    dt = clock.tick(60) / 1000  # delta time

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animating = not animating  ## Should toggle animation playing or not playing
            if event.key == pygame.K_RIGHT:
                current_animation_idx = (current_animation_idx + 1) % len(animations)
                current_animation_name = animation_names[current_animation_idx]
                current_frame = 0
            if event.key == pygame.K_LEFT:
                current_animation_idx = (current_animation_idx - 1) % len(animations)
                current_animation_name = animation_names[current_animation_idx]
                current_frame = 0

        if event.type == pygame.QUIT:
            running = False

    if animating:
        current_frame = (current_frame + 1) % len(animations[current_animation_name])

    image = animations[current_animation_name][current_frame]

    # draw
    screen.fill((30, 30, 30))
    screen.blit(image, (400, 300))

    frame_text = font.render(f"Frame: {current_frame}", True, (255, 255, 255))
    screen.blit(frame_text, (10, 10))

    anim_text = font.render(f"animation: {current_animation_name}", True, (255, 255, 255))
    screen.blit(anim_text, (10, 30))

    pygame.display.flip()
    clock.tick(12)

pygame.quit()