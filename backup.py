from distutils.dir_util import copy_tree
import os
import sys
import ctypes

d1 = sys.argv[1]
d2 = sys.argv[2]

def is_user_admin():
    try:
        is_admin = os.getuid() == 0

    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if is_admin == False:
        print("Você não tem permissão para executar este script!")
        exit()
    else:
        is_path()

def is_path():
    print("Executando como administrador...\n")
    if os.path.isdir(d1) == False or os.path.isdir(d2) == False:
        print("Diretórios não encontrados!!!")

    else:
        copy_files()

def copy_files():
    print("Diretórios localizados!")
    print(d1, d2)
    print("\n")
    copy_tree(d1, d2)
    print("Arquivos copiados!")
    print("Arquivos do diretório destino: ", os.listdir(d2))

is_user_admin()