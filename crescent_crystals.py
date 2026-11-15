#!/usr/bin/env python3

import pygame
pygame.init()

class Question:
    def __init__(self, q_text, id, a_text, b_text, effects=None):
        if effects is None:
          	effects = []
        self.q = q_text
        self.id = id
        self.a = a_text
        self.b = b_text
        self.effects = effects

Q = Question("Where do you choose to go?", "Q", "Space Station.", "Outside.")
AQ = Question("You discover an O2 tank. What do you do next?", "AQ", "Explore the\nAdmin room.", "Go outside.")
AAQ = Question("Admin tells you to go outside. You are tipped off about the\nlocation of a food source south. What do you do once outside?", "AAQ", "Go explore North.", "Go South.", ["+1C"])
AAAQ = Question("You find a broken rover. What do you do?", "AAAQ", "Fix it.", "Continue exploring.", ["+1C"])
AAAAQ = Question("You return to the Space Station. Your mission is set\nto end soon. What do you do to prepare?", "AAAAQ", "Go to the cafeteria\nand have dinner.", "Analyse moon dust\nsamples.", ["-10R"])
AAAAAQ = Question("You found ending 1/32!", "AAAAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10F"])
AAAABQ = Question("You found ending 2/32!", "AAAABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
AAABQ = Question("You find a med kit. This was unexpected, so you rush back\nto report to Admin. What do you do along the way?", "AAABQ", "Stop and investigate\na crater.", "Rush to report\nthe news.", ["-10R", "+1C"])
AAABAQ = Question("You found ending 3/32!", "AAABAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
AAABBQ = Question("You found ending 4/32!", "AAABBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O"])
AABQ = Question("After finding the food, you hear a strange noise nearby.\nWhat do you do?", "AABQ", "Call the Space Station\non your radio.", "You check out\nthe source.", ["+10F", "+15R"])
AABAQ = Question("They tell you to go back inside.", "AABAQ", "Obey.", "You disregard their advice\nand continue exploring.", ["+15R"])
AABAAQ = Question("You found ending 5/32!", "AABAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O"])
AABABQ = Question("You found ending 6/32!", "AABABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C", "+15R"])
AABBQ = Question("You find a cute little green guy. What do you do?", "AABBQ", "Try to befriend him.", "Attack him.", ["+1C"])
AABBAQ = Question("You found ending 7/32!", "AABBAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+15F"])
AABBBQ = Question("You found ending 8/32!", "AABBBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+20R", "+1C"])
ABQ = Question("What do you do once outside?", "ABQ", "Explore a nearby crater.", "Find a bunker.", ["+15R"])
ABAQ = Question("You find a broken rover. What do you do?", "ABAQ", "Fix it.", "Continue exploring.", ["+1C"])
ABAAQ = Question("You report back on your findings via radio.", "ABAAQ", "You return to the\nSpace Station.", "You continue exploring.", ["-10R"])
ABAAAQ = Question("You found ending 9/32!", "ABAAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O"])
ABAABQ = Question("You found ending 10/32!", "ABAABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
ABABQ = Question("You find a little blue guy.", "ABABQ", "Introduce yourself.", "Leave him alone\nand move on.", ["+1C"])
ABABAQ = Question("You found ending 11/32!", "ABABAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+20R", "-15F"])
ABABBQ = Question("You found ending 12/32!", "ABABBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
ABBQ = Question("What do you do inside?", "ABBQ", "Look around for\nsome food.", "Reorganise the\nsupplies.", ["-10R"])
ABBAQ = Question("You leave the bunker. You hear a strange noise nearby.\nWhat do you do?", "ABBAQ", "Call the Space Station\non your radio.", "You check out\nthe source.", ["+10F", "+10O"])
ABBAAQ = Question("You found ending 13/32!", "ABBAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+15R"])
ABBABQ = Question("You found ending 14/32!", "ABBABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
ABBBQ = Question("You find a map of previously undiscovered places.", "ABBBQ", "Explore them yourself.", "Wait for more\nastronauts to arrive.", ["+1C"])
ABBBAQ = Question("You found ending 15/32!", "ABBBAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C", "+15R"])
ABBBBQ = Question("You found ending 16/32!", "ABBBBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O"])
BQ = Question("You see footprints leading away. What do you do?", "BQ", "Follow them.", "Explore according to\nyour mission.", ["+1C", "+15R"])
BAQ = Question("You find another astronaut. They ask to share resources.", "BAQ", "Share.", "Refuse and head\nback inside.", ["+15R"])
BAAQ = Question("You and the astronaut become friends. You both run into a\ncute little green guy offering you an O2 tank.", "BAAQ", "Take it.", "Refuse and keep\nexploring.", ["+1C"])
BAAAQ = Question("You find a mysterious cavern.", "BAAAQ", "You go in first.", "The other astronaut\ngoes in first.", ["+20O", "-15R"])
BAAAAQ = Question("You found ending 17/32!", "BAAAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BAAABQ = Question("You found ending 18/32!", "BAAABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+15R", "+10F"])
BAABQ = Question("You find a mysterious cavern.", "BAABQ", "You go in first.", "The other astronaut\ngoes in first.", ["+1C"])
BAABAQ = Question("You found ending 19/32!\nUnfortunately, you did not survive your mission.", "BAABAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+100R"])
BAABBQ = Question("You found ending 20/32!\nUnfortunately, the other astronaut did not make it out alive.", "BAABBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BABQ = Question("What do you do inside?", "BABQ", "Look around for\nsome food.", "Reorganise the supplies.", ["-10R"])
BABAQ = Question("Admin finds your digital journal in which you complain\nabout your mission.", "BABAQ", "Say it belongs to\nthe other astronaut.", "Confess.", ["+10F", "+10O"])
BABAAQ = Question("You found ending 21/32!", "BABAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+15R"])
BABABQ = Question("You found ending 22/32!", "BABABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BABBQ = Question("You find a little blue guy hidden amongst boxes.", "BABBQ", "Escort him outside.", "Lock him inside and\nawait further instructions.", ["+1C"])
BABBAQ = Question("You found ending 23/32!", "BABBAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+20R"])
BABBBQ = Question("You found ending 24/32!", "BABBBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BBQ = Question("You end up at a cross roads.", "BBQ", "Go right.", "Go left.", ["+1C"])
BBAQ = Question("You are starting to feel back pain.", "BBAQ", "Empty your O2 tank.", "Take a deep breath.", ["+1C"])
BBAAQ = Question("A little shimmering rainbow guy pops up of the tank\nand heals you.", "BBAAQ", "Do a little dance\nwith him.", "Thank him kindly.", ["+100O", "+100F", "-100R"])
BBAAAQ = Question("You found ending 25/32!", "BBAAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BBAABQ = Question("You found ending 26/32!", "BBAABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["-30R"])
BBABQ = Question("You trip over air and injure yourself.\nYou wonder why NASA hired you.", "BBABQ", "You lie in the dirt\nfor a while but\nultimately get up.", "You call via radio\nfor help.", ["+30O", "+1C"])
BBABAQ = Question("You found ending 27/32!", "BBABAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C"])
BBABBQ = Question("You found ending 28/32!", "BBABBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+15R"])
BBBQ = Question("You find a box with a map of previously undiscovered places.", "BBBQ", "Explore them by\nyourself.", "Wait for more\nastronauts to arrive.", ["+15R"])
BBBAQ = Question("You find a couple suspicious Mars bars\nthat drifted from another planet.", "BBBAQ", "Eat them.", "Go back to the lab\nand analyse them.", ["+1C"])
BBBAAQ = Question("You found ending 29/32!", "BBBAAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10F", "+15R"])
BBBABQ = Question("You found ending 30/32!", "BBBABQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O", "+1C"])
BBBBQ = Question("What do you do once they arrive?", "BBBBQ", "Go back inside\nand wait.", "Help them explore.", ["+15R"])
BBBBAQ = Question("You found ending 31/32!", "BBBBAQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+10O"])
BBBBBQ = Question("You found ending 32/32!", "BBBBBQ", "TRY\nAGAIN", "TRY\nAGAIN", ["+1C", "+15R"])
D = Question("You did not survive your mission.", "D", "TRY\nAGAIN", "TRY\nAGAIN")

