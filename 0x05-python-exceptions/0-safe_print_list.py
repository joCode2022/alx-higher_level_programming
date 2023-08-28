#!/usr/bin/python3

def safe_print_list(m_list=[], x=0):
    idx = 0

    try:
        for i in m_list:
            if idx < x:
                print('{}'.format(m_list[idx]), end='')
                idx += 1

        print()
    except TypeError:
        pass
    finally:
        return idx
