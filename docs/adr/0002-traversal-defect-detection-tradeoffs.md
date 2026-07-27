# ADR 0002: Architectural Trade-Offs in Breadth-First Search (BFS) Defect Detection

## Status
Proposed

## Context
We are choosing between two competing algorithmic paradigms for detecting topological loops (cycles) within an immobilized matrix-based BFS pipeline:
1. **Implicit Metric Balance (Knuth's Approach):** Blind runtime edge/vertex counting with deterministic post-traversal mathematical verification.
2. **Explicit Spatial Awareness (Generational Levels):** Tracking node generations (levels) to detect backward edges instantly on the fly.

## Comparative Analysis

### Approach 1: Post-Traversal Metric Balance
- **Mechanics:** The execution pipeline remains blind inside the `while` loop, incrementing flat register counters upon every valid matrix discovery. Cycle evaluation occurs strictly upon queue termination via dimensional inequality or in-degree reduction blocks.
- **Pros:** True Zero-Overhead memory consumption. Zero dynamic memory allocation. Perfect L1/L2 cache line locality. Deterministic $O(V + E)$ linear time complexity.
- **Cons:** Complete lack of incremental feedback. Cannot execute early termination upon encountering a defect; must process the entire accessible graph.

### Approach 2: On-the-Fly Generational Tracking
- **Mechanics:** Every node pushed to the pipeline is assigned a scalar generation height ($L_{child} = L_{parent} + 1$). The `elif` boundary compares the ancestor's height against the descendant's. A backward link targeting a higher or equal tier triggers an immediate defect alert.
- **Pros:** Instantaneous failure detection allowing immediate loop termination (`break`), bypassing massive trailing graph branches. Independent of global graph connectivity constraints.
- **Cons:** Forces Memory Bloat by allocating an auxiliary array of size $V$ for layer metadata. Induces continuous CPU cache misses due to non-contiguous lookups in the level storage array.

## Decision
To ensure maximum objectivity and alignment with the anti-hype manifesto, we will implement and commit **both paradigms** into the repository. 
1. We will first refine the standard pipeline into a Wirthian pointer-driven array system to establish the base benchmark.
2. We will then branch the source tree to demonstrate the exact runtime, memory footprint, and cache-miss differences between Knuth's implicit balance and the spatial level-tracking approach.
