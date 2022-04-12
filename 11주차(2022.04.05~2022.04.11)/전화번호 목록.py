def solution(phone_book):

    phone_book.sort()
    base = phone_book[0]

    for pn in phone_book[1:]:
        if pn.startswith(base):
            return False
        base = pn

    return True
