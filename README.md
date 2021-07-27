# backup-script
Script de backup de arquivos desenvolvido como atividade prática no curso.

# Como o projeto funciona?
O script só roda se for executado como administrador e os diretórios devem ser passados como parâmetros no terminal (ex: python backup.py diretorio1 diretorio2)
Utilizando a biblioteca "os" e "ctypes" é possível identificar o usuário executando o script e com a biblioteca "sys" é possível identificar os diretórios passados no terminal.
Para a manipulação de arquivos foi usada a função "copy_tree" da biblioteca "disutils".
