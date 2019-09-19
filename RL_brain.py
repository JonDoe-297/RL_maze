import numpy as np
import pandas as pd


class QTable:
    def __init__(self, actions):
        self.action = actions
        self.lr = 0.01
        self.gamma = 0.9
        self.epsilon = 0.9
        self.Q_Table = pd.DataFrame(columns=self.action, dtype=np.float64)

    def choose_action(self, state):
        self.check_state_exist(state)
        if np.random.uniform() < self.epsilon:
            state_action = self.Q_Table.loc[state]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            action = np.random.choice(self.action)
        return action

    def learn(self, state, action, reward, next_state):
        self.check_state_exist(next_state)
        predict = self.Q_Table.loc[state, action]
        if next_state != 'terminal':
            target = reward + self.gamma * self.Q_Table.loc[next_state].max()
        else:
            target = reward
        self.Q_Table.loc[state, action] += self.lr * (target - predict)

    def check_state_exist(self, state):
        if state not in self.Q_Table.index:
            self.Q_Table = self.Q_Table.append(
                pd.Series(
                    [0] * len(self.action),
                    index=self.Q_Table.columns,
                    name=state,
                )
            )

# if __name__ == '__main__':
#     data = {'state': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
#             'year': [2000, 2001, 2002, 2001, 2001, 2003],
#             'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
#     test_table = pd.DataFrame(data)
#     state = test_table[0:1]
#     print(state[state == np.max(state)])
#     # print(test_table[0:1])
#     # s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'f', 'e'])
#     # print(s)
#     # print(s.max())
#     # QT = QTable('d')
#     # QT.check_state_exist('[0, 0, 30, 30]')
