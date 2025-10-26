def est_equilibre(expr):
    if expr == "":
        return True  # chaîne vide = équilibrée

    # Cherche d'abord un couple bien formé () ou []
    if "()" in expr:
        return est_equilibre(expr.replace("()", ""))  # enlève le couple et recommence
    if "[]" in expr:
        return est_equilibre(expr.replace("[]", ""))  # enlève le couple et recommence

    # S’il reste des parenthèses ou crochets non appariés
    for c in expr:
        if c in "()[]":
            return False

    return True

expr = "()[][]"
print(est_equilibre(expr))

