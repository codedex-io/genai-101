# 11. Think Step by Step

Hard concepts get better answers when the model reasons out loud first. The technique has a fancy name (chain-of-thought) and a famously simple trigger phrase.

## The prompt

```
You are a patient Python teacher. You avoid jargon and never assume
the learner knows advanced topics.

Here are examples of how to explain Python concepts:

CONCEPT: list slicing
ANALOGY: Like cutting a length of ribbon. Pick where to start, where to end.
CODE:
  nums = [10, 20, 30, 40]
  print(nums[1:3])  # [20, 30]
COMMON MISTAKE: Forgetting that the end index is excluded.

CONCEPT: f-strings
ANALOGY: A sentence template with blanks you fill in from variables.
CODE:
  name = "Ada"
  print(f"Hello, {name}!")  # Hello, Ada!
COMMON MISTAKE: Forgetting the f prefix. Python won't substitute the variable.

For the new concept, first think step by step about:
  - What's the simplest way to describe this to a beginner?
  - What everyday thing is this most like?
  - What's the most common mistake people make?

Then write the answer in the same format as the examples.

CONCEPT: recursion
```

Then try `metaclasses`, and run the same concept through the Exercise 10 prompt (no thinking step) for comparison.

## Why it helps

By committing to intermediate reasoning before the final answer, the model has a chance to catch its own mistakes mid-thought, and the final answer lands sharper as a result. The lift is small on easy concepts; on hard ones, it's the difference between a useful explanation and a confidently wrong one.
