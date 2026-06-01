# 12. Iterate

The named techniques you've picked up so far (specificity, role, few-shot, chain-of-thought) are the tools you have. The actual skill is the editing loop you run with them, which is what the rest of this exercise gives you reps on.

## Start here

Paste the Exercise 11 prompt into the chat and run it on something genuinely hard:

```
[Exercise 11 prompt]

CONCEPT: metaclasses
```

## The loop

1. Run the prompt.
2. Read the output and name the problem out loud. Something like "too long," "made up a method that doesn't exist," "missed the COMMON MISTAKE field," or "analogy is forced."
3. Change one thing in the prompt that addresses that one weakness.
4. Run again. Did it get better? Did something else break in the process?
5. Repeat.

Two or three rounds is usually enough to get to something you'd actually keep.

## Common moves

- Response too long → tighten or add the word limit.
- Analogy is bad → add an example with a strong analogy for a hard concept.
- Code is wrong → "the code must run correctly in Python 3."
- Extra commentary at the end → "stop after the COMMON MISTAKE line."

Resist editing five things at once. If you do, you won't know which fix actually helped, and any comparison against the previous run stops being meaningful.
