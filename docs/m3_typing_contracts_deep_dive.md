# M3 Deep Dive: Typing and API Contracts

## What this topic is really about
Typing is not just for strictness. In a library, typing is a way to explain what kinds of values users are allowed to pass and what they should expect back.

API contracts are the broader version of that idea:
- what inputs are accepted
- what outputs are returned
- what side effects happen
- what errors are raised

A stable library benefits a lot from making these rules explicit.

## Why it matters
- Better autocomplete and editor help.
- Easier onboarding for contributors and users.
- Safer refactors.
- Fewer ambiguous behaviors hidden behind "it accepts lots of things".

## Industry-standard approach
Mature Python libraries usually type the public API first.

That means:
- constructors
- user-facing methods
- return types
- common container shapes

They do not necessarily type every internal detail immediately.

## Recommended end-state for PHTML
Define a small set of core concepts and reuse them consistently.

Examples of concepts worth naming:
- renderable node
- text-like content
- style input
- attribute mapping

A good long-term direction is to have a few reusable type aliases instead of repeating large unions everywhere.

## Suggested typing philosophy
1. Be permissive only where the API genuinely needs flexibility.
2. Normalize input early.
3. Keep return types predictable.
4. Prefer a smaller number of well-defined accepted shapes.

For example, if `internal` can accept a single item or a list, normalize that immediately and store one canonical representation internally.

## Contract questions worth answering
1. What is valid element content?
2. Can style input be a string, mapping, style object, or list of those?
3. What methods always return `self` for chaining?
4. What methods return strings versus lists of strings?
5. What exceptions should users expect for invalid input?

These answers should be reflected in both types and docstrings.

## Recommended implementation strategy
### Phase 1: Public methods
Type:
- package-level entry points
- constructors of main element classes
- `Document`
- parser/search public methods
- common rendering properties/methods

### Phase 2: Shared aliases/protocols
Introduce reusable types such as:
- `Renderable`
- `ContentItem`
- `StyleInput`

### Phase 3: Error contracts
Document and type-check the expected invalid-input behavior.

## How strict to be
For this kind of library, medium strictness is usually best.

That means:
- public methods are clearly typed
- internal storage types are consistent
- implementation details can stay looser until needed

## Acceptance criteria
- A user can inspect signatures and understand what to pass.
- Common editor hints are useful without reading source.
- The library has fewer "accept anything and hope" pathways.
- Refactors can rely on stable type expectations.

## Docstring pattern that pairs well with typing
For each public API item:
- summary sentence
- parameters and accepted shapes
- return value
- raises
- short example

Types tell tools what is allowed. Docstrings tell humans how to use it.

## Common mistake to avoid
Do not copy current loose behavior into types without thinking.

If the API accepts too many unrelated shapes today, use this moment to decide which ones are actually worth supporting long term.

## Recommended rollout
1. Type the package root entry points and `Document` first.
2. Define 2-4 reusable aliases for common value shapes.
3. Type the core element base and frequently used element constructors.
4. Tighten error contracts and docstrings after that.
