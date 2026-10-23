"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

FACE_CARD_VALUE = 10
BLACKJACK_SCORE = 21
HIGH_ACE_VALUE = 11
LOW_ACE_VALUE = 1
DOUBLE_DOWN_TOTALS = {9, 10, 11}
FACE_CARDS = {"J", "Q", "K"}
TEN_CARDS = FACE_CARDS.union({"10"})


def value_of_card(card, ace_value=LOW_ACE_VALUE):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.
        ace_value (int): The value of the ace, has a default of LOW_ACE_VALUE.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1 or 11
        3.  '2' - '10' = numerical value.
    """

    if card in FACE_CARDS:
        return FACE_CARD_VALUE
    if card == "A":
        return ace_value
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1 or 11
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        return card_one, card_two
    if card_one_value > card_two_value:
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    card_one_value = value_of_card(card_one, HIGH_ACE_VALUE)
    card_two_value = value_of_card(card_two, HIGH_ACE_VALUE)

    current_total = card_one_value + card_two_value

    if current_total + HIGH_ACE_VALUE > BLACKJACK_SCORE:
        return LOW_ACE_VALUE
    return HIGH_ACE_VALUE


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    return (card_one in TEN_CARDS and card_two == "A") or (
        card_two in TEN_CARDS and card_one == "A"
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    return card_one_value == card_two_value


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    current_total = card_one_value + card_two_value

    return current_total in DOUBLE_DOWN_TOTALS
