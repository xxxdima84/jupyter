cars = 100 # переменная cars = 100
space_in_a_car = 4 # имеем 4 месста в авто
drivers = 30 # у нас 30 водителей
passengers = 90 # количество пассажиров = 90
cars_not_driven = cars-drivers # авто без водителей = авто - водители
cars_driven = drivers # авто с водителями = количеству водителей
carpool_capacity = cars_driven * space_in_a_car # вместимость автобазы = количество авто с водителями * мест в машине
average_passengers_per_car = passengers / cars_driven # среднее количество пассажиров на машину= количество пасажиров / количество водителей


print("В наличии", cars, "автомобилей.")
print("И только", drivers, "водителей вышли на работу")
print("Получается, что", cars_not_driven, "машин пустуют")
print("Мы можем перевести сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвести", passengers, "человек.")
print("В каждой машине будет примерно", average_passengers_per_car,"человека")

#average_passengers_per_car = car_pool_capacity / passenger - имя car_pool_capacity не определено