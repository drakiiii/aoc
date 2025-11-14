from collections import defaultdict
import heapq


def _parse_input(file):
    """Split the raw puzzle input into ordering rules and page updates."""
    with open(file) as f:
        raw_rules, raw_updates = f.read().strip().split("\n\n")

    page_rules = [tuple(map(int, line.split("|"))) for line in raw_rules.splitlines()]
    updates = [tuple(map(int, line.split(","))) for line in raw_updates.splitlines()]
    return page_rules, updates


def _is_order_valid(update, page_rules):
    """Return True if this update obeys every ordering rule."""
    positions = {value: idx for idx, value in enumerate(update)}
    for before, after in page_rules:
        if before in positions and after in positions and positions[before] > positions[after]:
            return False
    return True


def _topological_sort(update, page_rules):
    """Reorder the pages according to the dependency rules using Kahn's algorithm."""
    positions = {value: idx for idx, value in enumerate(update)}
    nodes = set(update)

    adjacency = defaultdict(set)
    indegree = {node: 0 for node in nodes}

    for before, after in page_rules:
        if before in nodes and after in nodes and after not in adjacency[before]:
            adjacency[before].add(after)
            indegree[after] += 1

    # Use a min-heap keyed by original index to maintain deterministic ordering.
    heap = []
    for node, degree in indegree.items():
        if degree == 0:
            heapq.heappush(heap, (positions[node], node))

    ordered = []
    while heap:
        _, current = heapq.heappop(heap)
        ordered.append(current)
        for neighbor in adjacency[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, (positions[neighbor], neighbor))

    if len(ordered) != len(update):
        raise ValueError("Cycle detected when reordering update.")

    return tuple(ordered)


def part1(file):
    """Sum the middle page numbers for updates already in correct order."""
    page_rules, updates = _parse_input(file)
    total = 0

    for update in updates:
        if _is_order_valid(update, page_rules):
            middle_idx = len(update) // 2
            total += update[middle_idx]

    return total


def part2(file):
    """Fix the bad updates and sum their middle page numbers instead."""
    page_rules, updates = _parse_input(file)
    total = 0

    for update in updates:
        if not _is_order_valid(update, page_rules):
            fixed = _topological_sort(update, page_rules)
            middle_idx = len(fixed) // 2
            total += fixed[middle_idx]

    return total
