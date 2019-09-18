from tkinter import *
import tkinter as tk
import time

# start position
START_TOP_X = 0
START_TOP_Y = 0
START_DOWN_X = 30
START_DOWN_Y = 30


class Maze(tk.Tk):
    def __init__(self):
        super(Maze, self).__init__()
        self.action = ['l', 'r', 'u', 'd']
        self.n_actions = len(self.action)
        self.current_position = [START_TOP_X, START_TOP_Y, START_DOWN_X, START_DOWN_Y]
        self.build_maze()

    # @staticmethod
    def build_maze(self):
        self.cv = Canvas(self, background='white')
        self.cv.pack(fill=BOTH, expand=YES)
        self.cv.create_rectangle(0, 0, 150, 150,
            outline='black',
            width=3)
        for i in range(5):
            self.cv.create_line((0, i * 30), (150, i * 30), width=2)
        for i in range(5):
            self.cv.create_line((i * 30, 0), (i * 30, 150), width=2)
        self.circular = self.cv.create_oval((START_TOP_X, START_TOP_Y),(START_DOWN_X, START_DOWN_Y), width=0,fill='yellow')
        self.cv.create_rectangle((120, 120), (150, 150), width=0, fill='red')
        self.cv.create_rectangle((120, 60), (150, 90), width=0, fill='black')
        # self.cv.create_rectangle((120, 120), (150, 150), width=0, fill='black')
        self.cv.pack()

    def reset_circular(self):
        self.update()
        self.cv.delete(self.circular)
        self.current_position = [START_TOP_X, START_TOP_Y, START_DOWN_X, START_DOWN_Y]
        self.circular = self.cv.create_oval((START_TOP_X, START_TOP_Y),(START_DOWN_X, START_DOWN_Y), width=0, fill='yellow')
        return self.current_position

    def action_step(self, action):
        if action == 'r' and self.current_position[0] != 120:  # right
            self.cv.move(self.circular, 30, 0)
            self.current_position[0] = self.current_position[0] + 30
            self.current_position[2] = self.current_position[2] + 30
        elif action == 'l' and self.current_position[0] != 0:  # left
            self.cv.move(self.circular, -30, 0)
            self.current_position[0] = self.current_position[0] - 30
            self.current_position[2] = self.current_position[2] - 30
        elif action == 'u' and self.current_position[1] != 0:  # up
            self.cv.move(self.circular, 0, -30)
            self.current_position[1] = self.current_position[1] - 30
            self.current_position[3] = self.current_position[3] - 30
        elif action == 'd' and self.current_position[1] != 120:  # down
            self.cv.move(self.circular, 0, 30)
            self.current_position[1] = self.current_position[1] + 30
            self.current_position[3] = self.current_position[3] + 30
        state = self.current_position
        # reward = 0
        if self.current_position == [120, 120, 150, 150]:
            reward = 1
            state = 'terminal'
            done = True
        elif self.current_position == [120, 60, 150, 90]:
            reward = -1
            state = 'terminal'
            done = True
        else:
            reward = 0
            done = False
        return state, reward, done

    def render(self):
        time.sleep(0.3)
        self.update()


def update():
    for t in range(3):
        # env.action_step('r')
        s = env.reset_circular()
        while True:
            env.render()
            s, r, done = env.action_step(1)
            print(s)
            if done:
                break


if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
