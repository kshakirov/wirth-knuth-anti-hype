# ADR 0006: The Shannon-Kolmogorov Duality Constraint in the Knuthian Zero-Overhead Pipeline

## Status
Proposed

## Context
We are migrating our Wirthian fixed-array Breadth-First Search (BFS) graph loop detector into Donald Knuth's single-array implicit architecture. The structural objective is to completely obliterate the auxiliary `w_visited` boolean history array. However, data cannot be destroyed without modifying the mechanics of its logical representation. We must formally define the theoretical boundaries of this resource transformation.

## Decision and Theoretical Refinement
We reject the naive simplification that states data is merely saved by removing arrays. Instead, we formally enforce the **Shannon-Kolmogorov Duality Constraint**, dividing the computational trade-offs into two independent scientific axes:

1. **The Shannon Axis (Spatial Complexity):** Claude Shannon's information theory dictates the physical volume of memory bits required to store state transitions in RAM. By squeezing the explicit `w_visited` structure into the core list, we reduce Shannon's spatial memory footprint to absolute zero overhead. To preserve entropy, we compress Shannon's alphabet, forcing a single 64-bit cell to cycle through three discrete states based on integer sign and scalar ranges.
2. **The Kolmogorov Axis (Algorithmic Complexity):** Andrey Kolmogorov defined the complexity of an object by the length of the shortest computer program needed to generate it. As Shannon's spatial footprint drops to zero, Kolmogorov's algorithmic complexity inside the CPU registers skyrockets. The source code must absorb multiple nested predicate checks, sign-bit evaluations, and pointer-chasing mechanics.

The operational taxonomy of this transition traces a strict evolution across three design stages:
- **Phase 1 (Levitin):** Minimal Kolmogorov code complexity / Maximum Shannon memory overhead (Dynamic dynamic arrays + hash sets).
- **Phase 2 (Wirth):** Moderate Kolmogorov code complexity / Optimized Shannon memory overhead (Frozen memory array + independent pointers).
- **Phase 3 (Knuth):** Peak Kolmogorov code complexity / Zero Shannon memory overhead (The single-array implicit transformer).

## Consequences
- **Positive:** Complete elimination of structural history overhead, forcing execution entirely within localized cache line bounds.
- **Negative:** Dramatic expansion of Kolmogorov algorithmic complexity, requiring rigid condition parsing inside the runtime CPU thread.
