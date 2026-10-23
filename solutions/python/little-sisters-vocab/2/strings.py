"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return f"un{word}"

def make_word_groups(vocab_words):
    separator = f" :: {vocab_words[0]}"
    
    return separator.join(vocab_words)

def remove_suffix_ness(word):
    suffix_removed = word.removesuffix("ness")

    if suffix_removed.endswith("i"):
        suffix_removed = suffix_removed[:-1] + "y"

    return suffix_removed


def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip(".,") + "en"
