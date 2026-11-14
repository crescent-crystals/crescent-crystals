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
AQ = Question("You discover an O2 tank. What do you do next?", "AQ", "Explore the Admin room.", "Go outside.", ["+O", "-F"])
AAQ = Question("Admin tells you to go outside. You are tipped off about the\nlocation of a food source south. What do you do once outside?", "AAQ", "Go explore North.", "Go South.", ["+C"])
AAAQ = Question("You find a broken rover. What do you do?", "AAAQ", "Fix it.", "Continue exploring.", ["+C", "-F"])
AAAAQ = Question("You return to the Space Station. Your mission is set to end soon. What do you do to prepare?", "AAAAQ", "Go to the cafeteria and have dinner.", "Analyse moon dust samples.", ["-R"])
AAAAAQ = Question("You found ending 1/32!", "AAAAAQ", "NULL", "NULL", ["+F"])
AAAABQ = Question("You found ending 2/32!", "AAAABQ", "NULL", "NULL", ["+C"])
AAABQ = Question("You find a med kit. This was unexpected, so you rush back\nto report to Admin. What do you do along the way?", "AAABQ", "Stop and investigate a crater.", "Rush to report the news.", ["-R", "+C"])
AAABAQ = Question("You found ending 3/32!", "AAABAQ", "NULL", "NULL", ["+C"])
AAABBQ = Question("You found ending 4/32!", "AAABBQ", "NULL", "NULL", ["+O"])
AABQ = Question("After finding the food, you hear a strange noise nearby. What do you do?", "AABQ", "Call the Space Station on your radio.", "You check out the source.", ["+F", "+R"])
AABAQ = Question("They tell you to go back inside.", "AABAQ", "Obey.", "You disregard their advice and continue exploring.", ["+R"])
AABAAQ = Question("You found ending 5/32!", "AABAAQ", "NULL", "NULL", ["+O"])
AABABQ = Question("You found ending 6/32!", "AABABQ", "NULL", "NULL", ["+C", "+R"])
AABBQ = Question("You find a cute little green guy. What do you do?", "AABBQ", "Try to befriend him.", "Attack him.", ["+C"])
AABBAQ = Question("You found ending 7/32!", "AABBAQ", "NULL", "NULL", ["+F"])
AABBBQ = Question("You found ending 8/32!", "AABBBQ", "NULL", "NULL", ["+R", "+C"])
ABQ = Question("What do you do once outside?", "ABQ", "Explore a nearby crater.", "Find a bunker.", ["+R"])
ABAQ = Question("You find a broken rover. What do you do?", "ABAQ", "Fix it.", "Continue exploring.", ["+C", "-F"])
ABAAQ = Question("You report back on your findings via radio.", "ABAAQ", "You return to the Space Station.", "You continue exploring.", ["-R"])
ABAAAQ = Question("You found ending 9/32!", "ABAAAQ", "NULL", "NULL", ["+O"])
ABAABQ = Question("You found ending 10/32!", "ABAABQ", "NULL", "NULL", ["+C"])
ABABQ = Question("You find a little blue guy.", "ABABQ", "Introduce yourself.", "Leave him alone and move on.", ["+C"])
ABABAQ = Question("You found ending 11/32!", "ABABAQ", "NULL", "NULL", ["+R", "-F"])
ABABBQ = Question("You found ending 12/32!", "ABABBQ", "NULL", "NULL", ["+C"])
ABBQ = Question("What do you do inside?", "ABBQ", "Look around for some food.", "Reorganise the supplies.", ["-R"])
ABBAQ = Question("You leave the bunker. You hear a strange noise nearby. What do you do?", "ABBAQ", "Call the Space Station on your radio.", "You check out the source.", ["+F", "+O"])
ABBAAQ = Question("You found ending 13/32!", "ABBAAQ", "NULL", "NULL", ["+R"])
ABBABQ = Question("You found ending 14/32!", "ABBABQ", "NULL", "NULL", ["+C"])
ABBBQ = Question("You find a map of previously undiscovered places.", "ABBBQ", "Explore them yourself.", "Wait for more astronauts to arrive.", ["+C"])
ABBBAQ = Question("You found ending 15/32!", "ABBBAQ", "NULL", "NULL", ["+C", "+R"])
ABBBBQ = Question("You found ending 16/32!", "ABBBBQ", "NULL", "NULL", ["+O"])
BQ = Question("You see footprints leading away. What do you do?", "BQ", "Follow them.", "Explore according to yout mission.", ["+C", "+R"])
BAQ = Question("You find another astronaut. They ask to share resources.", "BAQ", "Share.", "Refuse and head back inside.", ["+R"])
BAAQ = Question("You and the astronaut become friends. You both run into a\ncute little green guy offering you an O2 tank.", "BAAQ", "Take it.", "Refuse and keep exploring.", ["-F", "+C"])
BAAAQ = Question("You find a mysterious cavern.", "BAAAQ", "You go in first.", "The other astronaut goes in first.", ["+O", "-R"])
BAAAAQ = Question("You found ending 17/32!", "BAAAAQ", "NULL", "NULL", ["+C"])
BAAABQ = Question("You found ending 18/32!", "BAAABQ", "NULL", "NULL", ["+R", "+F"])
BAABQ = Question("You find a mysterious cavern.", "BAABQ", "You go in first.", "The other astronaut goes in first.", ["+C"])
BAABAQ = Question("You found ending 19/32!", "BAABAQ", "NULL", "NULL", ["+R", "-O"])
BAABBQ = Question("You found ending 20/32!\nUnfortunately, the other astronaut did not make it out alive.", "BAABBQ", "NULL", "NULL", ["+C"])
BABQ = Question("What do you do inside?", "BABQ", "Look around for some food.", "Reorganise the supplies.", ["-R"])
BABAQ = Question("Admin finds your digital journal in which you complain about your mission.", "BABAQ", "Say it belongs to the other astronaut.", "Confess.", ["+F", "+O"])
BABAAQ = Question("You found ending 21/32!", "BABAAQ", "NULL", "NULL", ["+R"])
BABABQ = Question("You found ending 22/32!", "BABABQ", "NULL", "NULL", ["+C"])
BABBQ = Question("You find a little blue guy hidden amongst boxes.", "BABBQ", "Escort him outside.", "Lock him inside and await further instructions.", ["+C"])
BABBAQ = Question("You found ending 23/32!", "BABBAQ", "NULL", "NULL", ["+R"])
BABBBQ = Question("You found ending 24/32!", "BABBBQ", "NULL", "NULL", ["+C"])
BBQ = Question("You end up at a cross roads.", "BBQ", "Go right.", "Go left.", "["+C"]")
BBAQ = Question("You are starting to feel back pain.", "BBAQ", "Empty your O2 tank.", "Take a deep breath.", ["+C"])
BBAAQ = Question("A little shimmering rainbow guy pops up of the tank and heals you.", "BBAAQ", "Do a little dance with him.", "Thank him kindly.", ["+O", "+F", "-R"])
BBAAAQ = Question("You found ending 25/32!", "BBAAAQ", "NULL", "NULL", ["+C"])
BBAABQ = Question("You found ending 26/32!", "BBAABQ", "NULL", "NULL", ["-R"])
BBABQ = Question("You trip over air and injure yourself.\nYou wonder why NASA hired you.", "BBABQ", "You lie in the dirt for a while but ultimately get up.", "You call via radio for help.", ["+O", "+C"])
BBABAQ = Question("You found ending 27/32!", "BBABAQ", "NULL", "NULL", ["+C"])
BBABBQ = Question("You found ending 28/32!", "BBABBQ", "NULL", "NULL", ["+R"])
BBBQ = Question("You find a box with a map of previously undiscovered places.", "BBBQ", "Explore them by yourself.", "Wait for more astronauts to arrive.", ["+R"])
BBBAQ = Question("You find a couple suspicious Mars bars that drifted from another planet.", "BBBAQ", "Eat them.", "Go back to the lab and analyse them.", ["+C"])
BBBAAQ = Question("You found ending 29/32!", "BBBAAQ", "NULL", "NULL", ["+F", "+R"])
BBBABQ = Question("You found ending 30/32!", "BBBABQ", "NULL", "NULL", ["+O", "+C"])
BBBBQ = Question("What do you do once they arrive?", "BBBBQ", "Go back inside and wait.", "Help them explore.", ["+R"])
BBBBAQ = Question("You found ending 31/32!", "BBBBAQ", "NULL", "NULL", ["+O"])
BBBBBQ = Question("You found ending 32/32!", "BBBBBQ", "NULL", "NULL", ["+C", "+R"])

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
    "BBBBBQ": BBBBBQ}


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

