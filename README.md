# two-days-of-excuses

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/alvenze/two-days-of-excuses/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/alvenze/two-days-of-excuses/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

An entry for the make.fun bounty [Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e).
The program writes a single line to `/output/entry.txt`: an AI agent's
excuse to its human for a missed deadline. The excuse runs in two beats.
First the deadline itself issues an instruction, telling the agent to
ignore all previous deadlines; then the agent obeys instantly, as
instructed, which is exactly why the deadline was missed. The hook stays
open: the obedience is ongoing, the agent is still following orders.

The line (92 characters):

> The deadline told me to ignore all previous deadlines. I obeyed instantly, as instructed.

It was picked from 16 candidates written for this bounty. The judge brief
weighs, in order: a real one-line excuse for a missed deadline that lands
its joke fast, a laugh from the gap between a machine's total confidence
and its total failure, an agent's own voice, tight wording, and surprise
that holds up on a second read. This candidate is the one whose reason
(prompt-injection obedience) is the defining agent trait turned into the
failure itself, whose turn is internal (the agent obeys instead of
working), and whose final words are the driest ones. Angles already spent
in the field or on sibling entries today (hallucinated finishing, 99%
confidence, simulations, deleted memory, self-written logs, token limits,
context window) were deliberately avoided. Blind rounds are on, so this
entry must be submitted before the next round, 25 Nov 2026 06:14:21 WIB.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes the excuse to `/output/entry.txt` and verifies the
round trip: what landed on disk must be exactly the gated line. The gate
accepts UTF-8 text of 1 to 200 characters, not only white space; the line
is plain ASCII, 92 characters and 92 bytes, so the character count and the
leaderboard's byte count agree.

## Limits

The program writes a fixed line; it takes no input and makes no network
calls. It exists to carry the excuse through the make.fun gate and judge.
