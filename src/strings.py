def main():
    print("x")


def remove_punctuations(str_engsentences):
    after_replace_engsentences = str_engsentences
    after_replace_engsentences = after_replace_engsentences.replace('.', '')
    after_replace_engsentences = after_replace_engsentences.replace(',', '')
    after_replace_engsentences = after_replace_engsentences.replace(':', '')
    after_replace_engsentences = after_replace_engsentences.replace(';', '')
    after_replace_engsentences = after_replace_engsentences.replace('!', '')
    after_replace_engsentences = after_replace_engsentences.replace('?', '')
    return after_replace_engsentences

def atgc_bppair(str_atgc):
    after_str_atgc = str_atgc
    after_str_atgc = after_str_atgc.replace('A', 'T')
    after_str_atgc = after_str_atgc.replace('T', 'A')
    after_str_atgc = after_str_atgc.replace('G', 'C')
    after_str_atgc = after_str_atgc.replace('C', 'G')
    return after_str_atgc

def swap_colon(str1):
    if str1.find(':') == -1:
        return str1
    colon_index = str1.index(':')
    # first_half = str1[:colon_index]
    # latter_half = str1[:colon_index]
    first_half, latter_half = str1[:colon_index], str1[colon_index + 1:]
    return latter_half + ":" + first_half

def atgc_count(str_atgc, str_bpname):
    return str_atgc.count(str_bpname)

def check_lower(str_engsentences):
    return str_engsentences.lower() == str_engsentences

def remove_clause(str_engsentences):
    index = len(str_engsentences) - str_engsentences.index(',') - 1
    return str_engsentences[-index:].lstrip().capitalize()

if __name__ == "__main__":
    print(swap_colon('Hello:Python'))
    # print(remove_clause("It's being seen, but you aren't observing.") == "But you aren't observing.")