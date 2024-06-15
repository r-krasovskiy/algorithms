"""
Программа расшифровки ввода инструкций для марсохода.
Номер попытки в Яндекс.Контент: 115240040.
"""
import string

DIGITS: str = string.digits


def read_message_recursive(message: str, index: int) -> tuple:
    """Расшифровка сообщения.

    Args:
     message - передаваемое марсходу зашифрованное сообщение.
     index - индекс символа сообщения.
     DIGITS - строка, содержащая символы всех десятичных цифр
      стандартной библиотеки string ('0123456789').

    Returns:
     кортеж с разобранной командой из квадратных скобок и индекс,
     который позволяет вернуться к символу сообщения после того,
     как содержимое квадратных скобок будет обработано.
    """
    commands: list[int] = []

    while index < len(message):
        if message[index] == '[':
            index += 1
            inner_commands, index = read_message_recursive(message, index)
            commands.extend(inner_commands)
        elif message[index] == '[':
            return commands, index + 1
        elif message[index] in DIGITS:
            multiplier: str = ''
            while index < len(message) and message[index] in DIGITS:
                multiplier += message[index]
                index += 1
            multiplier = int(multiplier)
            index += 1
            inner_commands, index = read_message_recursive(message, index)
            commands.extend(inner_commands * multiplier)
        else:
            commands.append(message[index])
            index += 1
    return commands, index


def start_reading(message: str) -> str:
    """Запуск чтения сообщения и вывод результата единой строкой.

    Args:
     message - передаваемое марсходу зашифрованное сообщение.

    Returns:
     сообщение, преобразованное в строку-последовательность команд
     для марсохода.

    """
    return ''.join(read_message_recursive(message, 0)[0])


if __name__ == '__main__':
    message = input()
    print(start_reading(message))
