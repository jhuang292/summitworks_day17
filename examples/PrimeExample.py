def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False
        # -ve prime, if you want to verficate, you have to add more script
# # 

#     if number <= 0:
#         return False

    for element in range(2,number):
    #for element in range(number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)