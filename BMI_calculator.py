def calculate_bmi(height, weight):
    bmi = weight / height**2
    return bmi
def interprete_bmi(bmi):
    if bmi <18.5:
        return "Under-weighted"
    elif 18.5 <= bmi < 30:
        return "Normal weighted"
    elif 30 <= bmi < 45:
        return "Over-weighted"
    else:
        return "Obese"
def main():
    weight = float(input("Inter your weight in kilogram: "))
    height = float(input("Inter your height in meter: "))
    bmi = calculate_bmi(height, weight)
    interpretation = interprete_bmi(bmi)
    print(f"If your bmi is {bmi:.2f}, which is considered as {interpretation}")

if __name__ == "__main__":
    main()
