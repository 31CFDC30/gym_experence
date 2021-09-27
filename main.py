# -*- coding: utf-8 -*-
"""
Created on 2021/9/27 9:53

@author: qk
"""


def main():
    import gym

    env = gym.make('GridWorld-v1')
    env.reset()
    env.render()
    env.close()

    print("branch 2")


if __name__ == '__main__':
    main()
