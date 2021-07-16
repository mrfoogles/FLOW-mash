CSI = '\x1b['
FG = '38'
BG = '48'

CM_RGB = '2'
CM_8 = '5'

example_rgb = '\x1b[38;2;<r>;<g>;<b>m<value>\x1b[m'

def seq(*args):
    args = list(map(lambda arg : str(arg), args))
    put(f'{CSI}{";".join(args)}m')

def put(string):
    print(string,end='')

def rgb_to_8(r, g, b):
    return int(r/32) * 32 + int(g/32) * 4 + int(b/64)

def block(r, g, b):
    seq(FG,CM_8, rgb_to_8(r,g,b))
    put('<|>')

from blessed import Terminal

if __name__ == '__main__':
    term = Terminal()

    seq(BG, CM_RGB, 128, 128, 0)
    put('COLOR TEST COMPLETE')
    seq(0)