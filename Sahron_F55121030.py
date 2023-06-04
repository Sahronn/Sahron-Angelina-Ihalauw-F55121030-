import time


def bubble_sort_slow(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - 1):
            time.sleep(0.1)  # Memberikan jeda 0.1 detik pada setiap perbandingan
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


# Mengambil input dari pengguna
numbers = input("Masukkan beberapa angka yang akan diurutkan (pisahkan dengan spasi): ")
numbers = list(map(int, numbers.split()))

# Memanggil fungsi bubble_sort_slow dan mencetak hasilnya
sorted_numbers, execution_time = bubble_sort_slow(numbers)
print("Angka yang diurutkan:", sorted_numbers)
print("Waktu eksekusi:", execution_time, "detik")
