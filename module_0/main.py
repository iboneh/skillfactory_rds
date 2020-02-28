import numpy as np

def game_core(number):
    number = np.random.randint(1,100)
    count = 0
    range_min = 1
    range_max = 100
    while True:
        lenght_predict_range = range_max - range_min
        predict = range_min + lenght_predict_range // 2
        count += 1
#        print (number, count, predict)
        if number == predict:
            break
        if lenght_predict_range == 1:
            count += 1
            break
        elif number > predict:
            range_min = range_min + lenght_predict_range // 2
        elif number < predict:
            range_max = range_max - lenght_predict_range // 2
    return(count)

def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def score_game_2(game_core):
    count_num = []
    count_predeict = []
    np.random.seed(1)
    for i in range(1, 101):
        count_num.append(game_core(i))

    for i in range(min(count_num),max(count_num)):
        count_predeict.append(game_core(i))
        print(i, count_num.count(i))

    score = int(np.mean(count_2))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game_2(game_core)
