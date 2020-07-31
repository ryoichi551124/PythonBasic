def calc_income_tax(total_income):

    first_income = 10000
    next_income = 10000

    if total_income < 10000:
        first_income = total_income
        next_income = 0
    elif total_income < 20000:
        first_income = 10000
        next_income = total_income - 10000
    else:
        first_income = 10000
        next_income = 10000

    remain_income = total_income - first_income - next_income

    first_rate = 0
    next_rate = 10
    remain_rate = 20

    income_tax = first_income * 0 + next_income * next_rate + remain_income * remain_rate

    print(f'For example, suppose that the taxable income is ${total_income} the income tax payable is')
    print(f'${first_income}*{first_rate}% + ${next_income}*{next_rate}% + ${remain_income}*{remain_rate}% = ${income_tax}')


calc_income_tax(9000)
calc_income_tax(15000)
calc_income_tax(45000)
