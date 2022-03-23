import gym
from gym_custom.envs.foo_env import FooEnv

env = gym.make('foo-v0')

# initialize the environment
env.reset()
# 1000 cycles 
for _ in range(1000):
    # drawing
    env.render()
    # perform an action
    a = env.action_space.sample()
    s, r, d, _ = env.step(a) # take a random action
# close
env.close()