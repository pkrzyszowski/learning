def sort_cards(cards):
    card_to_int = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13}
    int_to_card = {i: card for card, i in card_to_int.items()}
    int_cards = [card_to_int[card] for card in cards]
    int_cards.sort()
    sorted_cards = [int_to_card[i] for i in int_cards]
    return sorted_cards


if __name__ == '__main__':
    test_cards1 = [5, 9, 3, 2, 'A', 'K', 10, 'Q', 2, 'A', 'J', 5]
    test_cards2 = (5, 9, 3, 2, 'A', 'K', 10, 'Q', 2, 'A', 'J', 5)

    print("Test1:",  sort_cards(test_cards1))
    print("Test2:", sort_cards(test_cards2))
