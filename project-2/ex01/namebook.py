def format_names(dct: dict[str, str]) -> list[str]:
    """
    reiceive a dict of first name as key and last name as value and return
    a list of all items of the dict with first name and last name capitalized
    """
    return [f"{item[0].capitalize()} {item[1].capitalize()}" for item in dct.items()]
