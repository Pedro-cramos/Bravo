#-*- coding: utf-8 -*-
# patricia.bravo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Um aplicativo demo de web para ensinar programação para crianças.

.. codeauthor:: Pedro Carvalho Ramos <pedro300501@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

'''from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

balao = "https://i.pinimg.com/236x/d2/dd/c4/d2ddc45b2599d5fc60f03ec81c53bb6c.jpg"
balao2 = "https://i.pinimg.com/236x/14/3a/14/143a14c4535873de51301549ba96e051.jpg"
fundo = "https://i.pinimg.com/originals/ca/a8/25/caa8256ded30c7703fadf79651d7833b.jpg"

STYLE["width"] , STYLE["height"] = 1200, "600px"

def teste():
    x = 0
    cena = Cena(img = fundo)
    cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"))
    elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"))
    txt1 = Texto(cena,"Vamos aprender a programar?")
    txt2 = Texto(cena,"Escolha entre cenas ou elementos para começar.")
    #txt1.vai=txt2.vai
    cena.vai()
    cenas.entra(cena)
    elementos.entra(cena)
    if x == 0:
        txt1.vai()
        print("1")
        x = 1
    if x == 1:
        txt2.vai()
        print("2")

teste()'''
class Main:
    #classe exemplo
    def __init__(self, versao):
        print("classe exemplo", format(versao))

if __name__ == "__main__":
    Main(1)