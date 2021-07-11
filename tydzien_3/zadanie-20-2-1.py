def total_cost(time_hours: float, kwh: float, price_kwh: float = 0.617):

    return (kwh * price_kwh * time_hours)

print(total_cost(4,0.5))


