def fibonacci(n):
    if n <= 0:
        return "Geçersiz giriş"
    else == 1 or n == 2:
        return 1
    else:
        fib_sequence = [1, 1]  # Fibonacci dizisinin ilk iki elemanı
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[-1]

numara = int(input("Fibonacci sayısı için bir sıra numarası girin: "))




"""
Hesap 
"""
fib = fibonacci(numara)



"""
Sonuç 
"""
print("Fibonacci dizisinin", numara, ". elemanı:", fib)
