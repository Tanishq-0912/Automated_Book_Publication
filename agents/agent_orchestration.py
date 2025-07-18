from agents.writer import spin_chapter
from agents.reviewer import review_text
from agents.rl_reward import reward_score

def process_chapter(text, version_id, store_callback):
    spun = spin_chapter(text)
    reviewed = review_text(spun)
    score = reward_score(reviewed)
    store_callback(f"chapter_v{version_id}", reviewed)
    return reviewed, score
