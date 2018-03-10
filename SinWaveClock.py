import pygame
from pygame import Surface
import time
import math
from os import path

class SinWaveClock(pygame.Surface):
  def __init__(self, width, height):
    pygame.Surface.__init__(self,(width, height))
    pygame.font.init()
    # All values that can edit the sin wave clock
    self.sin_Length = self.get_width()
    # If zero it will just be a line
    self.sin_DotProximity = 10
    # .5 is 1 second period
    self.sin_Period = .25
    self.sin_Frequency = 4
    self.sin_Amplitude = int(height * .166667)
    self.sin_YDisplacment = int(height * .25)
    self.sin_XDisplacment = int(width * .005)
    # Color for dots in the future
    self.sin_LnColorPrimary = (186, 111, 23)
    # Clolor for dots in the past
    self.sin_LnColorSecondary = (39,40,34)
    # Size of dots
    self.sin_LnRadius = int(height * .01633333)
    self.sin_SecondsDotRadius = int(height * .026667)
    self.sin_SecondsYDisplacment = int(height * -.06667)
    self.sin_SecondsXDisplacment = int(width * -.055)
    self.bgColor = (0,0,0)
    self.bgSurface = pygame.Surface((width, height))
    # FONTS
    self.fonts_path = path.join(path.dirname(path.realpath(__file__)), 'Fonts')
    self.secondsFont = pygame.font.Font(path.join(self.fonts_path, '1979_dot_matrix.ttf'), int(height * .08))
    self.dateFont = pygame.font.Font(path.join(self.fonts_path, 'OpenSans-Regular.ttf'), int(height * .25))
    self.timeFont = pygame.font.Font(path.join(self.fonts_path, 'OpenSans-Regular.ttf'), int(height * .25))
    self.fontColor = (242,242,242)
    self.previousSec = int(time.time() % 60)
    self.previousTime = time.strftime('%I:%M %p')
    self.previousDate = time.strftime('%a, %b %d')
    self.secondsSurface = self.secondsFont.render(str(self.previousSec), True, (242,242,242))
    self.dateSurface = self.dateFont.render(str(self.previousDate), True, (242,242,242))
    self.timeSurface = self.timeFont.render(str(self.previousTime), True, (242,242,242))
    self.dateSurfaceXYOffset = (int(width * .01), int(height * -.03333333))
    self.timeSurfaceXYOffset = (int(width * .008), int(height * .216667))
    self.bgSurface.fill(self.bgColor)
    self.bgSurface.convert()
    self.blit(self.bgSurface, (0,0))
    self.convert()

  def Update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    # An improvment that could be made with All the render statements is adding a 
    # background color, pygame documentation says its much more efficient than 
    # Alpha channels.
    if self.previousSec != currentSecond:
      self.secondsSurface = self.secondsFont.render(str(currentSecond), True, self.fontColor)
      self.previousSec = currentSecond
    if self.previousDate != currentDate:
      self.dateSurface = self.dateFont.render(str(currentDate), True, self.fontColor)
      self.previousDate = currentDate
    if self.previousTime != currentTime:
      self.timeSurface = self.timeFont.render(str(currentTime), True, self.fontColor)
      self.previousTime = currentTime

    self.blit(self.bgSurface, (0,0))
    # Traverses through every pixel from left to right for sin wave and prints every frame
    for x in range(0, self.sin_Length, self.sin_DotProximity):
        # Find the points on a sine wave
        y = int((self.get_height()/2) + self.sin_Amplitude*math.sin(self.sin_Frequency*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period*time.time()*math.pi))))) + self.sin_YDisplacment
        # Draw dots infront of seconds counts
        pygame.draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        if (x - (self.sin_Length)/2) < self.sin_DotProximity/2 :
          # Draw dots behind seconds counter if behind the middle mark of sinwave.
          pygame.draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        # Draws larger second counter Dot
        if (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y < self.sin_YDisplacment + (self.get_height()/2)) :
          pygame.draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_SecondsDotRadius)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment + self.sin_SecondsXDisplacment ,y + self.sin_SecondsYDisplacment))
        elif (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y >= self.sin_YDisplacment + (self.get_height()/2)):
          pygame.draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), self.sin_SecondsDotRadius)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment + self.sin_SecondsXDisplacment,y + self.sin_SecondsYDisplacment))
        self.blit(self.dateSurface, self.dateSurfaceXYOffset)
        self.blit(self.timeSurface, self.timeSurfaceXYOffset)
    return self