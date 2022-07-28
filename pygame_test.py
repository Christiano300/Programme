import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.NOFRAME)
clock = pygame.time.Clock()

raphi_cursor = (
"                                                                                                                                ",
"                                             XXXXXXXXX............ ..   .....                                                   ",
"                                            XXXXXXXXXXXX...X................                                                    ",
"                                          XXXXXXXXXXXX....X..XXXXXXXX.........                                                  ",
"                                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXX..........                                                ",
"                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..........  .X                                          ",
"                                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..............                                          ",
"                                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX...XX......                                          ",
"                                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                          ",
"                                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           ....                           ",
"                                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.   ...  ....X..                         ",
"                                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................XXX.                       ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.........XXX.                      ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX............                     ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX............X                    ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX............                   ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..............                 ",
"                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..............                ",
"                                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..............               ",
"                                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX........XXXXXX.              ",
"                                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.........XXXXXXXX.             ",
"                               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXX             ",
"                              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
"                            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
"                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX...XXXXXXXXX.            ",
"                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..    .. ..               ",
"                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.                         ",
"                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                          ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                          ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                          ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X                      ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                         ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                      ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX....XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                      ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................XXXXXXXXXXXXXXXXXXXXXXXXX                         ",
"                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX......................XXXXXXXXXXXXXXXXXXXXXXXXX                        ",
"                          XXXXXXXXXXXXXXXXXXXXXXXXXXX............................XXXXXXXXXXXXXXXXXXXXXXX                        ",
"                            XXXXXXXXXXXXXXXXXXXXXXX............       ............XXXXXXXXXXXXXXXXXXXXXX                        ",
"                             XXXXXXXXXXXXXXXXXXXXX...........           ...........XXXXXXXXXXXXXXXXXXXXX                        ",
"                              XXXXXXXXXXXXXXXXXX...........               ..........XXXXXXXXXXXXXXXXXXXX                        ",
"                               XXXXXXXXXXXXXXXX...........                 ..........XXXXXXXXXXXXXXXXXXX                        ",
"                                XXXXXXXXXXXXXXX..........                   .........XXXXXXXXXXXXXXXXXXX                        ",
"                                 XXXXXXXXXXXXX...........                   ..........XXXXXXXXXXXXXXXXXX                        ",
"                                 XXXXXXXXXXXXX..........                     ..........XXXXXXXXXXXXXXXXX                        ",
"                                 XXXXXXXXXXXX...........                     ..........XXXXXXXXXXXXXXXXX                        ",
"                                 XXXXXXXXXXX...........                       .........XXXXXXXXXXXXXXXXX                        ",
"                                  XXXXXXXXX............                       ..........XXXXXXXXXXXXXXXX                        ",
"                                  XXXXXXXXX............                       ..........XXXXXXXXXXXXXXXX                        ",
"                               XXXXXXXXXXXX............                       ...........XXXXXXXXXXXXXX                         ",
"                             XXXXXXXXXXXXXX............                       ...........XXXXXXXXXXXXXX                         ",
"                            XXXXXXXXXXXXXXX............                       ...........XXXXXXXXXXXXXX                         ",
"                            XXXXXXXXXXXXXXX............                       ...........XXXXXXXXXXXXXX                         ",
"                            XXXXXXXXXXXXXXX.............                     ............XXXXXXXXXXXXXX                         ",
"                           XXXXXXXXXXXXXXX..............                     ............XXXXXXXXXXXXXX                         ",
"                           XXXXXXXXXXXXXXX...............                   .............XXXXXXXXXXXXXX                         ",
"                           XXXXXXXXXXXXXXX...............                   .............XXXXXXXXXXXXXX                         ",
"                           XXXXXXXXXXXXXXX................                 ...............XXXXXXXXXXXXX                         ",
"                           XXXXXXXXXXXXXX.....XXXXXXXX.....               ................XXXXXXXXXXXXX                         ",
"                             XXXXXXXXXXX.X..XXX...XXXXXX.....           ..................XXXXXXXXXXXXX                         ",
"                             XXXXXXXXXXX.XXXXX.........X.......       ........XXXXXXXX....XXXXXXXXXXXX                          ",
"                             XXXXXXXXXXX.XXX................................XXXXXXXXXXXX..XXXXXXXXXXXX                          ",
"                              XXXXXXXXXX.XX.................................XXXX...XXXXXXXXXXXXXXXXXXX                          ",
"                              XXXXXXXXXXXX.............................................XXXXXXXXXXXXXXX                          ",
"                              XXXXXXXXX.XX......XXXXX....................XX.............XXXXXXXXXXXXXX                          ",
"                               XXXXXXXX......XXX.....XXXX...............XX..............XXXXXXXXXXXXX                           ",
"                               XXXXXXX......XXXXXXXXXXXXXX.............XXX..XXXXXXXX.....XXXXXXXXXXX                            ",
"                               XXXXXXX.....XXXXXXXXXXXXXXXX...........XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            ",
"                               XXXXXXX.....XXXXXXXXXXXXXXXX...........XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            ",
"                               XXXXXXX.....XXXXX.XXXXXX.XX...........XX.XX.XXXXXXXXXXXXXXXXXXXXXXXX                             ",
"                               .XXXXX........XXX.XXXXXX..X...........X....XXXXXXXXXXXXXXXXXXXXXXXXX                             ",
"                               .XXXXX............XXXX....................XX..XXXXXXXXXXXXXXXXXXXXXX                             ",
"                               .XXXXXX.......................................XXXXXXXXXXXXXXXXXXXXX                              ",
"                               XXXXXXX........................................XXXX.XXXXX...XXXXXXX                              ",
"                               X.XXXXX..........................................XXX...X.....XXXXX                               ",
"                               X.XXXX................................................X......XXXXX                               ",
"                               X.XXXX............................................XXXX.......XXXXX                               ",
"                               X..XXX.......................................................XXXX                                ",
"                               X..XXX.......................................................XXXX                                ",
"                               X...XX.......................................................XXXX                                ",
"                                ....X.......................................................XXX                                 ",
"                                X...X.......................................................XXX                                 ",
"                                X...........................................................XXX                                 ",
"                                 X...X......................................................XXX                                 ",
"                                 X...X......................................................XXX                                 ",
"                                  X..X.....................................................XXX                                  ",
"                                   XXXX..................XXXXX......XXXXX..................XXX                                  ",
"                                    XXX..................XXXXXX..XXXXXXXX..................XX                                   ",
"                                    XXX...................XXXXXXXXXXXXXX..................XX.                                   ",
"                                     XXX.....................XXXXXXXXXX..................XXX                                    ",
"                                     XXX......XXXX............XXXXXX....................XXX                                     ",
"                                     XXXX....XXXXX..............XXX............XX.....XXXXX                                     ",
"                                     XXXX....XXXXX.............................XXXXXXXXXXX                                      ",
"                                     XXXX.....XXXXX............................XXXXXXXXXXX                                      ",
"                                     XXXXX.....X.XXX.........................XXXXXXXXXXXXX                                      ",
"                                     XXX.X.........XXXXX....................XXXX...XXXXXXX                                      ",
"                                      XX............XXXXXXXXXXX..XXXXXXXXXXXXXXX....XXXXX                                       ",
"                                      XX............XXXX.........XX...XXXXXXXX......XXXXX                                       ",
"                                      XXX............XXX................XXXXX.......XXXXX                                       ",
"                                       XX...............XX........X..XXXXXXX.......XXXXX                                        ",
"                                       XXX...............XX....X.XX..XXXXXX.......XXXXXX                                        ",
"                                       XXXX................XXXXXX................XXXXXX                                         ",
"                                        XXX................................X.....XXXXXX                                         ",
"                                        XXXX..............X...............X......XXXXX                                          ",
"                                         XXX...............X...........XX.X.....XXXXXX                                          ",
"                                         XXXX........................XX...X.....XXXXX                                           ",
"                                         XXXX............................X.....XXXXX                                            ",
"                                         XXXXX...........................X....XXXXX                                             ",
"                                         XXXXX................................XXXXX                                             ",
"                                          XXXXX..............................XXXXX                                              ",
"                                          XXXXXX............................XXXXXX                                              ",
"                                          XXXXXXX........X.................XXXXXXX                                              ",
"                                          XXXXXXXX........................XXXXXXXX                                              ",
"                                          XXXXXXXXX.......................XXXXXXXX                                              ",
"                                          X.XXXXXXXXX....................XXXXXXXX                                               ",
"                                          X...XXXXXXXX...........XX.....XXXXXXXXX                                               ",
"                                          XX...XXXXXXXX.....XXXXXXX....XXXXXXXXXX                                               ",
"                                          XX....XXXXXXXXX...XXXXXXX..XXXXXXXXXXXX                                               ",
"                                          XX.....XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                               ",
"                                          XX......XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                               ",
"                                          XX.......XXXXXXXXXXXXXXXXXXXXXXXXXXX.XX                                               ",
"                                          XX........XXXXXXXXXXXXXXXXXXXXXXXX...XX                                               ",
"                                          XX.........XXXXXXXXXXXXXXXXXXXXXX...XXX                                               ",
"                                          XX..........XXXXXXXXXXXXXXXXXXXX....XXX                                               ",
"                                          XX...........XXXXXXXXXXXXXXXXXX.....XXX                                               ",
"                                          XX............XXXXXXXXXXXXXXXX......XXX                                               ")

luca_cursor = pygame.cursors.compile(raphi_cursor, black='X', white='.', xor='.')
pygame.mouse.set_cursor((128, 128), (65, 51), *luca_cursor)

screen.fill("0xffffff")
pygame.draw.rect(screen, "0xf04f93", (100, 200, 365, 200), 200, 2000)
pygame.draw.circle(screen, "0xabcdef", (200, 100), 35.4, 20, True, False, True, False)
pygame.draw.ellipse(screen, "0xfedcab", (100, 150, 534, 260))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.rect(screen, "0xff7f05", (*event.pos, 5, 5))
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
        
        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, "0xff7f05", (*event.pos, 5, 5))

            


    pygame.display.update()
    clock.tick(60)
