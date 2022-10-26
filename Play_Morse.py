from random import choice

# инициализация переменных и функций
words = ["code", "bit", "list", "soul", "next"]
answers = []

morse_alphabet = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}


def morse_encode(word):
  """Шифрует слово в морзянку"""
  
  encrypted_word = ""
  for letter_word in range(0, len(word)):
    encrypted_word += morse_alphabet[word[letter_word]] + " "

  return encrypted_word 


def get_word():
  """Достает случайное слово из предлагаемых"""
  return choice(words) 


def print_statistics(answers):
  """Выводит статистику ответов"""

  total = len(answers)
  right = 0
  wrong = 0
  for answer in answers:
    if answer == True:
      right += 1
    elif answer == False:
      wrong += 1

  print(f"Всего задачек: {total}\nОтвечено верно: {right}\nОтвечено неверно: {wrong}")


# начало программы
start = input("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем")


for trying in range(0,5):
  random_word = get_word()
  encrypted_random_word = morse_encode(random_word)
  print(f"Слово {trying+1} - {encrypted_random_word}")

  user_answer = input()

  if user_answer.lower() == random_word:
    answers.append(True)
    print(f"Верно, {random_word}!\n")
  else:
    answers.append(False)
    print(f"Неверно, {random_word}!\n")

print_statistics(answers)