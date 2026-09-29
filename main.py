import numpy as np

arr = np.array([[1.125, 0.125, 0.125, 0.125],
                  [1.0, 1.125, 0.125, 0.125],
                  [-0.125, 1.0, 1.125, 0.125],
                  [-0.125, -0.125, 1.0, 1.125],
                  [-0.125, -0.125, -0.125, 1.0]])

print(f"{'B1':>7} {'B2':>7} {'B3':>7} {'B4':>7}")
for row in arr:
    for num in row:
        print(f"{num:7.3f}", end=" ")
    print()

i=1
B_arr = np.array([])
A_arr = np.array([])
jmas = np.array([])
imas = np.array([])
print(f"||{'k':>3} ||{'i':>3} ||{'B1':>7} |{'B2':>7} |{'B3':>7} |{'B4':>7} ||{'j':>3} ||{'A1':>7} "
      f"|{'A2':>7} |{'A3':>7} |{'A4':>7} |{'A5':>7} ||{'V_':>7} |{'V^':>7} ||{'V*':>7} ||")
for k in range(1, 10001):
    B_arr = arr[i] if B_arr.size == 0 else B_arr + arr[i]
    j = B_arr.argmin()
    jmas = np.append(jmas, j)
    V_ = B_arr.min()/k
    A_arr = arr[:,j] if A_arr.size == 0 else A_arr + arr[:,j]
    V1 = A_arr.max() / k
    VV = (V_ + V1) / 2
    imas = np.append(imas, i)
    print(f"||{k:>3} ||{i+1:>3} ||{B_arr[0]:>7.3f} |{B_arr[1]:>7.3f} |{B_arr[2]:>7.3f} |{B_arr[3]:>7.3f} ||{j+1:>3} ||{A_arr[0]:>7.3f} "
          f"|{A_arr[1]:>7.3f} |{A_arr[2]:>7.3f} |{A_arr[3]:>7.3f} |{A_arr[4]:>7.3f} ||{V_:>7.3f} |{V1:>7.3f} ||{VV:>7.5f} ||")
    i = A_arr.argmax()

unique_values, counts = np.unique(imas, return_counts=True)
print(f"\nНомер p: {unique_values+1}")
print(f"N: {counts}")
print(f"p: {counts/k}")


unique_values, counts = np.unique(jmas, return_counts=True)
print(f"\nНомер q: {unique_values+1}")
print(f"N: {counts}")
print(f"N: {counts/k}")

