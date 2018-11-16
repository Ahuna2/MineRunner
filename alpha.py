import sys
from random import *

import pygame
from pygame.locals import *


def game_over():
    return ('Miin!!!')


def maara_miinid():  # koostab randomilt sõnastiku, kus 1 tähistab miini ja 0 miini puudumist.

    valjund = {}
    miinide_list = sample(range(RUUTUDE_VEERGE * RUUTUDE_RIDU - 1), int(RUUTUDE_VEERGE * RUUTUDE_RIDU / 100 * PROTSENT_MIINE))
    for el in range(RUUTUDE_VEERGE * RUUTUDE_RIDU):
        valjund[el] = 0
    for i in miinide_list:
        valjund[i] = 1
    return valjund


def miinide_maatriks(sonastik):

    seis = []

    for i in range(RUUTUDE_RIDU):
        rida = []
        for j in range(RUUTUDE_VEERGE):
            rida.append(sonastik[j])
        seis.append(rida)
    
    return seis


def safe_zone():

    for ruut in valjak:
        if ruut in vasakpoolsed_ruudud or ruut in parempoolsed_ruudud:
            valjak[ruut] = 23


def miinide_arv(sisend):  # tagastab, mitu miini ümbritseb antud ruutu

    ulemised_ruudud = []
    for i in range(RUUTUDE_VEERGE):
        ulemised_ruudud.append(i)

    alumised_ruudud = []
    for i in range(RUUTUDE_VEERGE):
        alumised_ruudud.append(RUUTUDE_VEERGE * RUUTUDE_RIDU - 1 - i)

    if sisend in vasakpoolsed_ruudud and sisend in ulemised_ruudud:
        miinide_arv = valjak[sisend + 1] + valjak[sisend + RUUTUDE_VEERGE] + valjak[sisend + RUUTUDE_VEERGE + 1]

    elif sisend in parempoolsed_ruudud and sisend in ulemised_ruudud:
        miinide_arv = valjak[sisend - 1] + valjak[sisend + RUUTUDE_VEERGE - 1] + valjak[sisend + RUUTUDE_VEERGE]

    elif sisend in vasakpoolsed_ruudud and sisend in alumised_ruudud:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE] + valjak[sisend - RUUTUDE_VEERGE + 1] + valjak[sisend + 1]

    elif sisend in parempoolsed_ruudud and sisend in alumised_ruudud:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE - 1] + valjak[sisend - RUUTUDE_VEERGE] + valjak[sisend - 1]

    elif sisend in vasakpoolsed_ruudud:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE] + valjak[sisend - RUUTUDE_VEERGE + 1] + valjak[sisend + 1] + valjak[
            sisend + RUUTUDE_VEERGE] + valjak[sisend + RUUTUDE_VEERGE + 1]

    elif sisend in parempoolsed_ruudud:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE] + valjak[sisend - RUUTUDE_VEERGE - 1] + valjak[sisend - 1] + valjak[
            sisend + RUUTUDE_VEERGE] + valjak[sisend + RUUTUDE_VEERGE - 1]

    elif sisend in ulemised_ruudud:
        miinide_arv = valjak[sisend - 1] + valjak[sisend + 1] + valjak[sisend + RUUTUDE_VEERGE - 1] + valjak[
            sisend + RUUTUDE_VEERGE] + valjak[sisend + RUUTUDE_VEERGE + 1]

    elif sisend in alumised_ruudud:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE - 1] + valjak[sisend - RUUTUDE_VEERGE] + valjak[
            sisend - RUUTUDE_VEERGE + 1] + valjak[sisend - 1] + valjak[sisend + 1]

    else:
        miinide_arv = valjak[sisend - RUUTUDE_VEERGE - 1] + valjak[sisend - RUUTUDE_VEERGE] + valjak[
            sisend - RUUTUDE_VEERGE + 1] + valjak[sisend - 1] + valjak[sisend + 1] + valjak[sisend + RUUTUDE_VEERGE - 1] + \
                      valjak[sisend + RUUTUDE_VEERGE] + valjak[sisend + RUUTUDE_VEERGE + 1]

    return miinide_arv


def klikk(x, y):  # tagastab hulga elemendi, mille peale vajutati
    if x > 10 and x < (RUUTUDE_VEERGE * 20 + 10):
        x_asukoht = int((x - 10) / 20)

    elif x < 10 or x > (RUUTUDE_VEERGE * 20 + 10):
        return None

    if y > 10 and y < (RUUTUDE_RIDU * 20 + 10):
        y_asukoht = int((y - 10) / 20)

    elif y < 10 or y > (RUUTUDE_VEERGE * 20 + 10):
        return None

    valjund = y_asukoht * RUUTUDE_VEERGE + x_asukoht
    return valjund


def kliki_tagajarg(sisend):     # klikk avab ühe ruudu, see otsustab, kas ta astus miini otsa või tagastada kuvamiseks ümbritsevate miinide arv
    if sisend == None:
        return ('Väljaspool piiri')
    if valjak[sisend] == 1:
        return game_over()
    else:
        return miinide_arv(sisend)


