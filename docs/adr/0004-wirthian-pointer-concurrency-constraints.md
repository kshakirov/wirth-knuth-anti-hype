# ADR 0004: Execution Pipeline Synchronization and Pointer Autonomy in Wirthian Fixed Arrays

## Status
Accepted

## Context
We are migrating the validated loop detection logic from high-level dynamic lists to a memory-immobilized array according to Niklaus Wirth's constraints. The core objective is to lock the C-level `ob_item` pointer vector in RAM, eliminating structural `memmove()` overhead. However, replacing `pop(0)` and `append()` with manual index pointers introduces critical synchronization risks regarding pointer convergence and data overwrites.

## Decision
We enforce a strict linear FIFO pipeline over a fixed array $Q$ of size $V$ (where $V = |TotalVertices|$). To avoid linear lookup degradation ($O(V)$) when checking discovery history, the execution state is explicitly split into two independent architectural structures:
1. **Queue Buffer ($Q$):** A static array tracking only the active wave frontier. Elements are written sequentially from left to right and are never shifted or deleted.
2. **State Register (`visited`):** A separate flat boolean array of size $V$ dedicated strictly to constant-time $O(1)$ vertex historical tracking.

Execution control is transferred to two independent, single-direction integer registers simulating CPU address pointers: `head` (the interrogation cursor) and `tail` (the free memory allocation cursor). The pipeline execution is bound to the hardware inequality constraint: `while head < tail`.

## Refined Synchronization Protocol and Risk Mitigation
To maintain perfect operational determinism and prevent infinite loop states or memory corruption, the mutation of register counters must adhere to the following hardware-level isolation constraints:

1. **Absolute Counter Autonomy:** Expressions coupling pointer states dynamically (such as `tail = head + 1`) are strictly rejected. The `tail` register must mutate independently of `head`. 
2. **Conditional Tail Mutation:** Incrementing the allocation cursor (`tail += 1`) must occur exclusively inside the nested loop (`for j`) at the exact point of writing a new, unvisited node to $Q$. If a row yields no new nodes, `tail` must remain frozen.
3. **Top of Loop Interrogation:** The extraction of the current row index ($i = Q[head]$) and the subsequent progress of the tracking cursor (`head += 1`) must occur immediately at the apex of the `while` loop, releasing the register before nested matrix operations begin.
4. **Linear Bound Invariant:** In connected topologies with boolean history guards, duplicate nodes are banned. Thus, `tail` increases monotonically and is guaranteed never to exceed the upper memory boundary $V$. Circular modulo wrapping (`tail % V`) is discarded as redundant for this tier.

## Consequences
1. **Positive:** Complete elimination of C-level memory relocations, restoring true hardware linear efficiency.
2. **Positive:** Seamless structural trap interception within the nested `elif` clause at $O(1)$ efficiency.
3. **Negative:** Manual cross-pointer alignment tracking increases initial testing complexity in Python runtimes.
