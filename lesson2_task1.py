# Задание 1
# Объявите числовую переменную, содержащую в себе день недели.
# В зависимости от значения этой переменной выведите строку с именем дня недели.
# Учтите в этом задании все дни недели.
# Заведите вторую переменную содержащую в себе время.
# Для среды, в зависимости от второй переменной со временем, выведите текст "a.m." (< 12 часов дня) или "p.m." (>= 12 часов дня).
# Напишите комментарий с пояснением о том, что делает текущая программа.

time = 13
	
week_day = 3
if week_day == 1:
    print("monday")
elif week_day == 2:
    print("tuesday")
elif week_day == 3:
    if time < 12:
        print("wednesday, a.m.")
    else:
        print("wednesday, p.m.")
elif week_day == 4:
    print("thursday")
elif week_day == 5:
    print("friday")
elif week_day == 6:
    print("saturday")
else: 
    print("sunday")



# I didn't understand the task, but I tried.
