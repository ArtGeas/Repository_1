words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

answers = {}
count_right_answers = 0
words = {}

# Начало 
print("Выберите уровень сложности.")
dif_level = input("Легкий, средний, сложный. \n")

# Выбор сложности 
if dif_level.lower() == "легкий":
    words = words_easy
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод.")
elif dif_level.lower() == "средний":
    words = words_medium
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод.") 
elif dif_level.lower() == "сложный":
    words = words_hard
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод.") 
else:
    words = words_easy
    print("Раз вы не смогли самостоятельно ввести уровень сложности. Начнем с легкого. :)")

# Выполнение задания
for eng, rus in words.items():
    start_round = input("Нажмите Enter")
    input_answer = input(f"{eng}, {len(rus)} букв, начинается на {rus[0]}...\n")
    if input_answer == rus:
        print(f"Верно, {eng} - это {rus}.")
        answers[eng] = True
    else:
        print(f"Неверно, {eng} - это {rus}.")
        answers[eng] = False

# Подсчет результатов
print("Правильно отвечены слова:")
for word, answer in answers.items():
    if answer == True:
        print(word)
        count_right_answers += 1
print("Неправильно отвечены слова:")
for word, answer in answers.items():
    if answer == False:
        print(word)

print(f"Ваш ранг: \n{levels[count_right_answers]}")