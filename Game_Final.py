import pygame
import numpy as np
import time

col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)
print("All OK")

def update(plane, cur, sz):
    next = np.zeros((cur.shape[0], cur.shape[1]))
    
    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]
        
        col= col_background
        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_background
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            next[r, c] = 1
            col = col_alive
        
        pygame.draw.rect(plane, col, (c*sz, r*sz, sz-1, sz-1))
    
    return next

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    cells = np.random.choice(2,(dimy,dimx), p=[0.5,0.5] )
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    plane = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Sooraj's Game of Life")

    cells = init(dimx, dimy)

    #GEN START 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        plane.fill(col_grid) 
        cells = update(plane, cells, cellsize) 
        pygame.display.update()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Execution 
main(120,80,9)
     
