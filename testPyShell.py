# Author: Jesse Schmidt 2018

import pygame
import SinWaveClock
import rssEventDisplay
import welcomeHeader
from ScheduleDisplay import ScheduleDisplay
import os

#os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
frameHeight = 740
frameWidth = int(frameHeight *(1080/1920))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    mainScreen = pygame.display.set_mode((frameWidth, frameHeight), pygame.NOFRAME)
    mainScreen.fill((0, 0, 255))
    header = welcomeHeader.WelcomeHeader(frameWidth, int(frameHeight * (200/1920))) #200
    mainScreen.blit(header, (0, 0))
    clockScreen = SinWaveClock.SinWaveClock(frameWidth, int(frameHeight * (300/1920))) #300
    mainScreen.blit(clockScreen, (0, int(frameHeight * (200/1920)))) #200
    eventScreen = rssEventDisplay.AcademicCalanderDisplay(frameWidth, int(frameHeight * (100/1920))) #100
    mainScreen.blit(eventScreen, (0, int(frameHeight * (1820/1920)))) #1820
    schedule = ScheduleDisplay(frameWidth, int(frameHeight * (1320/1920))) #1320
    mainScreen.blit(schedule, (0, int(frameHeight * (500/1920)))) #500
    pygame.display.update(mainScreen.blit(header, (0, 0)))
    schedule.Update()
    pygame.display.update(mainScreen.blit(schedule, (0, int(frameHeight * (500/1920))))) #500

    run = True
    while(run):
        clock.tick(16)
       	if schedule.Update():
            pygame.display.update(mainScreen.blit(schedule, (0, int(frameHeight * (500/1920)))))

        pygame.display.update(mainScreen.blit(clockScreen.Update(), (0,int(frameHeight * (200/1920))))) #200
       	pygame.display.update(mainScreen.blit(eventScreen.Update(), (0,int(frameHeight * (1820/1920))))) #1820

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    run = False
            elif event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
        main()