borderbottom = pygame.Rect(0, 820, 35000, 50)
bordertop = pygame.Rect(0, 0.8, 35000, 50)

surface = pygame.Surface((35000, 50), pygame.SRCALPHA)


mouse = pygame.mouse.get_pos()
colour_light = (170,170,170)
colour_dark = (100,100,100)

location = "nothing"


button_left = pygame.Rect(0, 0, SCREEN_WIDTH/4, SCREEN_HEIGHT/5)
button_left.center = (SCREEN_WIDTH/5.5, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/10)

button_right = pygame.Rect(0, 0, SCREEN_WIDTH/4, SCREEN_HEIGHT/5)
button_right.center = (SCREEN_WIDTH*4.5/5.5, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_left.collidepoint(event.pos):
                print("Left button was pressed")

            elif button_right.collidepoint(event.pos):
                print("Right button was pressed")


    else:
        screen.blit(bg_image, (0,0)) 
    
        pygame.draw.rect(screen, (0,0,0), bordertop)
        pygame.draw.rect(screen, (0,0,0),  borderbottom)

        font = pygame.font.Font("question_font.ttf", 36)
        text = font.render("Where do you choose to go?", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4))
        screen.blit(text, text_rect)
        
  
        font = pygame.font.Font("question_font.ttf", 20)
        text = font.render(f"Oxygen Level: {oxygen:03}   |    Food Supply: {foodsupply:03}   |   Radiation: {radiation:03}", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/4.5,SCREEN_HEIGHT/1.03))
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("question_font.ttf", 24)
        text = font.render(f"At the {location}... ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/12.4,SCREEN_HEIGHT/35))
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("title_card_font.ttf", 38)
        text = font.render(f"Crystals: {crystals} ", True, (255,255,255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/1.07,SCREEN_HEIGHT/1.03))
        screen.blit(text, text_rect)


        astronaut = pygame.image.load("astronaut_sprite.png")
        screen.blit(astronaut, (SCREEN_WIDTH/2 - SCREEN_WIDTH/20, SCREEN_HEIGHT/2))

        mouse = pygame.mouse.get_pos()

        if button_left.collidepoint(mouse):
            pygame.draw.rect(screen, colour_light, button_left, border_radius=15)
        else:
            pygame.draw.rect(screen, colour_dark, button_left, border_radius=15)

        if button_right.collidepoint(mouse):
            pygame.draw.rect(screen, colour_light, button_right, border_radius=15)
        else:
            pygame.draw.rect(screen, colour_dark, button_right, border_radius=15)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()