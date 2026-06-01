# 07. The Prompt is Everything

The same underlying question, asked two ways, gets you two completely different answers from the same model. Send both prompts to Lumi and watch the gap open up.

## Prompt 1 (vague)

```
Explain decorators
```

## Prompt 2 (specific)

```
Explain Python decorators in plain English for someone who knows basic Python but not this concept. Use one analogy and one short code example. Max 100 words.
```

## What changed

Run the vague prompt a few times and you'll notice the responses drift between runs. Sometimes the answer is long, sometimes short. Sometimes it assumes you're a beginner, sometimes it assumes you already know what a closure is. The specific prompt produces something close to what you actually wanted on almost every run, which is what this chapter is teaching you to do.
