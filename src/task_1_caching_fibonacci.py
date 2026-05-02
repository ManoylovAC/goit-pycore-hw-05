def caching_fibonacci():
    '''
    The function returns a function that calculates the nth Fibonacci number.
    The function caches the results of previous calculations to improve performance.

    Returns:
        function: A function that calculates the nth Fibonacci number.
    '''
    cache = {}

    def fibonacci(n: int) -> int:
        '''
        The function calculates the nth Fibonacci number.

        Args:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.
        '''
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == '__main__':
    fib = caching_fibonacci()

    assert fib(10) == 55
    assert fib(15) == 610
    assert fib(20) == 6_765
    assert fib(42) == 267_914_296 

    print(
        [f'{fib(n):_}' for n in (10, 15, 20, 42)]
    )  # [55, 610, 6_765, 267_914_296]