d = { "Q": Q,
    "AQ": AQ,
    "AAQ": AAQ,
    "AAAQ": AAAQ,
    "AAAAQ": AAAAQ,
    "AAAAAQ": AAAAAQ,
    "AAAABQ": AAAABQ,
    "AAABQ": AAABQ,
    "AAABAQ": AAABAQ,
    "AAABBQ": AAABBQ,
    "AABQ": AABQ,
    "AABAQ": AABAQ,
    "AABAAQ": AABAAQ,
    "AABABQ": AABABQ,
    "AABBQ": AABBQ,
    "AABBAQ": AABBAQ,
    "AABBBQ": AABBBQ,
    "ABQ": ABQ,
    "ABAQ": ABAQ,
    "ABAAQ": ABAAQ,
    "ABAAAQ": ABAAAQ,
    "ABAABQ": ABAABQ,
    "ABABQ": ABABQ,
    "ABABAQ": ABABAQ,
    "ABABBQ": ABABBQ,
    "ABBQ": ABBQ,
    "ABBAQ": ABBAQ,
    "ABBAAQ": ABBAAQ,
    "ABBABQ": ABBABQ,
    "ABBBQ": ABBBQ,
    "ABBBAQ": ABBBAQ,
    "ABBBBQ": ABBBBQ,
    "BQ": BQ,
    "BAQ": BAQ,
    "BAAQ": BAAQ,
    "BAAAQ": BAAAQ,
    "BAAAAQ": BAAAAQ,
    "BAAABQ": BAAABQ,
    "BAABQ": BAABQ,
    "BAABAQ": BAABAQ,
    "BAABBQ": BAABBQ,
    "BABQ": BABQ,
    "BABAQ": BABAQ,
    "BABAAQ": BABAAQ,
    "BABABQ": BABABQ,
    "BABBQ": BABBQ,
    "BABBAQ": BABBAQ,
    "BABBBQ": BABBBQ,
    "BBQ": BBQ,
    "BBAQ": BBAQ,
    "BBAAQ": BBAAQ,
    "BBAAAQ": BBAAAQ,
    "BBAABQ": BBAABQ,
    "BBABQ": BBABQ,
    "BBABAQ": BBABAQ,
    "BBABBQ": BBABBQ,
    "BBBQ": BBBQ,
    "BBBAQ": BBBAQ,
    "BBBAAQ": BBBAAQ,
    "BBBABQ": BBBABQ,
    "BBBBQ": BBBBQ,
    "BBBBAQ": BBBBAQ,
    "BBBBBQ": BBBBBQ,
    "D": D}

