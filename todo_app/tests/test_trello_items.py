from todo_app.data.viewmodel import ViewModel
from todo_app.data.Item import Item
from todo_app.tests.dummy_data import get_dummy_cards_response


def test_todo_items():

    # Arrange
    cards = []
    trellolists = get_dummy_cards_response()
    for trellolist in trellolists:
        for card in trellolist ["cards"]:
            item = Item.from_trello_card(card, trellolist)
            cards.append(item)
    view_model=ViewModel (cards,"Done")
    # Act
    todo_items = view_model.todo_items

    # Assert
    assert todo_items[0].name == "cheese"
    assert todo_items[1].name == "hello liam"
    assert len (todo_items) == 2

def test_doing_items():

    # Arrange
    cards = []
    trellolists = get_dummy_cards_response()
    for trellolist in trellolists:
        for card in trellolist ["cards"]:
            item = Item.from_trello_card(card, trellolist)
            cards.append(item)
    view_model=ViewModel (cards,"Done")
    # Act
    doing_items = view_model.doing_items

    # Assert
    assert doing_items[0].name == "Hello "
    assert doing_items[1].name == "cheese"
    assert doing_items[2].name == "greg"
    assert len (doing_items) == 3

def test_done_items():

    # Arrange
    cards = []
    trellolists = get_dummy_cards_response()
    for trellolist in trellolists:
        for card in trellolist ["cards"]:
            item = Item.from_trello_card(card, trellolist)
            cards.append(item)
    view_model=ViewModel (cards,"Done")
    # Act
    done_items = view_model.done_items

    # Assert
    assert done_items[0].name == "Dane"
    assert len (done_items) == 1