# --- Phase 2 : Vérification du gagnant ---
def victoire(symbole):
    b = [btns[i]['text'] for i in range(9)]
    return (
        (b[0] == b[1] == b[2] == symbole) or
        (b[3] == b[4] == b[5] == symbole) or
        (b[6] == b[7] == b[8] == symbole) or
        (b[0] == b[3] == b[6] == symbole) or
        (b[1] == b[4] == b[7] == symbole) or
        (b[2] == b[5] == b[8] == symbole) or
        (b[0] == b[4] == b[8] == symbole) or
        (b[2] == b[4] == b[6] == symbole)
    )