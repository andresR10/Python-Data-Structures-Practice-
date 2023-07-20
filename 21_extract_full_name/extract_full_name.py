def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    # extracted = []

    # for names in people:
    #     full_names = names['first'] + ' ' + names['last']
    #     extracted.append(full_names)

    # return extracted

    # or a better way with list comprehensions 
    return [name["first"]+ " " + name["last"] for name in people]
    