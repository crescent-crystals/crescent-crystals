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
AQ = Question("You discover an O2 tank. What do you do next?", "AQ", "Explore the Admin room.", "Go outside.")
AAQ = Question("Admin tells you to go outside. You are tipped off about the\nlocation of a food source south. What do you do once outside?", "AAQ", "Go explore North.", "Go South.", ["+1C"])
AAAQ = Question("You find a broken rover. What do you do?", "AAAQ", "Fix it.", "Continue exploring.", ["+1C"])
AAAAQ = Question("You return to the Space Station. Your mission is set to end soon. What do you do to prepare?", "AAAAQ", "Go to the cafeteria and have dinner.", "Analyse moon dust samples.", ["-10R"])
AAAAAQ = Question("You found ending 1/32!", "AAAAAQ", "END", "END", ["+10F"])
AAAABQ = Question("You found ending 2/32!", "AAAABQ", "END", "END", ["+1C"])
AAABQ = Question("You find a med kit. This was unexpected, so you rush back\nto report to Admin. What do you do along the way?", "AAABQ", "Stop and investigate a crater.", "Rush to report the news.", ["-10R", "+1C"])
AAABAQ = Question("You found ending 3/32!", "AAABAQ", "END", "END", ["+1C"])
AAABBQ = Question("You found ending 4/32!", "AAABBQ", "END", "END", ["+10O"])
AABQ = Question("After finding the food, you hear a strange noise nearby. What do you do?", "AABQ", "Call the Space Station on your radio.", "You check out the source.", ["+10F", "+15R"])
AABAQ = Question("They tell you to go back inside.", "AABAQ", "Obey.", "You disregard their advice and continue exploring.", ["+15R"])
AABAAQ = Question("You found ending 5/32!", "AABAAQ", "END", "END", ["+10O"])
AABABQ = Question("You found ending 6/32!", "AABABQ", "END", "END", ["+1C", "+15R"])
AABBQ = Question("You find a cute little green guy. What do you do?", "AABBQ", "Try to befriend him.", "Attack him.", ["+1C"])
AABBAQ = Question("You found ending 7/32!", "AABBAQ", "END", "END", ["+15F"])
AABBBQ = Question("You found ending 8/32!", "AABBBQ", "END", "END", ["+20R", "+1C"])
ABQ = Question("What do you do once outside?", "ABQ", "Explore a nearby crater.", "Find a bunker.", ["+15R"])
ABAQ = Question("You find a broken rover. What do you do?", "ABAQ", "Fix it.", "Continue exploring.", ["+1C"])
ABAAQ = Question("You report back on your findings via radio.", "ABAAQ", "You return to the Space Station.", "You continue exploring.", ["-10R"])
ABAAAQ = Question("You found ending 9/32!", "ABAAAQ", "END", "END", ["+10O"])
ABAABQ = Question("You found ending 10/32!", "ABAABQ", "END", "END", ["+1C"])
ABABQ = Question("You find a little blue guy.", "ABABQ", "Introduce yourself.", "Leave him alone and move on.", ["+1C"])
ABABAQ = Question("You found ending 11/32!", "ABABAQ", "END", "END", ["+20R", "-15F"])
ABABBQ = Question("You found ending 12/32!", "ABABBQ", "END", "END", ["+1C"])
ABBQ = Question("What do you do inside?", "ABBQ", "Look around for some food.", "Reorganise the supplies.", ["-10R"])
ABBAQ = Question("You leave the bunker. You hear a strange noise nearby. What do you do?", "ABBAQ", "Call the Space Station on your radio.", "You check out the source.", ["+10F", "+10O"])
ABBAAQ = Question("You found ending 13/32!", "ABBAAQ", "END", "END", ["+15R"])
ABBABQ = Question("You found ending 14/32!", "ABBABQ", "END", "END", ["+1C"])
ABBBQ = Question("You find a map of previously undiscovered places.", "ABBBQ", "Explore them yourself.", "Wait for more astronauts to arrive.", ["+1C"])
ABBBAQ = Question("You found ending 15/32!", "ABBBAQ", "END", "END", ["+1C", "+15R"])
ABBBBQ = Question("You found ending 16/32!", "ABBBBQ", "END", "END", ["+10O"])
BQ = Question("You see footprints leading away. What do you do?", "BQ", "Follow them.", "Explore according to yout mission.", ["+1C", "+15R"])
BAQ = Question("You find another astronaut. They ask to share resources.", "BAQ", "Share.", "Refuse and head back inside.", ["+15R"])
BAAQ = Question("You and the astronaut become friends. You both run into a\ncute little green guy offering you an O2 tank.", "BAAQ", "Take it.", "Refuse and keep exploring.", ["+1C"])
BAAAQ = Question("You find a mysterious cavern.", "BAAAQ", "You go in first.", "The other astronaut goes in first.", ["+20O", "-15R"])
BAAAAQ = Question("You found ending 17/32!", "BAAAAQ", "END", "END", ["+1C"])
BAAABQ = Question("You found ending 18/32!", "BAAABQ", "END", "END", ["+15R", "+10F"])
BAABQ = Question("You find a mysterious cavern.", "BAABQ", "You go in first.", "The other astronaut goes in first.", ["+1C"])
BAABAQ = Question("You found ending 19/32!", "BAABAQ", "END", "END", ["+100R"])
BAABBQ = Question("You found ending 20/32!\nUnfortunately, the other astronaut did not make it out alive.", "BAABBQ", "END", "END", ["+1C"])
BABQ = Question("What do you do inside?", "BABQ", "Look around for some food.", "Reorganise the supplies.", ["-10R"])
BABAQ = Question("Admin finds your digital journal in which you complain about your mission.", "BABAQ", "Say it belongs to the other astronaut.", "Confess.", ["+10F", "+10O"])
BABAAQ = Question("You found ending 21/32!", "BABAAQ", "END", "END", ["+15R"])
BABABQ = Question("You found ending 22/32!", "BABABQ", "END", "END", ["+1C"])
BABBQ = Question("You find a little blue guy hidden amongst boxes.", "BABBQ", "Escort him outside.", "Lock him inside and await further instructions.", ["+1C"])
BABBAQ = Question("You found ending 23/32!", "BABBAQ", "END", "END", ["+20R"])
BABBBQ = Question("You found ending 24/32!", "BABBBQ", "END", "END", ["+1C"])
BBQ = Question("You end up at a cross roads.", "BBQ", "Go right.", "Go left.", ["+1C"])
BBAQ = Question("You are starting to feel back pain.", "BBAQ", "Empty your O2 tank.", "Take a deep breath.", ["+1C"])
BBAAQ = Question("A little shimmering rainbow guy pops up of the tank and heals you.", "BBAAQ", "Do a little dance with him.", "Thank him kindly.", ["+100O", "+100F", "-100R"])
BBAAAQ = Question("You found ending 25/32!", "BBAAAQ", "END", "END", ["+1C"])
BBAABQ = Question("You found ending 26/32!", "BBAABQ", "END", "END", ["-30R"])
BBABQ = Question("You trip over air and injure yourself.\nYou wonder why NASA hired you.", "BBABQ", "You lie in the dirt for a while but ultimately get up.", "You call via radio for help.", ["+30O", "+1C"])
BBABAQ = Question("You found ending 27/32!", "BBABAQ", "END", "END", ["+1C"])
BBABBQ = Question("You found ending 28/32!", "BBABBQ", "END", "END", ["+15R"])
BBBQ = Question("You find a box with a map of previously undiscovered places.", "BBBQ", "Explore them by yourself.", "Wait for more astronauts to arrive.", ["+15R"])
BBBAQ = Question("You find a couple suspicious Mars bars that drifted from another planet.", "BBBAQ", "Eat them.", "Go back to the lab and analyse them.", ["+1C"])
BBBAAQ = Question("You found ending 29/32!", "BBBAAQ", "END", "END", ["+10F", "+15R"])
BBBABQ = Question("You found ending 30/32!", "BBBABQ", "END", "END", ["+10O", "+1C"])
BBBBQ = Question("What do you do once they arrive?", "BBBBQ", "Go back inside and wait.", "Help them explore.", ["+15R"])
BBBBAQ = Question("You found ending 31/32!", "BBBBAQ", "END", "END", ["+10O"])
BBBBBQ = Question("You found ending 32/32!", "BBBBBQ", "END", "END", ["+1C", "+15R"])
D = Question("You did not survive your mission.", "D", "END", "END")

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

