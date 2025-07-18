# analysis.md
## AI Writer & Reviewer Performance
Each iteration of the chapter undergoes rewriting and review. The LLM spins the text creatively, then a second pass improves grammar and clarity.

## Reward Function
We calculate a pseudo-RL reward score using:
- Length of output
- Randomized readability score (in practice, replace with actual readability scoring metrics)

This is used to guide which versions are worth keeping or improving.

## Version Tracking
ChromaDB stores each chapter version. Semantic search lets us retrieve earlier versions for comparison or reference.

## Score Distribution Chart
Below is a sample histogram of reward scores for different versions:

```python
import matplotlib.pyplot as plt

scores = [0.78, 0.84, 0.92, 0.85, 0.90]

plt.hist(scores, bins=5, edgecolor='black')
plt.title("Reward Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
```

## Conclusion
This system provides an end-to-end framework to spin, refine, and finalize AI-generated book chapters using feedback loops and memory. It's a useful base for future automation of content generation with human supervision.
