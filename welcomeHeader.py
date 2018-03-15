from pygame import image, Surface, font, transform, SRCALPHA
from os import path

class WelcomeHeader(Surface):
    def __init__(self, width, height):
        Surface.__init__(self, (width, height))
        self.width = width
        self.height = height
        self.fill((242,242,242))
        # You need this if you intend to display any text
        font.init()
        self.dir_path = path.dirname(path.realpath(__file__))
        self.assets_path = path.join(self.dir_path, 'Assets')
        # notice the 'Fonts' folder is located in the 'Assets'
        self.fonts_path = path.join(self.assets_path, 'Fonts')
        self.bcLogoFile = 'ButteCollegeLogo.png'
        self.welcomeTextFont = (path.join(self.fonts_path, 'OpenSans-Bold.ttf'), int(height * .3))
        self.welcomeTextTop = 'Welcome to'
        self.welcomeTextBottom = 'the Media Center'
        self.Render()

    def aspect_scale(self, img, bx, by):
        # """ Scales 'img' to fit into box bx/by.
        # This method will retain the original image's aspect ratio """
        ix,iy = img.get_size()
        if ix > iy:
            # fit to width
            scale_factor = bx/float(ix)
            sy = scale_factor * iy
            if sy > by:
                scale_factor = by/float(iy)
                sx = scale_factor * ix
                sy = by
            else:
                sx = bx
        else:
            # fit to height
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            if sx > bx:
                scale_factor = bx/float(ix)
                sx = bx
                sy = scale_factor * iy
            else:
                sy = by

        return transform.scale(img, (int(sx),int(sy)))

    def Render(self):
        bcLogoSurface = image.load(path.join(self.assets_path, self.bcLogoFile))
        bcLogoSurface = self.aspect_scale(bcLogoSurface, int(.4 * self.width), self.height)
        welcomeFont = font.Font(*self.welcomeTextFont)
        welcomeTextTopSurface = welcomeFont.render(self.welcomeTextTop, True, (0,0,0))
        welcomeTextTopSurfaceRect = (int(self.width * .015873) + bcLogoSurface.get_rect().width + ((self.width - bcLogoSurface.get_rect().width) / 2) - (welcomeTextTopSurface.get_rect().width / 2), int(self.height * .1))
        welcomeTextBottomSurface = welcomeFont.render(self.welcomeTextBottom, True, (0,0,0))
        welcomeTextBottomSurfaceRect = (10 + bcLogoSurface.get_rect().width + ((self.width - bcLogoSurface.get_rect().width) / 2) - (welcomeTextBottomSurface.get_rect().width / 2), int(self.height * .5))
        self.blit(bcLogoSurface, (int(self.width * .015873), (self.height / 2) - (bcLogoSurface.get_rect().height / 2)))
        self.blit(welcomeTextTopSurface, welcomeTextTopSurfaceRect)
        self.blit(welcomeTextBottomSurface, welcomeTextBottomSurfaceRect)