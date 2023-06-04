import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


# Mengambil input dari pengguna
numbers = input("Masukkan beberapa angka yang akan diurutkan (pisahkan dengan spasi): ")
numbers = list(map(int, numbers.split()))

# Memanggil fungsi bubble_sort dan mencetak hasilnya
sorted_numbers, execution_time = bubble_sort(numbers)
print("Angka yang diurutkan:", sorted_numbers)
print("Waktu eksekusi:", execution_time, "detik")