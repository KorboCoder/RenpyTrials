init python:

    import random
    import math

    random.seed()

    def Snow(image, max_particles=50, speed=150, wind=100, direction=0.0,  xborder=(0,100), yborder=(50,400), **kwargs):

        return Particles(SnowFactory(image, max_particles, speed, direction, wind, xborder, yborder, **kwargs))

    class SnowFactory(object):
        def __init__(self, image, max_particles, speed, direction, wind, xborder, yborder, **kwargs):
            self.max_particles = max_particles
            self.speed = speed
            self.wind = wind
            direction = math.radians(90-direction)
            self.direction = (math.cos(direction), math.sin(direction))
            self.xborder = xborder
            self.yborder = yborder

            self.depth = kwargs.get("depth", 10)

            self.image = self.image_init(image)

        def create(self, particles, st):

            if particles is None or len(particles) < self.max_particles:

                depth = random.randint(1, self.depth)
                depth_speed = 1.5-depth/(self.depth+0.0)

                return [ SnowParticle(self.image[depth-1],      # the image used by the particle
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      self.direction,
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      
                                      ) ]

        def image_init(self, image):
            rv = [ ]

            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0

                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv

        def predict(self):
            return self.image

    class SnowParticle(object):
        def __init__(self, image, wind, speed, direction, xborder, yborder):

            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            self.direction = direction
            
            if(direction[0] < 0.01 and direction[0] > -0.01):
                # the horizontal/vertical positions of this particle            
                self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
                self.ypos = -yborder
            else:
                if random.randint(0,1) == 1:
                    self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
                    self.ypos = -yborder
                else:
                    if direction[0] > 0:
                        self.xpos = 0
                    else:
                        self.xpos = renpy.config.screen_width
                    self.ypos = random.uniform(0-yborder, renpy.config.screen_height+yborder)
                    


        def update(self, st):

            if self.oldst is None:
                self.oldst = st

            lag = st - self.oldst
            self.oldst = st

            self.xpos += lag * (self.wind + self.direction[0]*self.speed)
            self.ypos += lag * (self.speed*self.direction[1])

            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None

            return int(self.xpos), int(self.ypos), st, self.image