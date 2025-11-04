import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input('Aperte Enter para sair...')  # Melhor que pygame.event.wait()
pygame.quit()