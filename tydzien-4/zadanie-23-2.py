def play_game(player: str, computer_choice: str) -> int:
    choice_to_number = {
        'papier': 1,
        'kamień': 2,
        'nożyce': 3
    }

    player = choice_to_number[player]
    ai = choice_to_number[computer_choice]

    if (player == 1 and ai == 2) or (player == 2 and ai == 3) or (player == 3 and ai == 1):
        return 1
    if player == ai:
        return 0
    return 2


def test_play_game_player_wins():
    assert play_game('kamień', 'nożyce') == 1
    assert play_game('nożyce', 'papier') == 1
    assert play_game('papier', 'kamień') == 1

def test_play_game_computer_wins():
    assert play_game('nożyce', 'kamień') == 2
    assert play_game('papier', 'nożyce') == 2
    assert play_game('kamień', 'papier') == 2

def test_play_game_duce():
    assert play_game('nożyce', 'nożyce') == 0
    assert play_game('papier', 'papier') == 0
    assert play_game('kamień', 'kamień') == 0
