import pygame
import SinWaveClock
import rssEventDisplay
import welcomeHeader
from ScheduleDisplay import ScheduleDisplay
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

def main():
    pygame.init()
    clock = pygame.time.Clock()
    mainScreen = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME)
    mainScreen.fill((0, 0, 255))
    header = welcomeHeader.WelcomeHeader(1080, 200)
    mainScreen.blit(header, (0, 0))
    clockScreen = SinWaveClock.SinWaveClock(1080, 300)
    mainScreen.blit(clockScreen, (0, 200))
    eventScreen = rssEventDisplay.AcademicCalanderDisplay(1080, 100)
    mainScreen.blit(eventScreen, (0, 1820))
    schedule = ScheduleDisplay(1080, 1320)
    mainScreen.blit(schedule, (0, 500))


    pygame.display.update()
    run = True
    while(run):
        clock.tick(26)
        mainScreen.blit(header, (0, 0))
        mainScreen.blit(clockScreen.Update(), (0, 200))
        mainScreen.blit(eventScreen.Update(), (0, 1820))
        mainScreen.blit(schedule.Update(), (0, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    run = False
            elif event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
        main()