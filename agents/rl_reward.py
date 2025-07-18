# Directory: agents/rl_reward.py
import random

def reward_score(text):
    length_score = len(text.split())
    readability_score = random.uniform(0.7, 1.0)
    final_score = 0.4 * length_score + 0.6 * readability_score
    return final_score
