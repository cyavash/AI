def divide(a, b):
    """Return the float division of a by b."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b  # Fixed: use true division instead of floor division
