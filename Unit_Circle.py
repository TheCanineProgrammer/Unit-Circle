import pygame_textinput, pygame, math

pygame.init()

# Window Configuration
width = 500
height = 550
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("./Icon/ICON.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Unit Circle")
check = False

# Fonts & TextInput
font = pygame.font.Font("consola.ttf", 20)
font_help = pygame.font.Font("consola.ttf", 10)
manager = pygame_textinput.TextInputManager(validator = lambda x : (len(x) <= 21 and x.isdecimal()) or x == "")
textinput = pygame_textinput.TextInputVisualizer(manager = manager, font_object = font)
textinput.antialias = True
text = "Enter angle in degrees: "
text_surf = font.render(text, True, "black")
pygame.key.set_repeat(200, 55)

# FPS
clock = pygame.time.Clock()

# Functions
def convert_to_radians(degree : float) -> float:
    """
    According to R / pi = D / 180 formula
    """
    R = (degree / 180) * math.pi
    return R

# Main Loop
while True:
    screen.fill("#c3d2d6")
    events = pygame.event.get()
    textinput.update(events)
    screen.blit(text_surf, (5, width / 30))
    screen.blit(textinput.surface, (260, width / 30))
    x = 50
    y = 150
    gap = 10
    center = (width / 2, width / 2 + width / 6)
    x_center, y_center = center
    start_pos = pygame.math.Vector2(x_center, y_center)
    ###
    pygame.draw.circle(screen, color = "black", center = center, width = 2, radius = 150)
    ### Sine Axis
    pygame.draw.polygon(screen, "black", [(width/2, y_center - 200), (width / 2 + gap, y_center - 200 +gap), (width / 2 - gap, y_center - 200 +gap)])
    pygame.draw.line(screen, color = "black", start_pos = (width / 2, y_center - 200), end_pos = (width / 2, y_center + 200), width = 2)
    y_label = font.render("Sin(θ)", True, "black")
    screen.blit(y_label, (width / 2 + 20,  y_center-200))
    ### Cosine Axis
    pygame.draw.polygon(screen, "black", [(450, y_center), (450 - gap, y_center + gap), (450 - gap, y_center - gap)])
    pygame.draw.line(screen, color = "black", start_pos = (x, y_center), end_pos = (450, y_center), width = 2)
    x_label = font.render("Cos(θ)", True, "black")
    screen.blit(x_label, (430, y_center+10))
    ###
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            check = True
            if textinput.value == "":
                angle = 0
            else:
                angle = int(textinput.value) % 360
            radian = convert_to_radians(angle)

        if event.type == pygame.QUIT:
            exit()
    if check:
        if angle <= 90:
            x_axis = 150 * math.cos(radian)
            y_axis = 150 * math.sin(radian)
            end_pos = pygame.math.Vector2(x_center + x_axis, y_center - y_axis)
            line = pygame.draw.line(screen, "#f09102", start_pos, end_pos, width=2)
            help_y = pygame.draw.line(screen, "#0289f0", end_pos, (x_center, y_center - y_axis), 2)
            sin = font_help.render(f"{y_axis/150:0.3f}", True, "black")
            if (y_axis / 150) <= math.sin(math.pi / 4):
                screen.blit(sin, (x_center - 35, y_center - y_axis-10))
            else:
                screen.blit(sin, (x_center - 35, y_center - y_axis+8))
            cos = font_help.render(f"{x_axis / 150:0.3f}", True, "black")
            help_x = pygame.draw.line(screen, "#0289f0", end_pos, (x_center + x_axis, y_center), 2)
            if (x_axis / 150) >= math.cos(math.pi / 4):
                screen.blit(cos, (x_center + x_axis - 35, y_center + 10))
            else:
                screen.blit(cos, (x_center + x_axis + 10, y_center + 10))
        elif angle > 90 and angle <= 180:
            x_axis = 150 * math.cos(radian)
            y_axis = 150 * math.sin(radian)
            end_pos = pygame.math.Vector2(x_center + x_axis, y_center - y_axis)
            line = pygame.draw.line(screen, "#f09102", start_pos, end_pos, width=2)
            help_y = pygame.draw.line(screen, "#0289f0", end_pos, (x_center, y_center - y_axis), 2)
            sin = font_help.render(f"{y_axis/150:0.3f}", True, "black")
            if (y_axis / 150) >= math.sin(3 * math.pi / 4):
                screen.blit(sin, (x_center + 10, y_center - y_axis + 5))
            else:
                screen.blit(sin, (x_center + 10, y_center - y_axis - 10))
            cos = font_help.render(f"{x_axis / 150:0.3f}", True, "black")
            if (x_axis / 150) >= math.cos(3 * math.pi/4):
                screen.blit(cos, (x_center + x_axis - 35, y_center + 10))
            else:
                screen.blit(cos, (x_center + x_axis + 5, y_center + 10))
            help_x = pygame.draw.line(screen, "#0289f0", end_pos, (x_center + x_axis, y_center), 2)
        elif angle > 180 and angle <= 270:
            x_axis = 150 * math.cos(radian)
            y_axis = 150 * math.sin(radian)
            end_pos = pygame.math.Vector2(x_center + x_axis, y_center - y_axis)
            line = pygame.draw.line(screen, "#f09102", start_pos, end_pos, width=2)
            help_y = pygame.draw.line(screen, "#0289f0", end_pos, (x_center, y_center - y_axis), 2)
            help_x = pygame.draw.line(screen, "#0289f0", end_pos, (x_center + x_axis, y_center), 2)
            sin = font_help.render(f"{y_axis/150:0.3f}", True, "black")
            if (y_axis / 150) >= math.sin(1.25 * math.pi):
                screen.blit(sin, (x_center + 10, y_center - y_axis + 5))
            else:
                screen.blit(sin, (x_center + 10, y_center - y_axis - 20))
            cos = font_help.render(f"{x_axis / 150:0.3f}", True, "black")
            if (x_axis / 150) >= math.cos(3 * math.pi/4):
                screen.blit(cos, (x_center + x_axis - 35, y_center - 10))
            else:
                screen.blit(cos, (x_center + x_axis + 5, y_center - 10))
            help_x = pygame.draw.line(screen, "#0289f0", end_pos, (x_center + x_axis, y_center), 2)
        elif angle > 270 and angle <= 360:
            x_axis = 150 * math.cos(radian)
            y_axis = 150 * math.sin(radian)
            end_pos = pygame.math.Vector2(x_center + x_axis, y_center - y_axis)
            line = pygame.draw.line(screen, "#f09102", start_pos, end_pos, width=2)
            help_y = pygame.draw.line(screen, "#0289f0", end_pos, (x_center, y_center - y_axis), 2)
            sin = font_help.render(f"{y_axis/150:0.3f}", True, "black")
            if (y_axis / 150) <= math.sin(1.75 * math.pi):
                screen.blit(sin, (x_center - 38, y_center - y_axis-15))
            else:
                screen.blit(sin, (x_center - 38, y_center - y_axis+8))
            cos = font_help.render(f"{x_axis / 150:0.3f}", True, "black")
            help_x = pygame.draw.line(screen, "#0289f0", end_pos, (x_center + x_axis, y_center), 2)
            if (x_axis / 150) >= math.cos(1.75 * math.pi):
                screen.blit(cos, (x_center + x_axis - 35, y_center - 10))
            else:
                screen.blit(cos, (x_center + x_axis + 10, y_center - 10))

    pygame.display.update()
    clock.tick(30)