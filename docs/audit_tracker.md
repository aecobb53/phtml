# PHTML Audit Tracker

Date: 2026-07-24
Audit depth: Quick, high-level
Project goal: Open-source HTML generation wrapper
Priority order provided by maintainer:
1. Developer ergonomics
2. Correctness
3. Maintainability
4. Performance
5. Test quality
6. Packaging/release quality

## How to use this tracker
- Move items between sections as decisions are made.
- Keep status values as: TODO, IN PROGRESS, DONE, WONT DO.
- Add links to PRs/issues as you implement.

## High-priority findings (quick audit)

### H1. Public API is wildcard-heavy and hard to reason about
Why this matters:
- Most modern Python libraries prefer explicit exports for discoverability, type checking, and stable public APIs.

Evidence:
- Wildcard re-export at package root.
- Wildcard imports used in runtime code and tests.

Suggested end-state:
- Explicit public API via __all__ at package root and module level.
- Keep star-import compatibility only if intentionally supported, but document it as legacy.

Status: TODO

### H2. Mutable defaults create shared-state bugs
Why this matters:
- Shared default list objects are a classic Python pitfall and a standards-level correctness issue.

Evidence:
- Mutable defaults in constructors for document styles/scripts and head global styles.

Suggested end-state:
- Replace list defaults with None and instantiate per object.

Status: TODO

### H3. Document rendering has side effects on repeated calls
Why this matters:
- render/get-output methods are expected to be idempotent in Python libraries.
- Calling output repeatedly should not mutate internal structure.

Evidence:
- Rendering appends styles/scripts into element trees on each call.

Suggested end-state:
- Make rendering pure: build temporary render tree or snapshot without mutating self.

Status: TODO

### H4. Parser and finder modules contain debug prints and brittle behavior
Why this matters:
- Library code should avoid print output unless routed through logging.
- Parsing logic should be robust and deterministic, especially for malformed input.

Evidence:
- Debug print statements in runtime modules.
- Parser does ad-hoc string/regex processing and broad symbol lookup.

Suggested end-state:
- Remove prints; use optional logger.
- Tighten parser behavior and error handling.

Status: TODO

## Medium-priority findings

### M1. Test suite passes but has weak assertions in key areas
Why this matters:
- A green suite can still miss regressions if tests do not assert behavior.

Evidence:
- Some tests only exercise code paths and do not assert outcomes.
- Some tests include local absolute paths and debug artifacts.

Suggested end-state:
- Convert smoke tests to assertion-based tests.
- Use test fixtures under tests/resources only.

Status: TODO

### M2. Packaging metadata is incomplete for open-source distribution
Why this matters:
- PyPI consumers expect clear metadata: classifiers, dependencies, optional dev extras, and build-system declarations.

Evidence:
- Minimal metadata in project config and setup script.
- Empty requirements file.

Suggested end-state:
- Keep a single source of truth in pyproject with full metadata.
- Add optional dependency groups for test/dev/docs.

Status: TODO

### M3. API consistency and typing can be stronger
Why this matters:
- Better type hints and consistent naming improve editor support and contributor confidence.

Evidence:
- Mixed typing coverage and mixed patterns for strings/lists/objects in methods.

Suggested end-state:
- Tighten type hints and method contracts.
- Define clear accepted types for content and attributes.

Status: TODO

## Implementation tracker

| ID | Area | Priority | Decision | Status | Notes | Link |
|---|---|---|---|---|---|---|
| H1 | Public API exports and imports | High | Implement | TODO | Replace wildcard API with explicit exports and __all__ | docs/h1_public_api_deep_dive.md |
| H2 | Mutable default arguments | High | Implement | TODO | Use None defaults and per-instance initialization |  |
| H3 | Idempotent rendering | High | Implement (learning-focused) | TODO | Make return_document/return_string_version side-effect free and document rationale | docs/h3_render_idempotency_deep_dive.md |
| H4 | Parser/finder logging and robustness | Low (deferred) | Defer for now | TODO | Remove prints and define parse error behavior in later cleanup |  |
| M1 | Test assertions and fixture hygiene | Medium | Implement | TODO | Remove environment-specific paths and add meaningful asserts | docs/m1_testing_strategy_deep_dive.md |
| M2 | Packaging metadata completeness | Medium | Implement | TODO | Consolidate metadata in pyproject and modernize release config |  |
| M3 | Typing and API contracts | Medium | Implement | TODO | Expand type hints and normalize accepted argument types | docs/m3_typing_contracts_deep_dive.md |
| D1 | AI-oriented library guide | Medium | Track, defer until API improvement | TODO | Create an AI-readable guide covering architecture, public API, invariants, and contribution expectations after the external API is improved |  |

## Candidate items to implement now
- H2 mutable defaults
- H3 idempotent rendering
- H1 explicit public API and __all__
- M1 remove debug prints and hardcoded test paths

## Maintainer decisions (2026-07-24)
- H1: approved to implement now.
- H2: approved to implement now.
- H3: approved to implement; include explanation-oriented changes so behavior is easier to reason about.
- H4: explicitly deferred and treated as low priority.
- M1: approved; stronger tests desired.
- M2: approved; packaging/release quality is important.
- M3: approved; API is now stable enough for stronger typing/contracts.

## Suggested phased rollout

### Phase 1: API correctness and ergonomics foundation
- H2 mutable default fixes.
- H3 side-effect-free rendering.
- H1 explicit exports with compatibility notes.
- Deliverable: no behavior regressions in current tests, clearer API surface.

### Phase 2: developer experience and confidence
- M3 type hints for public API and key internals.
- Docstring pass for public classes/methods with usage examples.
- M1 assertion-focused tests around rendering, parser edges, and element search.
- Deliverable: better editor autocomplete/help and safer refactors.

### Phase 3: packaging and release hardening
- M2 pyproject modernization (classifiers, optional-dependencies, metadata).
- Release workflow and versioning notes.
- Deliverable: cleaner open-source distribution posture.

### Phase 4: parser/finder cleanup (deferred)
- H4 remove debug prints and improve parser error model.
- Deliverable: reduced noise and clearer failure behavior.

## Developer ergonomics checklist
- Public API map: maintain a single explicit export list.
- Stable signatures: avoid ambiguous argument types unless documented.
- Type hints: prioritize user-facing methods first.
- Docstrings: include Parameters, Returns, Raises, and 1 short example.
- Error messages: actionable and specific.
- Changelog discipline: include migration notes for breaking changes.

## Additional themes surfaced by deeper dives
- Add a short API guarantees document describing what is stable, what is convenience-only, and what may change.
- Introduce regression-test discipline: each subtle bug fix should add one focused test.
- Consider lightweight CI across multiple Python versions before expanding feature scope.
- Add doc examples that mirror the intended public import style and typed usage.
- Add an AI-oriented maintainer guide after the external API is improved so it describes the intended stable model instead of transitional behavior.

## Candidate items to defer
- Parser rewrite for full HTML compliance (larger scope)
- Performance tuning beyond correctness and API cleanup
- AI-oriented library/developer guide until H1/H3/M3 reshape the external API

## Deferred documentation ideas
- AI-oriented library guide:
	- library purpose and non-goals
	- public API map and preferred import style
	- rendering and mutation invariants
	- typing and testing expectations
	- contribution guidance for safe refactors
	- write this after external API improvements land

## Candidate items to avoid for now
- Premature micro-optimizations
- Feature expansion before API cleanup and behavioral guarantees

## Conversation log
- 2026-07-24: Initial quick audit completed.
- Next: run a focused implementation pass on H2/H3/H1 in that order.
