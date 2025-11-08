import random
import time
from tkinter import *
from tkinter import messagebox
from functools import partial

class Tetris:

    def __init__(self):    
        self.root = Tk()
        self.root.title('Tetris')
        self.root.bind('<Left>', partial(self.move, -1))
        self.root.bind('<Right>', partial(self.move, 1))
        self.root.bind('<Up>', self.spin)
        self.root.bind('<Down>', self.fast)
        self.root.bind('a', self.medium)
        self.root.bind('p', self.pause)
        self.root.protocol('WM_DELETE_WINDOW', self.delete)
        
        self.lines = 0
        self.score = Label(self.root, text=self.lines, font=("Arial", 30), justify=LEFT)
        self.score.grid(row=0, column=0, columnspan=10)
        
        self.grid = [[self.griddy(Canvas(self.root, bg='white', width=25, height=25, highlightthickness=1, highlightbackground='black'), i, j+1) for i in range(10)] for j in range(20)]
        self.bool = [[False for i in range(10)] for j in range(20)]
        blocks = ['O', 'I', 'J', 'L', 'Z', 'S', 'T']
        self.blockColor = {'O':'yellow', 'I':'cyan', 'J':'blue', 'L':'orange', 'Z':'red', 'S':'green', 'T':'purple'}
        self.wait = False
        self.gameOver = False
        self.numBlocks = 0
        self.blocks = Label(self.root, text=f'Blocks: {self.numBlocks}', font=("Arial", 18))
        self.blocks.grid(row=21, column=0, columnspan=10)

        while not self.gameOver:
            
            self.block = random.choice(blocks)
            
            if self.block == 'O':
                x = random.randint(0, 8)
                self.grid[0][x ]['bg'], self.grid[0][x+1]['bg'], self.grid[1][x]['bg'], self.grid[1][x+1]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x, 0], [x+1, 1], [x+1, 0]]
                
            elif self.block == 'I':
                x = random.randint(0, 6)
                self.grid[1][x]['bg'], self.grid[1][x+1]['bg'], self.grid[1][x+2]['bg'], self.grid[1][x+3]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x+1, 1], [x+2, 1], [x+3, 1]]
                self.rotate = [[2, -1], [1, 0], [0, 1], [-1, 2]]
                
            elif self.block == 'J':
                x = random.randint(0, 7)
                self.grid[0][x]['bg'], self.grid[1][x]['bg'], self.grid[1][x+1]['bg'], self.grid[1][x+2]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x, 0], [x+1, 1], [x+2, 1]]
                self.rotate = [[1, -1], [2, 0], [0, 0], [-1, 1]]

            elif self.block == 'L':
                x = random.randint(0, 7)
                self.grid[1][x]['bg'], self.grid[1][x+1]['bg'], self.grid[1][x+2]['bg'], self.grid[0][x+2]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x+1, 1], [x+2, 1], [x+2, 0]]
                self.rotate = [[1, -1], [0, 0], [-1, 1], [0, 2]]

            elif self.block == 'Z':
                x = random.randint(0, 7)
                self.grid[0][x]['bg'], self.grid[0][x+1]['bg'], self.grid[1][x+1]['bg'], self.grid[1][x+2]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 0], [x+1, 1], [x+1, 0], [x+2, 1]]
                self.rotate = [[2, 0], [0, 0], [1, 1], [-1, 1]]

            elif self.block == 'S':
                x = random.randint(0, 7)
                self.grid[1][x]['bg'], self.grid[1][x+1]['bg'], self.grid[0][x+1]['bg'], self.grid[0][x+2]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x+1, 1], [x+1, 0], [x+2, 0]]
                self.rotate = [[1, -1], [0, 0], [1, 1], [0, 2]]

            else:
                x = random.randint(0, 7)
                self.grid[1][x]['bg'], self.grid[1][x+1]['bg'], self.grid[1][x+2]['bg'], self.grid[0][x+1]['bg'] = self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block], self.blockColor[self.block] 
                self.index = [[x, 1], [x+1, 1], [x+1, 0], [x+2, 1]]
                self.rotate = [[1, -1], [0, 0], [1, 1], [-1, 1]]
                
            self.root.update()
            self.speed = .5
            time.sleep(self.speed)
            
            while not self.gameOver and self.index[0][1] < 19 and self.index[1][1] < 19 and self.index[2][1] < 19 and self.index[3][1] < 19 and not self.bool[self.index[0][1]+1][self.index[0][0]] and not self.bool[self.index[1][1]+1][self.index[1][0]] and not self.bool[self.index[2][1]+1][self.index[2][0]] and not self.bool[self.index[3][1]+1][self.index[3][0]]:
                for i in self.index:
                    self.grid[i[1]][i[0]]['bg'] = 'white'                
                self.index[0][1], self.index[1][1], self.index[2][1], self.index[3][1] = self.index[0][1]+1, self.index[1][1]+1, self.index[2][1]+1, self.index[3][1]+1
                for i in self.index:
                    self.grid[i[1]][i[0]]['bg'] = self.blockColor[self.block]
                self.root.update()
                time.sleep(self.speed/2)
                self.root.update()
                time.sleep(self.speed/2)
                
            self.numBlocks += 1
            self.blocks['text'] = f'Blocks: {self.numBlocks}'
            
            stop = False
            for i in self.index:
                self.bool[i[1]][i[0]] = True
                if i[1] <= 0:
                    messagebox.showerror(title='Tetris', message='You lost!!!')
                    self.root.unbind('<KeyPress-Left>')
                    self.root.unbind('<KeyPress-Right>')
                    self.root.unbind('<Up>')
                    self.root.unbind('<Down>')
                    stop = True
                    break
            if stop:
                break
            
            i = 19
            while not self.gameOver and i>=0:
                if False not in self.bool[i]:
                    self.lines += 1
                    self.score['text'] = self.lines
                    for j in range(10):
                        self.grid[i][j]['bg'] = 'white'
                        self.bool[i][j] = False
                    for k in range(i-1, -1, -1):
                        for l in range(10):
                            if self.bool[k][l]:
                                self.grid[k][l]['bg'], self.grid[k+1][l]['bg'] = self.grid[k-1][l]['bg'], self.grid[k][l]['bg']
                                self.bool[k][l], self.bool[k+1][l] = self.bool[k-1][l], self.bool[k][l]
                    i += 1
                i -= 1
                
        self.root.destroy()

        
    def griddy(self, canvas, i, j):
        canvas.grid(row=j, column=i)
        return canvas
    
    def medium(self, bruh):
        self.speed = 0.1 if self.speed!=0.1 else 0.5
    
    def fast(self, bruh):
        self.speed = 0.01
        
    def pause(self, bruh):
        self.wait = not self.wait
        
        if self.wait:
            self.root.unbind('<Left>')
            self.root.unbind('<Right>')
            self.root.unbind('<Up>')
            self.root.unbind('<Down>')
            self.root.unbind('a')
            
        while not self.gameOver and self.wait:
            time.sleep(0.05)
            self.root.update()
            time.sleep(0.05)
            
        self.root.bind('<Left>', partial(self.move, -1))
        self.root.bind('<Right>', partial(self.move, 1))
        self.root.bind('<Up>', self.spin)
        self.root.bind('<Down>', self.fast)
        self.root.bind('a', self.medium)


    def delete(self):
        self.gameOver = True


    def move(self, x, bruh):
        if ((self.index[0][0]>0 and self.index[1][0]>0 and self.index[2][0]>0 and self.index[3][0]>0 and x==-1) or (self.index[0][0]<9 and self.index[1][0]<9 and self.index[2][0]<9 and self.index[3][0]<9 and x==1)) and not self.bool[self.index[0][1]][self.index[0][0]+x] and not self.bool[self.index[1][1]][self.index[1][0]+x] and not self.bool[self.index[2][1]][self.index[2][0]+x] and not self.bool[self.index[3][1]][self.index[3][0]+x]:
            for i in self.index:
                self.grid[i[1]][i[0]]['bg'] = 'white'                
            self.index[0][0], self.index[1][0], self.index[2][0], self.index[3][0] = self.index[0][0]+x, self.index[1][0]+x, self.index[2][0]+x, self.index[3][0]+x
            for i in self.index:
                self.grid[i[1]][i[0]]['bg'] = self.blockColor[self.block]
        
    def spin(self, bruh):
        if not self.block=='O' and 0<=self.index[0][0] + self.rotate[0][0]<=9 and 0<=self.index[1][0] + self.rotate[1][0]<=9 and 0<=self.index[2][0] + self.rotate[2][0]<=9 and 0<=self.index[3][0] + self.rotate[3][0]<=9 and not self.bool[self.index[0][1] + self.rotate[0][1]][self.index[0][0] + self.rotate[0][0]] and not self.bool[self.index[1][1] + self.rotate[1][1]][self.index[1][0] + self.rotate[1][0]] and not self.bool[self.index[2][1] + self.rotate[2][1]][self.index[2][0] + self.rotate[2][0]] and not self.bool[self.index[3][1] + self.rotate[3][1]][self.index[3][0] + self.rotate[3][0]]:
            for i in range(4):
                self.grid[self.index[i][1]][self.index[i][0]]['bg'] = 'white'
            for i in range(4):
                self.index[i][0], self.index[i][1] = self.index[i][0] + self.rotate[i][0], self.index[i][1] + self.rotate[i][1]
                self.grid[self.index[i][1]][self.index[i][0]]['bg'] = self.blockColor[self.block]
                self.rotate[i][0], self.rotate[i][1] = -self.rotate[i][1], self.rotate[i][0]
                
if __name__ == "__main__":
    Tetris()

