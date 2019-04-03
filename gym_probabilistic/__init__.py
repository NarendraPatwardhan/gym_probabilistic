from gym.envs.registration import register

register(
    id='pCartPole-v0',
    entry_point='gym_probabilistic.envs:CartPoleEnv',
)

register(
    id='pMountainCar-v0',
    entry_point='gym_probabilistic.envs:MountainCarEnv',
)

register(
    id='pMountainCarContinuous-v0',
    entry_point='gym_probabilistic.envs:MountainCarContinuous',
)

register(
    id='pPendulum-v0',
    entry_point='gym_probabilistic.envs:PendulumEnv',
)

register(
    id='pAcrobot-v0',
    entry_point='gym_probabilistic.envs:AcrobotEnv',
)

