from gym.envs.registration import register

register(
    id='agent-experiment-v0',
    entry_point='gym_agent_experiment.envs:agentExperimentEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)