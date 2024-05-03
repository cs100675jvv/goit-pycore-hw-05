from summ import sum_profit
from floats import generator_floats





def main():

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_floats)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()

