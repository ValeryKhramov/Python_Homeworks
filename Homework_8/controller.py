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
                index = view.get_info(txt.text_change_contact)
                if fun.check_contact(index)[0]:
                    fun.change_contact(view.new_contact(), fun.check_contact(index)[1])
                    view.print_info(txt.change_contact_successful)
                else:
                    view.print_info(txt.error_index)
            case 7:
                index = view.get_info(txt.text_delete_contact)
                if fun.check_contact(index)[0]:
                    fun.delete_contact(fun.check_contact(index)[1])
                    view.print_info(txt.delete_contact_successful)
                else:
                    view.print_info(txt.error_index)
            case 8:
                if fun.exit_phone_book():
                    if view.confirm(txt.is_changed):
                        fun.save_file()
                        view.print_info(txt.save_successful)
                view.print_info(txt.bye_bye)
                exit()
