import sys
from random import *

import pygame
from pygame.locals import *


# Koostab randomilt sõnastiku, kus 1 tähistab miini ja 0 miini puudumist
def maara_miinid():

    valjund = {}
    miinide_list = sample(range(RUUTUDE_VEERGE * RUUTUDE_RIDU - 1), int(RUUTUDE_VEERGE * RUUTUDE_RIDU / 100 * PROTSENT_MIINE))
    for el in range(RUUTUDE_VEERGE * RUUTUDE_RIDU):
        valjund[el] = 0
    for i in miinide_list:
        valjund[i] = 1
    return valjund


def kaardista_miinid():
    
    valjund = {}
    for i in valjak.keys():
        valjund[i] = miinide_arv(i)
    return valjund


# Koostab sõnastiku, mida mäng uuendab, et kontrollida kas kõrvalt on midagi avatud
def kas_umbritsev(vasakpoolsed_ruudud):
    
    valjund = {}
    for el in range(RUUTUDE_VEERGE * RUUTUDE_RIDU):
        valjund[el] = 0
    for el in vasakpoolsed_ruudud:
        valjund[el] = 1
    return valjund


def jah_umbritsev(sisend, kas_umbritseb):
    
    try:
        kas_umbritseb[sisend - RUUTUDE_VEERGE] = 1
    except:
        pass
    try:
        kas_umbritseb[sisend + RUUTUDE_VEERGE] = 1
    except:
        pass
        
    if sisend not in vasakpoolsed_ruudud:
        kas_umbritseb[sisend - 1] = 1
        try:
            kas_umbritseb[sisend - RUUTUDE_VEERGE - 1] = 1
        except:
            pass
        try:
            kas_umbritseb[sisend + RUUTUDE_VEERGE - 1] = 1
        except:
            pass
            
    if sisend not in parempoolsed_ruudud:
        kas_umbritseb[sisend + 1] = 1
        try:
            kas_umbritseb[sisend - RUUTUDE_VEERGE + 1] = 1
        except:
            pass
        try:
            kas_umbritseb[sisend + RUUTUDE_VEERGE + 1] = 1
        except:
            pass


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
            valjak[ruut] = 0
    
    # Joonistab rohelised ruudud
    for i in range(len(maatriks)):
        for j in range(0, len(maatriks[i]), RUUTUDE_VEERGE - 1):
            maatriks[i][j] = 24


def miinide_arv(sisend):
    
    miinide_arv = 0
    
    try:
        miinide_arv += valjak[sisend - RUUTUDE_VEERGE]
    except:
        pass
    try:
        miinide_arv += valjak[sisend + RUUTUDE_VEERGE]
    except:
        pass
        
    if sisend not in vasakpoolsed_ruudud:
        miinide_arv += valjak[sisend - 1]
        try:
            miinide_arv += valjak[sisend - RUUTUDE_VEERGE - 1]
        except:
            pass
        try:
            miinide_arv += valjak[sisend + RUUTUDE_VEERGE - 1]
        except:
            pass
            
    if sisend not in parempoolsed_ruudud:
        miinide_arv += valjak[sisend + 1]
        try:
            miinide_arv += valjak[sisend - RUUTUDE_VEERGE + 1]
        except:
            pass
        try:
            miinide_arv += valjak[sisend + RUUTUDE_VEERGE + 1]
        except:
            pass

    if miinide_arv == None:
        miinide_arv = 0
    
    return miinide_arv

def ava_umbritsevad(sisend):
    
    try:
        if kaart[sisend - RUUTUDE_VEERGE] == 0:
            kliki_tagajarg(sisend - RUUTUDE_VEERGE)
    except:
        pass
    try:
        if kaart[sisend + RUUTUDE_VEERGE] == 0:
            kliki_tagajarg(sisend + RUUTUDE_VEERGE)
    except:
        pass
        
    if sisend not in vasakpoolsed_ruudud:
        if kaart[sisend - 1] == 0:
            kliki_tagajarg(sisend - 1)
        try:
            if kaart[sisend - RUUTUDE_VEERGE - 1] == 0:
                kliki_tagajarg(sisend - RUUTUDE_VEERGE - 1)
        except:
            pass
        try:
            if kaart[sisend + RUUTUDE_VEERGE - 1] == 0:
                kliki_tagajarg(sisend + RUUTUDE_VEERGE - 1)
        except:
            pass
            
    if sisend not in parempoolsed_ruudud:
        if kaart[sisend + 1] == 0:
            kliki_tagajarg(sisend + 1)
        try:
            if kaart[sisend - RUUTUDE_VEERGE + 1] == 0:
                kliki_tagajarg(sisend - RUUTUDE_VEERGE + 1)
        except:
            pass
        try:
            if kaart[sisend + RUUTUDE_VEERGE + 1] == 0:
                kliki_tagajarg(sisend + RUUTUDE_VEERGE + 1)
        except:
            pass


