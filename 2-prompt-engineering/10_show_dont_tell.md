# 10. Show, Don't Tell

Show the model two worked examples first, then ask it to produce a third one. It copies the shape of the examples almost automatically, which is what makes few-shot prompting one of the more reliable techniques in this chapter.

## The prompt

```
You are a patient Python teacher. You avoid jargon and never assume
the learner knows advanced topics.

Here are examples of how I want concepts explained:

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

Now explain this concept in the same format:

CONCEPT: decorators
```

Then run the same prompt with `CONCEPT: generators` and `CONCEPT: context managers`. The output should follow ANALOGY → CODE → COMMON MISTAKE almost every time.

## One thing to watch

Keep the examples in the same shape. If they disagree on format, the model has to guess which one to copy, and you'll get inconsistent output.

Two examples is usually plenty for a pattern this size, and three starts to feel like overkill. The bigger risk isn't quantity but inconsistency between them.
