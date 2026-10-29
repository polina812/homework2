sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}

def total(sales, day):
    total_now= 0
    for name, price, qty in sales[day]:
        total_now += price * qty
    return total_now

def best(sales, day):
    best_now = ""
    cnt_now = 0
    for name, price, qty in sales[day]:
        if qty > cnt_now:
            cnt_now = qty
            best_now = name
    return f"Хит {day}: {best_now}"

for day in sales:
    print(f"{day}: выручка {total(sales, day)}")
    print(best(sales, day))


# 2 часть
itog = 0
max_day = ""
max_vr = 0

for day in sales:
    cr_vr = 0
    now = total(sales, day)
    itog += now
    if now > max_vr: 
        max_day = day
        max_vr = now
    al = 0
    for name, price, qty in sales[day]:
        al += qty
    cr_vr = now / al
    print(f"Cредняя выручка за {day}: {round(cr_vr)}")
print(f"Итоговая выручка за неделю: {itog}, день с максимальной выручкой: {max_day}")


