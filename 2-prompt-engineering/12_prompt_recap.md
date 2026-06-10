# 12. Prompt Recap

The Study Buddy started as `Explain decorators`. It now looks like this:

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

Explain {concept}.
```

## What's in there

What you've actually built is four techniques layered into one prompt. Specificity at the top, role to set the voice, two worked examples for the format, and a brief reasoning step before the answer comes out. The system prompts behind real products like Cursor or Claude Projects are longer and more carefully tuned, but they sit on the same scaffolding.

Save this prompt somewhere outside the lesson before you move on. It works in any chat interface you might use later, and the next chapters won't ask you to keep refining it.
