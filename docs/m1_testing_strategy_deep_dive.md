# M1 Deep Dive: Testing Strategy for an HTML Generation Library

## Scope note
This deep dive is intentionally written from best practices for a library like PHTML, not from a review of the current test suite.

## What this topic is really about
Testing should prove that the library behaves correctly, predictably, and safely as the API evolves.

For an HTML generation library, the test goal is not just "does code run". The goal is to prove:
- HTML output is correct
- repeated operations are stable
- invalid input fails in understandable ways
- refactors do not break core guarantees

## What a good test strategy looks like
A strong test strategy has layers.

### 1. Unit tests for individual element behavior
These should cover:
- attribute serialization
- child insertion
- style/class handling
- text handling
- self-closing or special tags if supported

These tests should be small and fast.

### 2. Contract tests for public API behavior
These prove the promises users rely on.

Examples:
- rendering is repeatable
- chaining methods return `self`
- public constructors accept documented inputs
- public output methods return the documented types

### 3. Integration tests for document composition
These validate realistic combinations:
- document with head/body
- nested elements
- document-level styles/scripts
- mixed text and child elements

### 4. Regression tests for previously fixed bugs
Every subtle bug that gets fixed should ideally produce a focused test.

This is one of the best long-term investments in a library.

## Recommended testing principles
1. Test behavior, not implementation details.
2. Prefer explicit assertions over print/debug inspection.
3. Keep fixtures realistic but small.
4. Add a test when a bug teaches you something important.
5. Protect your invariants, not just your happy paths.

## Invariants worth testing for this library
Good candidates include:
- repeated render output is identical
- output generation does not mutate state
- attributes appear in expected serialized form
- nested content order is preserved
- text extraction is predictable
- invalid input either normalizes cleanly or raises a clear error

## Best test shapes for this kind of project
### Example-based tests
Use these for:
- exact HTML output
- small element combinations
- known edge cases

### Property-style tests
Even without a dedicated property-testing library, you can test broad rules such as:
- rendering twice gives the same result
- adding children preserves order
- empty inputs do not create stray markup

### Golden-file tests
Useful for larger HTML outputs.

Use them sparingly and only when they add clarity. They can become noisy if every tiny formatting change causes broad diffs.

Best use:
- one or two representative full-document outputs
- parser round-trip examples if round-trip behavior is an intended contract

## How much parser testing to do
For a parser/reader component, prioritize:
- valid small examples
- malformed input handling expectations
- round-trip checks only if round-trip fidelity is an explicit goal

Do not try to prove complete HTML-spec compliance unless that is actually a project goal.

## What to automate in CI
A good baseline:
- run tests on multiple Python versions
- fail on test failures
- optionally run a formatter/linter/type check later

For an open-source library, multi-version CI is often more valuable than adding many exotic tests early.

## Recommended coverage priorities
### Highest priority
- `Document` composition and rendering
- base element serialization
- style/class/attribute behavior
- invariants like idempotency

### Medium priority
- parser/search happy paths
- nested edge cases
- invalid inputs and error messages

### Lower priority at first
- exhaustive combinations of all element classes
- large snapshot sprawl

## Acceptance criteria
- Core behaviors are protected by small, direct tests.
- Bugs become regression tests.
- CI can catch breakage before release.
- Tests help refactoring instead of getting in the way.

## Common mistakes to avoid
- treating code execution as proof of correctness
- overusing giant snapshot files
- testing only happy paths
- writing tests tightly coupled to internal structure when user-facing behavior is what matters

## Recommended rollout
1. Define core invariants and public contracts.
2. Add focused unit tests around those guarantees.
3. Add a few integration tests for realistic document generation.
4. Add regression tests whenever fixes land.
5. Run the suite across multiple supported Python versions in CI.
