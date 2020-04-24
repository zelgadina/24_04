amount_of_words = input(" Сколько слов в словаре")
aow = int(amount_of_words)
slovar = {}


for i in range(aow):
    key = input("Ведите слово на английском\n: ").strip().lower()
    value = input("Ведите перевод\n: ").strip().lower()
    slovar[key] = value

for key in slovar.keys():
    print("Ввeдите перевод слова",  key, ": ")
    answer = input(": ").strip().lower()
    if slovar[key] == answer:
        print("Лев сыт")
    else:
        print(slovar[key], "- правильный ответ")