screen = pygame.display.set_mode((900, 750))
pygame.display.set_caption("Crescent Crystals")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()

bg_image = pygame.image.load('images/space_station.jpg')

crystals = 0
foodsupply = 100
radiation = 0
oxygen = 100
running = True

bordertop = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT/12), pygame.SRCALPHA)
bordertop.fill((0, 0, 0, 180))

borderbottom = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT/12), pygame.SRCALPHA)
borderbottom.fill((0, 0, 0, 180))

mouse = pygame.mouse.get_pos()
colour_light = (170,170,170)
colour_dark = (100,100,100)

button_left = pygame.Rect(0, 0, SCREEN_WIDTH/4, SCREEN_HEIGHT/3)
button_left.center = (SCREEN_WIDTH/5.5, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/30)

button_right = pygame.Rect(0, 0, SCREEN_WIDTH/4, SCREEN_HEIGHT/3)
button_right.center = (SCREEN_WIDTH*4.5/5.5, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/30)

def draw_gradient_button(rect, top_colour, bottom_colour, hovered):
    gradient = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)

    for y in range(rect.height):
        amount = y / rect.height

        colour = (
            int(top_colour[0] + (bottom_colour[0] - top_colour[0]) * amount),
            int(top_colour[1] + (bottom_colour[1] - top_colour[1]) * amount),
            int(top_colour[2] + (bottom_colour[2] - top_colour[2]) * amount)
        )

        if hovered:
            colour = (
                min(colour[0] + 30, 255),
                min(colour[1] + 30, 255),
                min(colour[2] + 30, 255)
            )

        pygame.draw.line(gradient, colour, (0, y), (rect.width, y))

    mask = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255, 255, 255, 255), mask.get_rect(), border_radius=15)

    gradient.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(gradient, rect)

curr_q = Q

bg_music = pygame.mixer.Sound("sounds/bg_music.mp3")

find_crystal = pygame.mixer.Sound("sounds/find_crystal.mp3")
end_music = pygame.mixer.Sound("sounds/end_music.mp3")
alien = pygame.mixer.Sound("sounds/alien.mp3")
alien_qs = [AABBQ, ABABQ, BAAQ, BABBQ, BBAAQ]

