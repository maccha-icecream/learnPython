import sys, enum


def canTransit(_from: str, _to: str) -> bool:
    if _from == '審査中' and _to in {'差し戻し中', '承認済み'}:
        return True
    if _from == '差し戻し中' and _to in {'審査中', '終了'}:
        return True
    if _from == '承認済み' and _to in {'実施中', '終了'}:
        return True
    if _from == '実施中' and _to in {'終了', '実施中'}:
        return True
    if _from == '中断中' and _to in {'実施中', '終了'}:
        return True
    return  False


if __name__ == "__main__":
    assert  canTransit('承認済み', '差し戻し中') == False
    assert  canTransit('審査中', '承認済み') == True