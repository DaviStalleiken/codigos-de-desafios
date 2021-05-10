import pygame
pygame.init()
pygame.mixer.music.load('antimidia.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass

''' Outra opção é utilizar a Library Playsound:

from playsound import playsound
playsound('exemplo.mp3') '''
