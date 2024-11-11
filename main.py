# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
# # Пример использования функции
# n = int(input("Введите число для вычисления факториала: "))
# print("Факториал числа", n, "равен", factorial(n))

#  первые 20 простых чисел

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num//2):
#         if (num % i) == 0:
#             return False
#     return True
#
# primes = []
# for num in range(2):
#     if is_prime(num):
#         primes.append(num)
#
# print("Первые 20 простых чисел:")
# for prime in primes:
#     print(prime)


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# count = 0
# num = 2
# while count < 20:
#     if is_prime(num):
#         print(num)
#         count += 1
#     num += 1

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num//2):
#         if (num % i) == 0:
#             return False
#     return True
#
# primes = []
# for num in range(2, 21):
#     if is_prime(num):
#         primes.append(num)
#
# print("Первые 20 простых чисел:")
# for prime in primes:
#     print(prime)



# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# count = 0
# num = 2
# while count < 20:
#     if is_prime(num):
#         print(num)
#         count += 1
#     num += 1
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def first_n_primes(n):
#     primes = []
#     num = 2  # Начинаем проверку с 2, так как это первое простое число
#     while len(primes) < n:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes
#
# # Вывод первых 20 простых чисел
# first_20_primes = first_n_primes(20)
# print("Первые 20 простых чисел:", first_20_primes)

# def longest_common_prefix(words):
#     if not words:
#         return ""
#
#     # Начинаем с первого слова в массиве в качестве префикса
#     prefix = words[0]
#
#     for word in words[1:]:
#         # Сравниваем префикс с каждым словом и обрезаем его, если необходимо
#         while word[:len(prefix)] != prefix:
#             prefix = prefix[:-1]  # Убираем последний символ из префикса
#             if not prefix:
#                 return ""  # Если префикс стал пустым, возвращаем пустую строку
#
#     return prefix
#
#
# # Пример использования
# words = ["flower", "flow", "flight"]
# result = longest_common_prefix(words)
# print("Максимально длинное общее начало:", result)

def find_longest_common_prefix(words):
    if not words:
        return ''
    prefix = words[0]
    for word in words[1:]:
        i = 0
        while i < len(prefix) and i < len(word):
            if prefix[i] != word[i]:
                break
            i += 1
        prefix = prefix[:i]
    return prefix

words = ["apple", "apricot", "apology"]
longest_prefix = find_longest_common_prefix(words)
print(longest_prefix)  # Output: "ap"