while running:
    
    bg_music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_left.collidepoint(event.pos):
                try:
                    curr_q = d[curr_q.id[:-1] + "A" + curr_q.id[-1]]
                    if curr_q in alien_qs:
                        alien.play()
                    if len(curr_q.id) == 6 or curr_q == D:
                        end_music.play()
                    oxygen -= 5
                    foodsupply -= 5
                    for item in curr_q.effects:
                        resc = item[-1]
                        amount = item[:-1]
                        if resc == "C":
                            find_crystal.play()
                            crystals += int(amount)
                        elif resc == "F":
                            foodsupply += int(amount)
                        elif resc == "O":
                            oxygen += int(amount)
                        else:
                            radiation += int(amount)
                    if (foodsupply <= 0 or oxygen <= 0 or radiation >= 100) and curr_q != BAABAQ:
                        curr_q = D
                    if foodsupply > 100:
                        foodsupply = 100
                    elif foodsupply < 0:
                        foodsupply = 0
                    if oxygen > 100:
                        oxygen = 100
                    elif oxygen < 0:
                        oxygen = 0
                    if radiation < 0:
                        radiation = 0
                    elif radiation > 100:
                        radiation = 100
                except KeyError:
                    curr_q = Q
                    crystals = 0
                    foodsupply = 100
                    radiation = 0
                    oxygen = 100

            elif button_right.collidepoint(event.pos):
                try:
                    curr_q = d[curr_q.id[:-1] + "B" + curr_q.id[-1]]
                    if curr_q in alien_qs:
                        alien.play()
                    if len(curr_q.id) == 6 or curr_q == D:
                        end_music.play()
                    oxygen -= 5
                    foodsupply -= 5
                    for item in curr_q.effects:
                        resc = item[-1]
                        amount = item[:-1]
                        if resc == "C":
                            find_crystal.play()
                            crystals += int(amount)
                        elif resc == "F":
                            foodsupply += int(amount)
                        elif resc == "O":
                            oxygen += int(amount)
                        else:
                            radiation += int(amount)
                    if (foodsupply <= 0 or oxygen <= 0 or radiation >= 100) and curr_q != BAABAQ:
                        curr_q = D
                    if foodsupply > 100:
                        foodsupply = 100
                    elif foodsupply < 0:
                        foodsupply = 0
                    if oxygen > 100:
                        oxygen = 100
                    elif oxygen < 0:
                        oxygen = 0
                    if radiation < 0:
                        radiation = 0
                    elif radiation > 100:
                        radiation = 100
                except KeyError:
                    curr_q = Q
                    crystals = 0
                    foodsupply = 100
                    radiation = 0
                    oxygen = 100

    else:
        screen.blit(bg_image, (0,0))

        screen.blit(bordertop, (0, 0))
        screen.blit(borderbottom, (0, SCREEN_HEIGHT - SCREEN_HEIGHT/12))

        font = pygame.font.Font("fonts/question_font.ttf", 36)
        text = font.render(curr_q.q, True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4))
        screen.blit(text, text_rect)

        font = pygame.font.Font("fonts/question_font.ttf", 20)
        
        if oxygen > 70:
            oxygen_colour = (0, 255, 0)
        elif oxygen > 30:
            oxygen_colour = (255, 165, 0)
        else:
            oxygen_colour = (255, 0, 0)

        if foodsupply > 70:
            food_colour = (0, 255, 0)
        elif foodsupply > 30:
            food_colour = (255, 165, 0)
        else:
            food_colour = (255, 0, 0)

        if radiation < 40:
            radiation_colour = (0, 255, 0)
        elif radiation < 70:
            radiation_colour = (255, 165, 0)
        else:
            radiation_colour = (255, 0, 0)
            
        oxygen_text = font.render(f"Oxygen Level: {oxygen:03}", True, oxygen_colour)
        separator_one = font.render(" | ", True, (255,255,255))
        food_text = font.render(f"Food Supply: {foodsupply:03}", True, food_colour)
        separator_two = font.render(" | ", True, (255,255,255))
        radiation_text = font.render(f"Radiation: {radiation:03}", True, radiation_colour)

        stats = [oxygen_text, separator_one, food_text, separator_two, radiation_text]
        total_width = sum(part.get_width() for part in stats)

        x = SCREEN_WIDTH/4.5 - total_width/2
        y = SCREEN_HEIGHT/1.03

        for part in stats:
            text_rect = part.get_rect(midleft=(x, y))
            screen.blit(part, text_rect)
            x += part.get_width()

        font = pygame.font.Font("fonts/question_font.ttf", 24)
        text = font.render(f"At the Lunar Outpost... ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/9,SCREEN_HEIGHT/35))
        screen.blit(text, text_rect)

        font = pygame.font.Font("fonts/title_card_font.ttf", 38)
        text = font.render(f"Crystals: {crystals} ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/1.07,SCREEN_HEIGHT/1.03))
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("fonts/logo_font.ttf", 38)
        text = font.render(f"Crescent Crystals", True, (169,55,250))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/1.1,SCREEN_HEIGHT/20))
        screen.blit(text, text_rect)

        astronaut = pygame.image.load("images/astronaut_sprite.png")
        screen.blit(astronaut, (SCREEN_WIDTH/2 - SCREEN_WIDTH/20, SCREEN_HEIGHT/2))

        mouse = pygame.mouse.get_pos()

        draw_gradient_button(
            button_left,
            (189, 23, 108),
            (46, 0, 24),
            button_left.collidepoint(mouse)
        )

        draw_gradient_button(
            button_right,
            (23, 145, 82),
            (2, 56, 28),
            button_right.collidepoint(mouse)
        )
        
        font = pygame.font.Font("fonts/question_font.ttf", 30)
        text = font.render(f"{curr_q.a}", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/5.5,SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("fonts/question_font.ttf", 30)
        text = font.render(f"{curr_q.b}", True, (255,255,255))
        text_rect = text.get_rect(center=(13*SCREEN_WIDTH/16,SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

bg_music.stop()

pygame.quit()