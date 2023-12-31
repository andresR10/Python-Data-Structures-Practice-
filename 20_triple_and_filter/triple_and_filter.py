def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # tripled = []

    # for num in nums:
    #     if num % 4 == 0:
    #         tripled_num = num * 3
    #         tripled.append(tripled_num)

    # return tripled

    # or a better way is list comprehension:

    return [num * 3 for num in nums if num % 4 == 0]
