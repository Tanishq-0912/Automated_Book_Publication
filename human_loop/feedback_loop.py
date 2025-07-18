# Directory: human_loop/feedback_loop.py

def get_human_feedback():
    print("\n[Human Review] Do you want to:")
    print("1. Accept\n2. Revise\n3. Reject")
    choice = input("Enter your choice (1/2/3): ")
    return choice

