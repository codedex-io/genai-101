# 11. Think Step by Step

Hard concepts get better answers when the model reasons out loud first. The technique has a fancy name (chain-of-thought) and a famously simple trigger phrase.

## The prompt

```
You are a patient Computer Science teacher. You avoid jargon at all costs.

Here are two examples of how I want concepts explained:

CONCEPT: list slicing
ANALOGY: Like cutting a length of ribbon. Pick where to start, where to end. A common mistake is forgetting that the end index is excluded.
CODE:
  nums = [10, 20, 30, 40]
  print(nums[1:3])  # [20, 30]

CONCEPT: f-strings
ANALOGY: A sentence template with blanks you fill in from variables.
CODE:
  name = 'Ada'
  print(f'Hello, {name}!')  # Hello, Ada!

For the new concept, first think step by step about:
  - What's the simplest way to describe this to a beginner?
  - What everyday thing is this most like?
  - What's the most common mistake people make?

Then write the answer in the same format as the examples.

Explain decorators.
```

Then try `generators`. For a comparison run, delete the `For the new concept, first think step by step about:` and the three bullet points block and send the same concept again.

## Why it helps

By committing to intermediate reasoning before the final answer, the model has a chance to catch its own mistakes mid-thought. The lift is small on easy concepts; on hard ones, it's the difference between a useful explanation and a confidently wrong one.
