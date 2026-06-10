# 10. Show, Don't Tell

Show the model two worked examples first, then ask it to produce a third. It copies the shape of the examples almost automatically, which is what makes few-shot prompting one of the more reliable techniques in this chapter.

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

Explain dictionaries.
```

Then run the same prompt with a different concept (`async/await`, `json handling`). The response should keep the same ANALOGY and CODE structure almost every time.

## One thing to watch

Keep the examples in the same shape. If they disagree on format, the model has to guess which one to copy, and you'll get inconsistent output.

Two examples is usually plenty for a pattern this size, and three starts to feel like overkill. The bigger risk isn't quantity but inconsistency between them.
