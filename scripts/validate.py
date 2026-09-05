# Build: eaba5c7f58322f66bb3500c36c79eb1c

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
