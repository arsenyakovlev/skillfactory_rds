import math
import numpy as np
def game_core_v5(number):
    a=1
    b=100+1 
    count = 0
    predict = int((a+b-1)/2)
    while number != predict:
        count+=1
        if count>100: 
            #print("num="+str(number)+" a="+str(a)+" b="+str(b)+" predict="+str(predict)+" ^Break >100")
            break;
        if number > predict: 
            a=predict
        elif number < predict: 
            b=predict
        if b>a:    
            predict = int((a+b)/2)
        else:
            predict = a
    #print("num="+str(number)+" predict="+str(predict)+" Count= "+str(count))  
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core_v5):
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v5(number))
    score = int(np.mean(count_ls))
    print(f"Мой алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v5)