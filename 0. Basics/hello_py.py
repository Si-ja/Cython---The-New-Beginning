def say_hello_to(name, iterations=10000):
    """
    Say hello after itterating over some loops.

    name (str)      : whom to say hello to
    iterations (int): how many iterations to make. Default = 10,000
    """
    if iterations <= 0 or type(iterations) != int:
        iterations = 1

    for _ in range(iterations):
        # literally do nothing just pass
        pass

    return f"Hello {name}"