# Põhifunktsioon
def main():

    global valjak, maatriks, vasakpoolsed_ruudud, parempoolsed_ruudud

    pygame.init()

    # Teeb akna valmis
    aken = pygame.display.set_mode((akna_laius, akna_korgus))
    pygame.display.set_caption('Minesweeper Vol. 2')

    # Laeb pildid sisse
    ruut = pygame.image.load('ruut.jpg').convert()
    avatud_ruut = pygame.image.load('avatud_ruut.jpg').convert()
    safe_ruut = pygame.image.load('safe_ruut.jpg').convert()
    uks = pygame.image.load('1.jpg').convert()
    kaks = pygame.image.load('2.jpg').convert()
    kolm = pygame.image.load('3.jpg').convert()
    neli = pygame.image.load('4.jpg').convert()
    viis = pygame.image.load('5.jpg').convert()
    kuus = pygame.image.load('6.jpg').convert()
    seitse = pygame.image.load('7.jpg').convert()
    kaheksa = pygame.image.load('8.jpg').convert()
    miin = pygame.image.load('miin.jpg').convert()
    lipp = pygame.image.load('lipp.jpg').convert()

    # Seab kindla numbri pildiga vastavusse
    pildi_id = {1:ruut, 0:ruut, 11: uks, 12:kaks, 13:kolm,
                14:neli, 15:viis, 16:kuus, 17:seitse, 18:kaheksa,
                10:avatud_ruut, 21:miin, 22:lipp, 23:safe_ruut}

    # Tsükkel, mis täidab akna avamata ruutudega
    for ruudu_y in range(SERVA_PAKSUS, RUUDU_PIKKUS * RUUTUDE_RIDU, RUUDU_PIKKUS):
        for ruudu_x in range(SERVA_PAKSUS, RUUDU_LAIUS * RUUTUDE_VEERGE, RUUDU_LAIUS):
            aken.blit(ruut, (ruudu_x, ruudu_y))

    # Mänguvälja loomine
    valjak = maara_miinid()
    
    # Safe zone loomine
    vasakpoolsed_ruudud = []
    for i in range(RUUTUDE_RIDU):
        vasakpoolsed_ruudud.append(i * RUUTUDE_VEERGE)

    # Maatriks mille järgi joonistatakse mängu seis
    maatriks = miinide_maatriks(valjak)

    parempoolsed_ruudud = []
    for i in range(RUUTUDE_RIDU):
        parempoolsed_ruudud.append(i * RUUTUDE_VEERGE + (RUUTUDE_VEERGE - 1))

    # Põhitsükkel
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()
        
        rida = 0

        # Tsükkel, mis joonistab pildi maatriksi põhjal
        for ruudu_y in range(SERVA_PAKSUS, RUUDU_PIKKUS * RUUTUDE_RIDU, RUUDU_PIKKUS):
            
            id = 0

            for ruudu_x in range(SERVA_PAKSUS, RUUDU_LAIUS * RUUTUDE_VEERGE, RUUDU_LAIUS):

                    pilt = pildi_id[maatriks[rida][id]]
                    aken.blit(pilt, (ruudu_x, ruudu_y))
                    # Kui on miini klikitud, siis joonistab selle ja paneb mängu kinni
                    if pilt == miin:
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        sys.exit()
                    id += 1
            
            rida += 1

        # TODO ruut highlighitud kui hiir selle peal on

        # Vasak hiireklõps
        if pygame.mouse.get_pressed()[0] == 1:
            # Hiire koordinaadid
            hiire_pos = pygame.mouse.get_pos()
            peale_vajutatud_element = klikk(hiire_pos[0], hiire_pos[1])
            if peale_vajutatud_element == None:
                continue
            else:
                ava_ruut = kliki_tagajarg(peale_vajutatud_element)
                if ava_ruut == 'Väljaspool piiri':
                    continue
                elif ava_ruut == 'Miin!!!':
                    print('Mäng läbi!')
                    rea_nr = peale_vajutatud_element // RUUTUDE_VEERGE
                    elemendi_nr = peale_vajutatud_element % RUUTUDE_VEERGE
                    maatriks[rea_nr][elemendi_nr] = 21
                    # TODO avab kõik ruudud
                else:
                    rea_nr = peale_vajutatud_element // RUUTUDE_VEERGE
                    elemendi_nr = peale_vajutatud_element % RUUTUDE_VEERGE
                    maatriks[rea_nr][elemendi_nr] = 10 + ava_ruut
        
        # Parem hiireklõps
        if pygame.mouse.get_pressed()[2] == 1:
            # Hiire koordinaadid
            hiire_pos = pygame.mouse.get_pos()
            peale_vajutatud_element = klikk(hiire_pos[0], hiire_pos[1])
            if peale_vajutatud_element == None:
                continue
            else:
                rea_nr = peale_vajutatud_element // RUUTUDE_VEERGE
                elemendi_nr = peale_vajutatud_element % RUUTUDE_VEERGE
                maatriks[rea_nr][elemendi_nr] = 22
        
        # Uuendab pilti
        pygame.display.flip()

        # 60 fps
        kell.tick(FPS)





# Ühe ruudukese suurus pikslites
RUUDU_LAIUS = 20
RUUDU_PIKKUS = 20
# TODO ruudu suurus pildi järgi

# Mitu ruutu väljal on
RUUTUDE_VEERGE = 60
RUUTUDE_RIDU = 15
# TODO muudetav arv ruute

# Akna ääre paksus pikslites
SERVA_PAKSUS = 10

# Arvutab akna suuruse
akna_laius = RUUDU_LAIUS * RUUTUDE_VEERGE + 2 * SERVA_PAKSUS
akna_korgus = RUUDU_PIKKUS * RUUTUDE_RIDU + 2 * SERVA_PAKSUS

# Mitu protsenti ruutudest on miinid
PROTSENT_MIINE = 20

# Loob kella fps-i jaoks
kell = pygame.time.Clock()

FPS = 60



# valjak = maara_miinid()
# safe_zone()
# print(valjak)
# miine_kokku = 0
# for el in valjak:
#     if valjak[el] == 1:
#         miine_kokku += 1

# # Debugimine kindlatel kliki koordinaatidel
# k = klikk(500, 160)
# print('miine kokku = ' + str(miine_kokku))
# print('elemendi number = ' + str(k))
# print(str(kliki_tagajarg(k)) + ' miini on selle ümber')





main()