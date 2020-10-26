#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare_files(fname1, fname2):
    with open(fname1) as f1, open(fname2) as f2:
        f1.seek(0, 2)
        f2.seek(0, 2)
        print(f1.tell(), f2.tell())
        f1.seek(0)
        f2.seek(0)
        c = f1.read(1)
        k = f2.read(1)
        while c != '' and k != '':
            if c != k:
                position = f1.tell()
                print(f'la difference entre les deux est {c} et {k} a la position {position}')
                break
            c = f1.read(1)
            k = f2.read(1)


def nombre(fname):
    with open(fname) as f:
        donnees = f.read()
    listNumb = sorted([int(mot) for mot in donnees.split() if mot.isdigit()])
    return listNumb




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #compare_files('exemple.txt', 'exemple2.txt')

    print(nombre('exemple.txt'))
    pass