# Tagastab hulga elemendi, mille peale vajutati
def klikk(x, y):

    if x >= SERVA_PAKSUS and x <= (RUUTUDE_VEERGE * RUUDU_KULG + SERVA_PAKSUS):
        x_asukoht = int((x - SERVA_PAKSUS) / RUUDU_KULG)

    elif x < SERVA_PAKSUS or x > (SERVA_PAKSUS + RUUTUDE_VEERGE * RUUDU_KULG):
        return

    if y >= SERVA_PAKSUS and y <= (RUUTUDE_RIDU * RUUDU_KULG + SERVA_PAKSUS):
        y_asukoht = int((y - SERVA_PAKSUS) / RUUDU_KULG)

    elif y < SERVA_PAKSUS or y > (SERVA_PAKSUS + RUUTUDE_VEERGE * RUUDU_KULG):
        return

    valjund = y_asukoht * RUUTUDE_VEERGE + x_asukoht
    
    return valjund


# Klikk avab ühe ruudu, see otsustab, kas ta astus miini otsa või tagastada kuvamiseks ümbritsevate miinide arv
def kliki_tagajarg(sisend):

    if kas_umbritseb[sisend] == 1:
        if sisend in parempoolsed_ruudud:
            voidetud = True
        jah_umbritsev((peale_vajutatud_element), kas_umbritseb)
        if valjak[sisend] == 1:
            return 'Miini otsas!'
        else:
            valjund = miinide_arv(sisend)
##            if valjund == 0:
##                ava_umbritsevad(sisend)
            return valjund


def loo_pilt(aken, pildi_id, miin):
    
    # Tsükkel, mis joonistab pildi maatriksi põhjal
    rida = 0
    
    for ruudu_y in range(SERVA_PAKSUS, RUUDU_KULG * RUUTUDE_RIDU, RUUDU_KULG):
        
        id = 0

        for ruudu_x in range(SERVA_PAKSUS, RUUDU_KULG * RUUTUDE_VEERGE, RUUDU_KULG):

                pilt = pildi_id[maatriks[rida][id]]
                aken.blit(pilt, (ruudu_x, ruudu_y))
                # Kui on miini klikitud, siis joonistab selle
                if pilt == miin:
                    pygame.display.flip()
                    pygame.time.delay(2000)
                id += 1
        
        rida += 1

