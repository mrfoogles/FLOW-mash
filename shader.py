import color as cl
import numpy


class Rect:
    def __init__(self,x=0,y=0,w=None,h=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def shade(self,x,y,v,**uniforms):
        raise NotImplementedError()
    
    def render_to(self,screen,**uniforms):
        if self.w:
            w = min(self.w,screen.shape[0])
        else:
            w = screen.shape[0]
        if self.h:
            h = min(self.h,screen.shape[1])
        else:
            h = screen.shape[1]

        for x in range(self.x,w):
            for y in range(self.y,w):
                color = self.shade(
                    x=x,y=y,
                    v=screen[x][y],
                    w=w,h=h,
                    **uniforms
                )
                if color != None:
                    screen[x][y] = color
        
        print(self.__class__)
        print(screen)
        return screen

class BlockRGB(Rect):
    def __init__(self,c=(255,255,255),**kwargs):
        super().__init__(**kwargs)
        self.c = c
    
    def shade(self,x,y,v,**uniforms):
        return cl.rgb_to_8(*self.c)

class Map(Rect):
    def __init__(self,data,colors,**kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.colors = colors
    
        self.w = data.shape[0]
        self.h = data.shape[1]

    @staticmethod
    def with_shape(shape,colors):
        return Map(numpy.zeros(shape,numpy.int64),colors)
    
    @staticmethod
    def from_text(text,letter_ids,colors):
        if len(text) == 0:
            raise Exception("Undefined behavior for 0x0 map.")
        
        lines = text.split('\n')
        shape = (len(lines[0]),len(lines))

        data = numpy.zeros(shape,numpy.int64)
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                data[x][y] = letter_ids[c]
    
        return Map(data,colors)

    def shade(self,x,y,v,**uniforms):
        if self.data[x][y] != 0:
            return self.colors[self.data[x][y]]

def render_screen(screen):
    current_color = 0
    for row in screen:
        for tile_color in row:
            if tile_color != current_color:
                cl.seq(cl.BG, cl.CM_8, tile_color)
                current_color = tile_color
            cl.put('<|>')
        cl.put('\n')
    cl.seq(0)

# Test

from blessed import Terminal
if __name__ == "__main__":
    screen_shape = (10,10)
    screen = numpy.zeros(screen_shape,numpy.int8)

    block = BlockRGB(x=0,y=0,w=5,h=5,c=(255,0,0))
    screen = block.render_to(screen)

    print(screen)

    term = Terminal()
    render_screen(screen)