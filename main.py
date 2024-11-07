import decimal
import time

def calculate_pi(digits):
    decimal.getcontext().prec = digits + 5
    
    C = 426880 * decimal.Decimal(10005).sqrt()
    M = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    X = decimal.Decimal(1)
    K = decimal.Decimal(6)
    S = L
    for i in range(1, digits):
        M = (K**3 - 16*K) * M / (i**3)
        L += 545140134
        X *= -640320
        S += M * L / X
        K += 12
        if abs(M * L / X) < 1e-10:
            break
    
    pi_value = C / S
    return pi_value

def main():
    digits = int(input("Enter the number of digits of Pi to calculate: "))
    max_digits = 100000000
    if digits > max_digits:
        print(f"Calculating Pi to {max_digits} digits. Please reduce the number of digits.")
        digits = max_digits

    start_time = time.time()
    pi_value = calculate_pi(digits)
    end_time = time.time()

    print(f"Pi to {digits} decimal places: {str(pi_value)[:digits+2]}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    save_to_file = input("Do you want to save the digits to a file? [Y/n]: ").strip().lower()

    if save_to_file == '' or save_to_file == 'y':
        filename = input("Enter the filename (without extension): ").strip()
        
        with open(f"{filename}.txt", "w") as file:
            file.write(f"Pi to {digits} decimal places:\n")
            file.write(str(pi_value)[:digits+2])
        
        print(f"Pi to {digits} digits has been saved to {filename}.txt")
    else:
        print("The digits were not saved to a file.")

if __name__ == "__main__":
    main()