# Põhifunktsioon
def main():

    global valjak, maatriks, vasakpoolsed_ruudud, parempoolsed_ruudud, peale_vajutatud_element, kaart, kas_umbritseb, voidetud

    pygame.init()

    voidetud = False
    miini_otsa_astunud = False

    # Teeb akna valmis
    aken = pygame.display.set_mode((akna_laius, akna_korgus))
    pygame.display.set_caption('MineRunner')

    # Seab teksti fondi paika
    fondi_suurus = akna_laius // 6
    teksti_font = pygame.font.SysFont(None, fondi_suurus, bold=False)

    # Laeb pildid sisse
    ruut = pygame.image.load('ruut.png').convert()
    avatud_ruut = pygame.image.load('avatud_ruut.png').convert()
    safe_ruut = pygame.image.load('safe_ruut.png').convert()
    uks = pygame.image.load('1.png').convert()
    kaks = pygame.image.load('2.png').convert()
    kolm = pygame.image.load('3.png').convert()
    neli = pygame.image.load('4.png').convert()
    viis = pygame.image.load('5.png').convert()
    kuus = pygame.image.load('6.png').convert()
    seitse = pygame.image.load('7.png').convert()
    kaheksa = pygame.image.load('8.png').convert()
    miin = pygame.image.load('miin.png').convert()
    lipp = pygame.image.load('lipp.png').convert()

    # Seab kindla numbri pildiga vastavusse
    pildi_id = {1:ruut, 0:ruut, 11: uks, 12:kaks, 13:kolm,
                14:neli, 15:viis, 16:kuus, 17:seitse, 18:kaheksa,
                10:avatud_ruut, 21:miin, 22:lipp, 23:lipp, 24:safe_ruut}

    # Tsükkel, mis täidab akna avamata ruutudega
    for ruudu_y in range(SERVA_PAKSUS, RUUDU_KULG * RUUTUDE_RIDU, RUUDU_KULG):
        for ruudu_x in range(SERVA_PAKSUS, RUUDU_KULG * RUUTUDE_VEERGE, RUUDU_KULG):
            aken.blit(ruut, (ruudu_x, ruudu_y))

    # Mänguvälja loomine
    valjak = maara_miinid()
    
    # Safe zone'i ruutude loomine
    vasakpoolsed_ruudud = []
    for i in range(RUUTUDE_RIDU):
        vasakpoolsed_ruudud.append(i * RUUTUDE_VEERGE)

    parempoolsed_ruudud = []
    for i in range(RUUTUDE_RIDU):
        parempoolsed_ruudud.append(i * RUUTUDE_VEERGE + (RUUTUDE_VEERGE - 1))
        
    # Loob sõnastiku, mis salvestab, milliseid ruute saab avada
    kas_umbritseb = kas_umbritsev(vasakpoolsed_ruudud)
    kaart = kaardista_miinid()
        
    # Maatriks mille järgi joonistatakse mängu seis
    maatriks = miinide_maatriks(valjak)
    
    # Loob rohelised ruudud
    safe_zone()

    # Põhitsükkel
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                break
        elif event.type == pygame.QUIT:
            break

        # Joonistab pildi valmis
        loo_pilt(aken, pildi_id, miin)

        # Kontrollib kas on miini otsa astutud
        if miini_otsa_astunud:
            game_over_lava = teksti_font.render('GAME OVER!', False, (200, 50, 50), (100, 100, 100))
            aken.blit(game_over_lava, (akna_laius / 9, akna_korgus / 3))
            pygame.display.flip()
            pygame.time.delay(4000)
            break

        # Kui on jõutud teisele poole siis on mäng võidetud
        for rida in range(len(maatriks)):
            if maatriks[rida][RUUTUDE_VEERGE - 1] != 24:
                voidetud = True

        # Kontrollib kas mäng on võidetud
        if voidetud:
            print('Võitsid!')
            voidetud_lava = teksti_font.render('YOU WON!', False, (50, 180, 70), (100, 100, 100))
            aken.blit(voidetud_lava, (akna_laius / 5, akna_korgus / 3))
            pygame.display.flip()
            pygame.time.delay(4000)
            break

        # Vasak hiireklõps
        if pygame.mouse.get_pressed()[0] == 1:
            # Hiire koordinaadid
            hiire_pos = pygame.mouse.get_pos()
            peale_vajutatud_element = klikk(hiire_pos[0], hiire_pos[1])

            if peale_vajutatud_element == None:
                continue
            else:
                ava_ruut = kliki_tagajarg(peale_vajutatud_element)

                if ava_ruut == 'Miini otsas!':
                    rea_nr = peale_vajutatud_element // RUUTUDE_VEERGE
                    elemendi_nr = peale_vajutatud_element % RUUTUDE_VEERGE
                    maatriks[rea_nr][elemendi_nr] = 21
                    pygame.display.flip()
                    miini_otsa_astunud = True
                    # TODO avab kõik ruudud
                else:
                    rea_nr = peale_vajutatud_element // RUUTUDE_VEERGE
                    elemendi_nr = peale_vajutatud_element % RUUTUDE_VEERGE
                    
                    try:
                        maatriks[rea_nr][elemendi_nr] = 10 + ava_ruut
                    except:
                        pass
        
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

                # Kui parem hiireklõps on avamata ruudu peal, paneb sinna lipu
                if maatriks[rea_nr][elemendi_nr] == 0:
                    maatriks[rea_nr][elemendi_nr] = 22
                elif maatriks[rea_nr][elemendi_nr] == 1:
                    maatriks[rea_nr][elemendi_nr] = 23

                # Kui parem hiireklõps on lipu peal, paneb sinna eelneva avamata ruudu
                elif maatriks[rea_nr][elemendi_nr] == 22:
                    maatriks[rea_nr][elemendi_nr] = 0
                elif maatriks[rea_nr][elemendi_nr] == 23:
                    maatriks[rea_nr][elemendi_nr] = 1
                
                pygame.time.delay(100)
                
        
        # Uuendab pilti
        pygame.display.flip()

        # 60 fps
        kell.tick(FPS)
    
    pygame.quit()


########################
# Konstantsed muutujad #
########################

# Ühe ruudukese suurus pikslites
RUUDU_KULG = 20

# Mitu ruutu väljal on
RUUTUDE_VEERGE = 20
RUUTUDE_RIDU = 20

# Akna ääre paksus pikslites
SERVA_PAKSUS = 0

# Arvutab akna suuruse
akna_laius = RUUDU_KULG * RUUTUDE_VEERGE + 2 * SERVA_PAKSUS
akna_korgus = RUUDU_KULG * RUUTUDE_RIDU + 2 * SERVA_PAKSUS

# Mitu protsenti ruutudest on miinid
PROTSENT_MIINE = 10

# Loob kella fps-i jaoks
kell = pygame.time.Clock()

FPS = 60


#########################
# Programmi käivitamine #
#########################

if __name__ == '__main__':
    main()