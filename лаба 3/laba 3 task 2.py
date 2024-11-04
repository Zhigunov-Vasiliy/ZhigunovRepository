# TODO Напишите функцию find_common_participants
def find_common_participants(f, s, argument = ','):
    first = f.split(argument)
    first = set(first)
    second = s.split(argument)
    second = set(second)
    print (first.intersection(second))
    return first.intersection(second)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, argument='|')