def play_game(player_choice: str, computer_choice: str) -> int:
    choice_to_number = {
        "papier": 1,
        "kamien": 2,
        "nozyce": 3
    }
    pl_choice = choice_to_number[player_choice]
    ai_choice = choice_to_number[computer_choice]
    if ((pl_choice == 1 and ai_choice == 2) or
            (pl_choice == 2 and ai_choice == 3) or
            (pl_choice == 3 and ai_choice == 1)):
        return 1
    if pl_choice == ai_choice:
        return 3
    return 2


def test_play_game_player_wins():
    assert play_game("kamien", "nozyce") == 1
    assert play_game("nozyce", "papier") == 1
    assert play_game("papier", "kamien") == 1


def test_play_game_computer_wins():
    assert play_game("nozyce", "kamien") == 2
    assert play_game("papier", "nozyce") == 2
    assert play_game("kamien", "papier") == 2


def test_play_game_draw():
    assert play_game("nozyce", "nozyce") == 3
    assert play_game("papier", "papier") == 3
    assert play_game("kamien", "kamien") == 3


# ================================================================================
from random import choice

if __name__ == "__main__":
    player = input("Wybierz papier, kamien lub nozyce: ")
    while player not in ["kamien", "papier", "nozyce"]:
        player = input("Wybierz papier, kamien lub nozyce: ")
    computer = choice(["kamien", "papier", "nozyce"])
    print(f'Computer wybral {computer}')
    result = play_game(player, computer)
    if result == 1:
        print("gracz wins")
    elif result == 2:
        print("com wins")
    else:
        print("draw")

# python -m pytest 1_3_TDD_zad2.py -vvv
