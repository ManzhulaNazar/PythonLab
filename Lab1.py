def are_anagrams(word1, word2):
    # Видаляємо всі пробіли з обох слів і перетворюємо їх на нижній регістр
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Сортуємо літери в обох словах і порівнюємо отримані рядки
    return sorted(word1) == sorted(word2)

# Запитуємо користувача на введення двох слів
word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

# Визначаємо, чи є слова анаграмами і виводимо результат
if are_anagrams(word1, word2):
    print(f"{word1} і {word2} - це анаграми.")
else:
    print(f"{word1} і {word2} - це не анаграми.")
