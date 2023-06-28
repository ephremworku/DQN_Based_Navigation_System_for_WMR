from gym.envs.registration import register

register(
    id='Wmr-v0',
    entry_point='gym_game.envs.custom_env:CustomEnv',
    max_episode_steps=2000,
)
