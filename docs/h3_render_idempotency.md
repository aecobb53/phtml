# H3: Render Idempotency

## Explain Like I Am 10
Imagine you have a LEGO castle, and every time you show it to a friend, you accidentally glue on an extra tower.

At first it looks fine, but if you show it 10 times, now it has 10 extra towers you never meant to add.

Render idempotency means: looking at your castle should not change your castle. In code, generating HTML output should not secretly modify your object.

## Slightly Deeper Explanation
A render method should be a pure read operation: same object state in, same output out, with no side effects.

If rendering mutates state (for example, appending styles/scripts while building output), repeated calls can duplicate content, make bugs hard to trace, and produce non-deterministic behavior.

Idempotent rendering improves correctness, makes tests reliable, and gives developers confidence that calling render multiple times is always safe.
