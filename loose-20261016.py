"""Scratch module."""

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def flatten(xs):
    return [y for x in xs for y in x]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None
