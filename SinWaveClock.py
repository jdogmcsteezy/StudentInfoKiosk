from WeatherWidget import WeatherWidget
import pygame
from pygame import Surface, font, image, transform, SRCALPHA, draw
from apscheduler.schedulers.background import BackgroundScheduler
import time
import math
from os import path

class SinWaveClock(pygame.Surface):
  def __init__(self, width, height):
    Surface.__init__(self,(width, height))
    font.init()
    self.dir_path = path.dirname(path.realpath(__file__))
    self.assest_path = path.join(self.dir_path, 'Assets')
    self.fonts_path = path.join(self.assest_path, 'Fonts')
    self.bgColor = (15,15,15)
    self.weatherSurface = WeatherWidget(int(width * (250/1000)), int(height * (150/300)), self.bgColor)
    self.scheduler = BackgroundScheduler()
    self.scheduler.start()
    self.scheduler.add_job(self.weatherSurface.Update, 'interval', minutes=5)
    self.scheduler.add_job(self.blit, 'interval', minutes=5, seconds=2, args=(self.weatherSurface, (self.get_width() - self.weatherSurface.get_width(), 0)))
    # All values that can edit the sin wave clock
    self.sin_Length = self.get_width()
    # If zero it will just be a line
    self.sin_DotProximity = int(width * .02882882)
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
    self.sin_LnRadius = int(height * (30/740))
    self.sin_SecondsDotRadius = int(height * (30/740))
    self.sin_SecondsYDisplacment = int(height * -.06667)
    self.sin_SecondsXDisplacment = int(width * -.055)
    self.fill(self.bgColor)
    # FONTS
    self.secondsFont = font.Font(path.join(self.fonts_path, '1979_dot_matrix.ttf'), int(height * .08))
    self.dateFont = font.Font(path.join(self.fonts_path, 'OpenSans-Regular.ttf'), int(height * .25))
    self.timeFont = font.Font(path.join(self.fonts_path, 'OpenSans-Regular.ttf'), int(height * .25))
    self.fontColor = (242,242,242)
    self.previousSec = int(time.time() % 60)
    self.previousTime = time.strftime('%I:%M %p')
    self.previousDate = time.strftime('%a, %b %d')
    self.dateSurfaceXYOffset = (int(width * .01), int(height * -.05))
    self.timeSurfaceXYOffset = (int(width * .008), int(height * .2))
    self.secondsSurface = self.secondsFont.render(str(self.previousSec), True, self.fontColor)
    self.dateSurface = self.dateFont.render(str(self.previousDate), True, self.fontColor)
    self.timeSurface = self.timeFont.render(str(self.previousTime), True, self.fontColor)
    self.blit(self.weatherSurface, (self.get_width() - self.weatherSurface.get_width(), 0))
    self.convert()


  def Update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    # An improvment that could be made with All the render statements is adding a 
    # background color, pygame documentation says its much more efficient than 
    # Alpha channels.
    if self.previousSec != currentSecond:
        if currentSecond > 9:
            self.secondsSurface = self.secondsFont.render(str(currentSecond), True, self.fontColor)
        else:
            self.secondsSurface = self.secondsFont.render('0' + str(currentSecond), True, self.fontColor)
        self.previousSec = currentSecond
    if self.previousDate != currentDate:
        self.dateSurface = self.dateFont.render(str(currentDate), True, self.fontColor)
        self.previousDate = currentDate
    if self.previousTime != currentTime:
        self.timeSurface = self.timeFont.render(str(currentTime), True, self.fontColor)
        self.previousTime = currentTime

    self.fill(self.bgColor)
    # Traverses through every pixel from left to right for sin wave and prints every frame
    for x in range(0, self.sin_Length, self.sin_DotProximity):
        # Find the points on a sine wave
        y = int((self.get_height()/2) + self.sin_Amplitude*math.sin(self.sin_Frequency*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period*time.time()*math.pi))))) + self.sin_YDisplacment
        # Draw dots infront of seconds counts
        draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        if (x - (self.sin_Length)/2) < self.sin_DotProximity/2 :
          # Draw dots behind seconds counter if behind the middle mark of sinwave.
          draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        # Draws larger second counter Dot
        if (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y < self.sin_YDisplacment + (self.get_height()/2)) :
          draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_SecondsDotRadius)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment + self.sin_SecondsXDisplacment ,y + self.sin_SecondsYDisplacment))
        elif (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y >= self.sin_YDisplacment + (self.get_height()/2)):
          draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), self.sin_SecondsDotRadius)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment + self.sin_SecondsXDisplacment,y + self.sin_SecondsYDisplacment))
        self.blit(self.dateSurface, self.dateSurfaceXYOffset)
        self.blit(self.timeSurface, self.timeSurfaceXYOffset)
    self.blit(self.weatherSurface, (self.get_width() - self.weatherSurface.get_width(), 0))
    return self