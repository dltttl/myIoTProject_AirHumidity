# myIoTProject_AirHumidity

# Идея
Устройство, которое будет измерять влажность воздуха в режиме реального времении

# Как запустить
для работы подключаем ардуинку с датчиком влажности через usb, загружаем на нее приложенный скетч(или сразу прошивку - .hex файл), запускаем сервер (web/main.py), предварительно вписав к коде правильный порт. Наслаждаемся!

# Примечание
при симуляции вместо датчика влажности DHT11 использован потенциометр.
____
в репозитории дополнительно есть макет для симуляции в simulide (arduino/simulide/test1.simu)
____
Макет в тинкеркаде: https://www.tinkercad.com/things/9yJcDLS4WNG-airhumidityproject - 

в нем дополнительно установлен RGB -светодиод для индикации приемлемости уровня влажности воздуха
