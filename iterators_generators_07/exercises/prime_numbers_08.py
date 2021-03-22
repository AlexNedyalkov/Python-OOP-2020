def get_primes(list_of_integers: list):
    for num in list_of_integers:
        if num == 1 or num == 0:
            continue
        counter = 0
        for i in range(2, num):
            if num % i == 0:
                continue
            else:
                counter += 1
        if counter >= num - 2:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
