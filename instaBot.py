## Instabot Version 1.0 ##
import webbrowser
import time
import pyautogui

users = ['ddudaamarcondes', 'taycazotto', 'babugia_dix', 'indiraklepa', 'jeancodel', 'micaelly_om' , 'thays_layne_', 'mariazinha.block', 'gabsbilk', 'mariac_paganini', 'dixx_vitinnn', 'anaamaciiell','aghetone_oceet', 'felipe.ponto', 'varelllinha', 'ju_jamnik', 'iscza', 'clar.a0', 'aliciamichalki', 'annaalcaq', 'juliadher', 'fernandacecyn', 'kethgotts', 'victor_bart19', 'juliana.vv', 'sergiossauro', 'tuhane.novosad', 'tovomate', 'pietrogcf', 'rodolfo_presa', 't3mpest4d3', 'diebarba', 'lucas.faian', 'leticiacolucci_15', 'eevee_lucy', 'deborapicoli','jesszsx', 'milenaplens', 'mariacorrdeiro', 'luishsalomao', 'tiepo.lo', 'jonnifer.feltrin', 'fernanda.dviana', 'celitamoraski', 'bruninha_braz', 'jusubeer', 'sammiancz', 'jvictorrebecchi', 'leogradici', 'faelmilani']

webbrowser.open('https://www.instagram.com/p/CBgt0TlhTxR/')
time.sleep(1.5)

pyautogui.scroll(-2)
time.sleep(2)
i = 0
while i<len(users)-1:
    time.sleep(2)
    if i>56:
        break
    pyautogui.click(x=829, y=641)
    pyautogui.write('@'+users[i])
    pyautogui.click(x=1097,y=649)
    print('@'+users[i])
    i += 1
    time.sleep(3)
