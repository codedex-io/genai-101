# 22. Trust but Verify

AI-generated code tends to look correct on first read because the model is trained to produce code that's plausible and idiomatic. Whether it actually works on the inputs you'd hit in practice is a different question, and that's the gap this exercise is about.

## Prompts

```
Write a Python function that returns the average of a list of numbers.
```

Then probe:

```
What does your function do if I pass it an empty list?
```

Try another one:

```
Write a Python function that checks if a string is a palindrome.
```

```
Does your function handle uppercase letters, spaces, and punctuation?
```

## What you're practicing

The skill on the table here is reading AI code the same way you'd read code from someone you don't know well. Did the first version handle `[]`, or would it have crashed with `ZeroDivisionError` the moment a real caller passed an empty list? Did the palindrome check ignore case and punctuation on its own, or did you have to nudge Lumi into adding that?

The model produces something that reads like the answer. Whether it is the answer comes down to the inputs you tried and the edge cases you remembered to ask about, which is the part it can't do for you.
