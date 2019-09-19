import copy
from maze_env import Maze
from RL_brain import QTable


def update():
    for episode in range(50):
        observation = env.reset_circular()
        # print(observation)
        print(str(episode) + ':')
        while True:
            env.render()
            action = RL.choose_action(str(observation))
            if action == 0:  # up
                action_step = 'u'
            elif action == 1:  # down
                action_step = 'd'
            elif action == 2:  # right
                action_step = 'r'
            elif action == 3:  # left
                action_step = 'l'
            # RL take action and get next observation and reward
            observation_, reward, done = env.action_step(action_step)
            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))
            # swap observation
            observation = copy.copy(observation_)  # 浅拷贝深拷贝

            # break while loop when end of this episode
            if done:
                break
        print(RL.Q_Table)

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()