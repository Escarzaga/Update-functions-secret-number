import random
import json
import datetime


def get_score_list():
    """ Función que lee el fichero de texto y regresa los valores de la lista"""
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    """Función que toma los valores de la lista de la función anterior y muestra 3 primeros"""
    score_list = get_score_list()
    top3_score_list = sorted(score_list, key=lambda x: x['attempts'])[:3]

    for score_dict in top3_score_list:
        score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".\
            format(score_dict.get("User name"), str(score_dict.get("attempts")), score_dict.get("date"),
            score_dict.get("secret_number"), score_dict.get("Unsuccessful guesses"))
        print(score_text)
        return top3_score_list


def play_game(difficulty="easy" or "hard"):
    """Función para jugar el juego"""
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    score_list = get_score_list()

    name = input("What's your name?: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1  # attempts = attempts + 1

        if guess == secret:
            current_time = str(datetime.datetime.now())
            score_data = {"User name": name, "secret_number": secret, "attempts": attempts,
                          "Unsuccessful guesses": wrong_guesses, "date": current_time}
            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                b = json.dumps(score_list)
                score_file.write(b)

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print(current_time)
            break
        elif guess > secret and difficulty == "easy":
            print("Your guess is not correct... try something smaller")
            wrong_guesses.append(guess)
        elif guess < secret and difficulty == "easy":
            print("Your guess is not correct... try something bigger")
            wrong_guesses.append(guess)
        elif guess != secret and difficulty == "hard":
            print("Wrong number. Game Over!")
            break


def main():
    """Ejecutar el juego"""
    while True:
        game_init = input("Would you like to: Play [A], See best scores [B], or Exit[C] ?")

        if game_init.upper() == "A":
            difficulty = input("Level [easy] or [hard]:")
            difficulty.lower()
            if difficulty == "easy":
                play_game("easy")
            elif difficulty == "hard":
                play_game("hard")
        elif game_init.upper() == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        else:
            break


if __name__ == "__main__":
    main()
