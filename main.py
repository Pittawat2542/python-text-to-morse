from art import logo
from converter import Converter


def display_title():
    print(logo)
    print('Welcome to text-to-morse converter program.')
    print('Our program currently only support English alphanumeric without symbols and special characters.')
    print('NOTE: Any unavailable characters will convert to <OOV>.')
    print('---')


def display_menu() -> int:
    print("Please choose one menu (1, 2, 3):")
    print("1 Convert text to morse code")
    print("2 Show history")
    print("3 Exit program")
    try:
        menu = int(input("Choice: "))
        if menu < 1 or menu > 3:
            raise ValueError("Invalid choice.")

        return menu
    except ValueError:
        print("Invalid choice.")
        return display_menu()


if __name__ == '__main__':
    display_title()
    converter = Converter()
    choice = display_menu()
    while choice != 3:
        if choice == 1:
            converter.get_user_input()
            converter.convert()
            converter.display_converted_text()
        elif choice == 2:
            converter.display_history()
        choice = display_menu()
