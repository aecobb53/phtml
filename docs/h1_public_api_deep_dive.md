# H1 Deep Dive: Public API Design and Exports

## What this topic is really about
A public API is the set of names and behaviors users are supposed to rely on.

For a Python library, this includes:
- what can be imported from the package root
- which classes/functions are documented and supported
- what behaviors are stable across releases

The deeper issue is not just imports. It is whether users can quickly understand what the library offers and which parts are safe to depend on.

## Why it matters
- Developer ergonomics: good autocomplete and clearer imports.
- Stability: contributors know what changes are breaking.
- Documentation: easier to generate and explain a defined surface.
- Tooling: type checkers, IDEs, and static analysis work better with explicit exports.

## Industry-standard approach
Most mature Python libraries do three things:
- export a deliberate set of root-level names
- keep internal helpers internal
- define stability by documentation and package structure

A package root should feel curated, not accidental.

## Recommended end-state for PHTML
At the package root, expose only the things you want users to reach for first.

Likely candidates:
- `Document`
- `HtmlReader`
- `FindElement`
- the major HTML element classes
- `Style`
- text-format helper classes that are intentionally public

Less suitable for root export unless intentionally supported:
- internal helper types
- private rendering utilities
- parser internals
- implementation-only aliases

## Suggested API shape
### Root package
Keep the common user experience simple:

```python
from phtml import Document, Div, Paragraph, Style
```

### Submodules
Also support more explicit imports for advanced users:

```python
from phtml.classes import Div, Paragraph
from phtml.document import Document
```

This is a common pattern: easy imports at the top, deeper paths available for clarity.

## Design principles
1. Explicit is better than implicit.
2. Convenience imports should be intentional, not wildcard spillover.
3. Anything exported at the root should be considered part of the supported API.
4. Internals should be easy to evolve without breaking users.

## Recommended implementation strategy
### Step 1: Define the support boundary
Make a written list of:
- root-level public names
- semi-public submodule names
- private/internal names

### Step 2: Add explicit exports
Use explicit imports and `__all__`.

This gives you:
- controlled star-import behavior
- clearer discoverability
- a concrete public contract

### Step 3: Keep compatibility in mind
If users may already rely on broad imports, provide a migration note before shrinking the surface.

### Step 4: Document the import style
Show two or three preferred import patterns in the README and docstrings.

## Decision questions
1. Is the library optimized for convenience at the root package?
2. Which classes are core enough to deserve root-level export?
3. Are text-format helpers first-class features or secondary utilities?
4. Do you want a smaller curated API or a broad convenience API?

Recommended answer:
- a curated but friendly root API

## Acceptance criteria
- `dir(phtml)` looks intentional, not noisy.
- Root imports match documented usage examples.
- Private implementation details are not accidentally exported.
- Breaking changes can be described clearly because the public surface is known.

## Good docstring/documentation pattern for this topic
For public classes and functions, document:
- one-sentence purpose
- common constructor arguments
- one short example
- any behavioral guarantees

This helps the package root act like a guided menu.

## Common mistake to avoid
Do not expose everything just because it is easy.

A large accidental API feels convenient at first, but it makes maintenance, docs, and breaking changes much harder later.

## Recommended rollout
1. Define the public root API list.
2. Add explicit `__all__` values.
3. Update examples/docs to match preferred import style.
4. Add a small import-compatibility test set.
