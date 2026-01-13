def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    More efficient than recursion.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def fibonacci_generator(limit):
    """
    Generate Fibonacci numbers up to a limit.

    Args:
        limit: Maximum number of Fibonacci numbers to generate

    Yields:
        The next Fibonacci number in the sequence
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci_sequence(n):
    """
    Generate the first n Fibonacci numbers as a list.

    Args:
        n: Number of Fibonacci numbers to generate

    Returns:
        List of the first n Fibonacci numbers
    """
    return list(fibonacci_generator(n))


if __name__ == "__main__":
    # Example usage
    print("First 10 Fibonacci numbers:")
    print(fibonacci_sequence(10))

    print("\n10th Fibonacci number (iterative):")
    print(fibonacci_iterative(10))

    print("\n15th Fibonacci number (recursive):")
    print(fibonacci_recursive(15))
