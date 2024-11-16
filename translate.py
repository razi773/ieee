pieces = {0: 'B', 1: 'K', 2: 'N', 3: 'P', 4: 'Q', 5: 'R', 6: 'b', 7: 'k', 8: 'n', 9: 'p', 10: 'q', 11: 'r', 12: 'f'}
# [11, 8, 6, 10, 7, 6, 8, 11, 9, 9, 9, 9, 9, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 3, 3, 3, 3, 3, 3, 3, 3, 5, 2, 0, 4, 1, 0, 2, 5]
def toFEN(labels):
    count = 0
    fen = ""
    for i, l in enumerate(labels):
        if i % 8 == 0 and i != 0:
            if count > 0:
                fen += str(count)
                count = 0
            fen += "/"
        if pieces[l] == 'f':
            count += 1
        elif count > 0:
            fen += str(count) + pieces[l]
            count = 0
        else:
            fen += pieces[l]
    if count > 0:
        fen += str(count)
    return fen


