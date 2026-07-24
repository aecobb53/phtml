# H3 Deep Dive: Render Idempotency

## What this topic is really about
Render idempotency means output generation is a read-only operation.

If an object has not changed, calling `render`, `return_document`, or `to_html` multiple times should:
- return the same output
- leave the object in the same state
- avoid duplicating child elements, styles, scripts, or attributes

This is a standard expectation in mature Python libraries because serialization is usually treated as observation, not mutation.

## Why it matters
- Correctness: repeated renders stay stable.
- Debuggability: developers do not have to wonder whether "just printing" an object changed it.
- Testability: you can assert output twice without side effects.
- Maintainability: write operations stay in one place, so data flow is easier to reason about.

## Core design rule
Only explicit mutator methods should change state.

Examples of mutators:
- `add_element`
- `add_style`
- `add_class`
- `set_indent_width`

Examples of non-mutators:
- `return_document`
- `return_string_version`
- `text`

## The industry-standard model
A mature HTML-building library usually separates:
- the object model: Python objects that hold structure and attributes
- the serializer: code that turns that structure into HTML text

The serializer reads from the model but does not write back into it.

## Recommended end-state for PHTML
1. Treat `Document`, `Head`, `Body`, and element classes as the source of truth.
2. Make render methods compute output from current state without appending temporary nodes.
3. If a render needs combined data, build that combination in local variables only.
4. Keep mutation inside explicit API methods.

## Good implementation patterns
### Pattern A: Local render composition
At render time, create temporary local lists such as:
- `head_items_for_render`
- `body_items_for_render`

These can combine:
- user-added children
- computed style tags
- computed script tags

Then serialize those locals without modifying `self`.

Why this is good:
- minimal architectural change
- easy to test
- preserves current API shape

### Pattern B: Dedicated serializer helper
Create helper methods like:
- `_render_head_items()`
- `_render_body_items()`
- `_serialize_node(node)`

Why this is good:
- easier to read
- cleaner separation of concerns
- better stepping stone if the library grows

### Pattern C: Cached rendering with invalidation
Only worth doing later if performance becomes an issue.

Why this is good:
- avoids repeated expensive serialization
- still keeps rendering read-only

Why not now:
- adds complexity too early

## Decision questions
1. Should styles/scripts be stored as first-class data or injected only at render time?
2. Should document rendering rely on temporary wrapper elements or direct serialization helpers?
3. Do you want every public output method to be guaranteed side-effect free?

Recommended answers:
- store data separately, inject only in local render composition
- use helpers if they improve clarity
- yes, all output methods should be side-effect free

## Acceptance criteria
- Rendering the same object twice produces the same string.
- Rendering does not change lengths of internal lists.
- Repeated calls do not duplicate style or script output.
- Output methods can be called in tests, repr/debug helpers, and docs examples safely.

## Test strategy for this topic
Add tests that prove:
- same output on first and second render
- no changes to child/style/script collection sizes after render
- nested elements remain unchanged after render
- output methods on individual elements are also repeatable

## Common mistake to avoid
Do not fix this by mutating state once and then trying to remember whether rendering already happened.

That creates hidden lifecycle state and usually makes the code harder to reason about.

## Recommended rollout
1. Make `Head` rendering pure.
2. Make `Document` rendering pure.
3. Add idempotency tests.
4. Then consider whether helper methods improve readability.