bg_image = pygame.image.load('space_station.jpg')


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

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_left.collidepoint(event.pos):
                curr_q = d[curr_q.id[:-1] + "A" + curr_q.id[-1]]
                if len(curr_q.id) == 6 or curr_q.id == "D":
                    pass
                else:
                    oxygen -= 5
                    foodsupply -= 5
                    for item in curr_q.effects:
                        resc = item[-1]
                        amount = item[:-1]
                        if resc == "C":
                            crystals += int(amount)
                        elif resc == "F":
                            foodsupply += int(amount)
                        elif resc == "O":
                            oxygen += int(amount)
                        else:
                            radiation += int(amount)
                    if foodsupply <= 0 or oxygen <= 0 or radiation >= 100:
                        curr_q = D
                    if foodsupply > 100:
                        foodsupply = 100
                    if oxygen > 100:
                        oxygen = 100
                    if radiation < 0:
                        radiation = 0

            elif button_right.collidepoint(event.pos):
                curr_q = d[curr_q.id[:-1] + "B" + curr_q.id[-1]]
                if len(curr_q.id) == 6 or curr_q.id == "D":
                    pass
                else:
                    oxygen -= 5
                    foodsupply -= 5
                    for item in curr_q.effects:
                        resc = item[-1]
                        amount = item[:-1]
                        if resc == "C":
                            crystals += int(amount)
                        elif resc == "F":
                            foodsupply += int(amount)
                        elif resc == "O":
                            oxygen += int(amount)
                        else:
                            radiation += int(amount)
                    if foodsupply <= 0 or oxygen <= 0 or radiation >= 100:
                        curr_q = D
                    if foodsupply > 100:
                        foodsupply = 100
                    if oxygen > 100:
                        oxygen = 100
                    if radiation < 0:
                        radiation = 0

    else:
        screen.blit(bg_image, (0,0))

        screen.blit(bordertop, (0, 0))
        screen.blit(borderbottom, (0, SCREEN_HEIGHT - SCREEN_HEIGHT/12))

        font = pygame.font.Font("question_font.ttf", 36)
        text = font.render(curr_q.q, True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4))
        screen.blit(text, text_rect)


        font = pygame.font.Font("question_font.ttf", 20)
        text = font.render(f"Oxygen Level: {oxygen:03}   |    Food Supply: {foodsupply:03}   |   Radiation: {radiation:03}", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/4.5,SCREEN_HEIGHT/1.03))
        screen.blit(text, text_rect)

        font = pygame.font.Font("question_font.ttf", 24)
        text = font.render(f"At the Lunar Outpost... ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/9,SCREEN_HEIGHT/35))
        screen.blit(text, text_rect)

        font = pygame.font.Font("title_card_font.ttf", 38)
        text = font.render(f"Crystals: {crystals} ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/1.07,SCREEN_HEIGHT/1.03))
        screen.blit(text, text_rect)

        astronaut = pygame.image.load("astronaut_sprite.png")
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
        
        font = pygame.font.Font("question_font.ttf", 38)
        text = font.render(f"{curr_q.a}", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/4,SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("question_font.ttf", 38)
        text = font.render(f"{curr_q.b} ", True, (255,255,255))
        text_rect = text.get_rect(center=(3*SCREEN_WIDTH/4,SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()