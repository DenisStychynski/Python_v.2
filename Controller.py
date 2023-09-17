

import Function as d
import faulthandler
import Trait


def run():
    input_from_user = ''
    while input_from_user != '7':
        Trait.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            d.show('all')
        if input_from_user == '2':
            d.add()
        if input_from_user == '3':
            d.show('all')
            d.id_edit_del_show('del')
        if input_from_user == '4':
            d.show('all')
            d.id_edit_del_show('edit')
        if input_from_user == '5':
            d.show('date')
        if input_from_user == '6':
           d.show('id')
           d.id_edit_del_show('show')
        if input_from_user == '7':
            Trait.goodbuy()
            break