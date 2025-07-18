# Directory: orchestrator.py
from scraping.fetch_chapter import fetch_chapter_text
from agents.agent_orchestration import process_chapter
from human_loop.feedback_loop import get_human_feedback
from voice.voice_interface import read_text

CHAPTER_PATH = "data/raw/gates_ch1.txt"


def orchestrate():
    fetch_chapter_text("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1", "gates_ch1")


    with open(CHAPTER_PATH, "r", encoding="utf-8") as f:
        original = f.read()

    version = original
    version_id = 1

    while True:
        reviewed, score = process_chapter(version, version_id, lambda key, value: None)

        print(f"\n[AI Output v{version_id}] Reward Score: {score:.2f}\n")
        print(reviewed[:300] + "...\n")
        read_text(reviewed[:300])

        action = get_human_feedback()
        if action == "1":
            print("✅ Finalized and accepted!")
            break
        elif action == "2":
            print("🔁 Revise based on previous output...")
            version = reviewed
            version_id += 1
        elif action == "3":
            print("❌ Rejected. Exiting.")
            break
        else:
            print("Invalid input. Exiting.")
            break

if __name__ == "__main__":
    orchestrate()
