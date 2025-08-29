def format_cents(nbr: int) -> str:
    """a function that receives a int represetn cents and return a a new string formated with [+] R$ cents"""
    if not isinstance(nbr, int):
        raise ValueError("Received a invalid input, expected a int")
    value = float(nbr) / 100
    if value < 0:
        value *= -1
    integer, decimal = f"{value:,.2f}".split(".")
    integer = integer.replace(",", ".")
    if nbr >= 0:
        return f"[+] R$ {integer},{decimal}"
    else:
        return f"[-] R$ {integer},{decimal}"
