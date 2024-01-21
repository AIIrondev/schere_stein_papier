import time
import random
import pygame


pygame.init()
Score_text = 0
font = pygame.font.Font(None, 75)
text = font.render("Du hast gewonnen!", True, (0, 255, 0))
text1 = font.render("Du hast verloren!", True, (0, 255, 0))
text2 = font.render("Keiner hat gewonnen!", True, (0, 255, 0))
text3 = font.render(str(Score_text), True, (0, 0, 0))
index1 = None
computer_choice = ['Schere', 'Stein', 'Papier']
size = (1024, 1024)
button_size = (200, 100)  # Größe der Schaltfläche
screen = pygame.display.set_mode(size)
text_rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
# Titel des Fensters
pygame.display.set_caption("Schere, Stein, Papier Game")
background_image = pygame.image.load("Hintergrund.jpg").convert()
background_image1 = pygame.image.load("Play_ground.png").convert()
button_image = pygame.image.load("Start Button.png").convert_alpha()
button_image = pygame.transform.scale(button_image, button_size)  # Größe des Bildes ändern
button_rect = button_image.get_rect()
Schere_image = pygame.image.load("Schere.png").convert_alpha()
Score_image = pygame.image.load("Score_board.png").convert_alpha()
# Position des Buttons berechnen
button_pos = (350, 650)
Stein_image = pygame.image.load("Stein.png").convert_alpha()
Papier_image = pygame.image.load("Papier.png").convert_alpha()
random_1 = random.choice(computer_choice)

def button_click():
    print("Schaltfläche wurde geklickt!")
# Schleife, die das Fenster offen hält

while True:
    # Ereignisschleife
    for event in pygame.event.get():
        screen.blit(background_image, [0, 0])

        # Zeichnen der Schaltfläche
        screen.blit(button_image, button_pos)

        # Aktualisieren des Fensters
        pygame.display.update()
        if event.type == pygame.QUIT:
            # Schließen des Fensters, wenn auf das X geklickt wird
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Überprüfen, ob der Benutzer auf die Schaltfläche geklickt hat

            # Zeichnen des Hintergrundbilds

            while True:
                kas = True
                for event1 in pygame.event.get():
                    # Zeichnen des Hintergrundbilds
                    screen.blit(background_image1, [0, 0])

                    # Zeichnen der Schaltfläche
                    screen.blit(Schere_image, [350, 500])
                    screen.blit(Stein_image, [480, 550])
                    screen.blit(Papier_image, [630, 500])
                    screen.blit(Score_image, [50, 50])
                    screen.blit(text3, [180, 70])

                    # Aktualisieren des Fensters
                    pygame.display.update()
                    if event1.type == pygame.QUIT:
                        # Schließen des Fensters, wenn auf das X geklickt wird
                        pygame.quit()
                        quit()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_s]:
                        print("s wurde gedrückt!")
                        user_input = "Schere"
                        kas = True
                        screen.blit(Schere_image, [480,450])
                        pygame.display.update()
                        if kas == True:
                            pygame.display.update()
                            for event2 in pygame.event.get():
                                if event2.type == pygame.QUIT:
                                    # Schließen des Fensters, wenn auf das X geklickt wird
                                    pygame.quit()
                                    quit()
                            if random_1 == "Schere":
                                screen.blit(Schere_image, [490, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text2, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Stein":
                                Score_text -= 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True,(0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Stein_image, [490, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text1, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Papier":
                                Score_text += 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True,(0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Papier_image, [490, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            break
                    if keys[pygame.K_t]:
                        print("t wurde gedrückt!")
                        user_input = "Stein"
                        kas = True
                        screen.blit(Stein_image, [480,450])
                        pygame.display.update()
                        if kas == True:
                            for event2 in pygame.event.get():
                                if event2.type == pygame.QUIT:
                                    # Schließen des Fensters, wenn auf das X geklickt wird
                                    pygame.quit()
                                    quit()
                            if random_1 == "Schere":
                                Score_text += 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True,(0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Schere_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Stein":
                                screen.blit(Stein_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text2, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Papier":
                                Score_text -= 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True,(0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Papier_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text1, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)

                            break
                    if keys[pygame.K_p]:
                        print("p wurde gedrückt!")
                        user_input = "Papier"
                        kas = True
                        screen.blit(Papier_image, [480,450])
                        pygame.display.update()
                        if kas == True:
                            for event2 in pygame.event.get():
                                if event2.type == pygame.QUIT:
                                    # Schließen des Fensters, wenn auf das X geklickt wird
                                    pygame.quit()
                                    quit()
                            if random_1 == "Schere":
                                Score_text -= 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True,(0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Schere_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text1, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Stein":
                                Score_text += 1  # aktualisiere Punktzahl
                                text3 = font.render(str(Score_text), True, (0, 0, 0))  # aktualisiere Textanzeige des Scoreboards
                                screen.blit(Score_image, [50, 50])  # zeichne das Scoreboard-Image
                                screen.blit(text3, [180, 70])  # zeichne den aktualisierten Text
                                pygame.display.update()  # aktualisiere das Fenster
                                screen.blit(Stein_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            elif random_1 == "Papier":
                                screen.blit(Papier_image, [480, 220])
                                pygame.display.update()
                                time.sleep(1)
                                screen.blit(text2, text_rect)
                                pygame.display.update()
                                kas = False
                                time.sleep(1)
                                random_1 = random.choice(computer_choice)
                            pygame.display.update()
                            break