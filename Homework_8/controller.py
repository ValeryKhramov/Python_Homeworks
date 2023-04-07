import view
import function_module as fun
import text_module_ru as txt


def start_phone_book():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                fun.load_file()
                view.print_info(txt.load_successful)
            case 2:
                fun.save_file()
                view.print_info(txt.save_successful)
            case 3:
                phone_book = fun.get_phone_book()
                view.show_contact(phone_book, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                fun.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                info_contact = view.get_info(txt.find_contact)
                view.show_contact(fun.find_contact(info_contact), txt.no_find_contact)
            case 6:
                pass
            case 7:
                pass
            case 8:
                if fun.exit_phone_book():
                    if view.confirm(txt.is_changed):
                        fun.save_file()
                        view.print_info(txt.save_successful)
                view.print_info(txt.bye_bye)
                exit()
