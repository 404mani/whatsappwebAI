import time
from simon.accounts.pages import LoginPage
from simon.header.pages import HeaderPage
from simon.pages import BasePage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
import random

# Waveigl Whatsapp Artificial Intelligence 1.0;
# Please read README.md before executing or configurating this '.py' file.
# Note that this application was developed for only educational purposes.



#PLEASE REPLACE ABOVE WITH YOUR BROWSER AND DIRECTORY.
from selenium import webdriver
ndriver = webdriver.Chrome('C:/Users/ucdhs/Downloads/chromedriver_win32/chromedriver.exe')
ndriver.get('https://web.whatsapp.com/')

#Artificial Intelligence Login
login = LoginPage(ndriver) #Attributing the driver inside of the LoginPage class.
login.load()
login.remember_me = False
time.sleep(17)  #Timesleeping until your Whatsapp Web is ready

Quantiaultimasmsgs = input('Last messages count per read, please provide an INT value: ')

##IGNORE UNTIL LINE __CONFIG__

#checagem do zapzapzapzapzapkkk
whatspage = BasePage(ndriver)
whatspage.is_title_matches()
whatspage.is_welcome_page_available()
whatspage.is_nav_bar_page_available()
whatspage.is_search_page_available()
whatspage.is_pane_page_available()
whatspage.is_chat_page_available()

pnPage = PanePage(ndriver)
Chatsabertos = pnPage.opened_chats

for i in Chatsabertos:
    print(i.name) #nome do ctt
    print(i.last_message) #ultima msg do contato
    print(i.has_notifications()) #verificar se existe alguma mensagem que não foi lida
    print(i.notifications) #bruh1

Chatsabertos[0].click()

chat = ChatPage(ndriver)
ultimasmensagens = chat.messages.newest(int(Quantiaultimasmsgs), filterby = 'contact')

for mensagem in ultimasmensagens:
    print(mensagem.contact)
    print(mensagem.status)
    print(mensagem.date)

MensagemMaisRecente = ultimasmensagens[0]
MensagemMaisRecente = chat.messages.newest(filterby='contact')

#Configuration, do whatever you want with your waveigl bot

xing = ('fdp','merda','cala','puta','debil','débil','fds','clb','clbc','puto','gay','mongol','mongolice','idiota','lixo','mama','nunca')
justificativas = ('pois','porque')
pergunta = ('?')
cumprimento = ('oi', 'eae', 'noite','dia','tarde')
nao = ('n','nao','não')
tais = ('tais demente?','tais sendo um idiota','tais com mongolice mental','tais de tais ne de tais que tais de tais pq tais ne prr','tais banido da black belt','tais ficando doente','tais sendo um repetente filha duma puta do caralho','tais sendo um tryunfo','tais ficando retardado','fudido','tais sendo um merda InsaNNE', 'caralho cara, puta merda', f'O QUE QUE TEM A VER {str.upper(MensagemMaisRecente.text)} COM A NOSSA CONVERSA EU TO FALANDO DE CS AQUI, {str.upper(MensagemMaisRecente.contact)}, vai se fude!!!','na moral de boa velho','tremendo desrespeito irmão nmrl cara','tomaste ja teu ban de 24 horas')

#desrespeitos (de acordo com o titio wave)
for i in xing:
    if i in str(MensagemMaisRecente.text):
        diasdeban = random.randrange(2,50)
        mensagemrandom = random.randrange(0,3)
        if mensagemrandom == int(0):
            MensagemMaisRecente.reply(f'beleza, tais banido da black belt por {diasdeban}')
        elif mensagemrandom == int(1):
            MensagemMaisRecente.reply('na moral de boa velho')
            time.sleep(random.randrange(0.0,5.0))
            MensagemMaisRecente.reply('se continuar a me desrespeitar irmao')
            time.sleep(random.randrange(0.0,5.0))
            MensagemMaisRecente.reply(f'vais tomar um ban de {diasdeban}')
            time.sleep(0.4)
            MensagemMaisRecente.reply('pq isso é um tremendo desrespeito irmão')
        elif mensagemrandom == int(2):
            MensagemMaisRecente.reply(f'tais banido, sem jogar aqui na black belt por {diasdeban} dias')
            time.sleep(random.randrange(0,2.5))
            MensagemMaisRecente.reply(f'o unico jeito de te suportar é vindo aqui no FireDash')
        elif mensagemrandom == int(3):
            MensagemMaisRecente.reply(f'na moral de boa velho, tais banido da black belt por {diasdeban} dias')

#justificativas
for i in justificativas:
    if i in str(MensagemMaisRecente.text):
        mensagemrandom = random.randrange(0,4)
        diasdeban = random.randrange(0,100)
        if mensagemrandom == int(0):
            MensagemMaisRecente.reply(f'Tais tentando justificar o que?')
            time.sleep(0.2)
            MensagemMaisRecente.reply(f'teis mongolice mental, {str(MensagemMaisRecente.contact)} ?')
            time.sleep(0.25)
            MensagemMaisRecente.reply(f'Na moral de boa velho, da próxima vez que tu justificar algo que eu não to perguntando vai ser {diasdeban} dias de ban')
        elif mensagemrandom == int(1):
            MensagemMaisRecente.reply('tais justificando o que?')
            time.sleep(0.40)
            MensagemMaisRecente.reply('seu filho da puta do MEU CARALHO!!1')
        elif mensagemrandom == int(2):
            MensagemMaisRecente.reply(f'vem cá, tu acha que um cara como eu, com mais de 30 mil horas de cs, tem tempo pra ler a MERDA da sua justificativa? vai estudar irmao, nem deve ter carteira assinada e quer vir encher o saco do top 9 nacional, vá se arrombar, vá se fuder {str(MensagemMaisRecente.contact)}!!! ')
            time.sleep(0.2)
            MensagemMaisRecente.reply('seu coco')
        elif mensagemrandom == int(3):
            MensagemMaisRecente.reply('na moral, de boa velho')
            time.sleep(1)
            MensagemMaisRecente.reply(f'da proxima vez que tu tentar justificar algo que eu não pedi vai ser {diasdeban} dias de ban da black belt irmao')
        elif mensagemrandom == int(4):
            MensagemMaisRecente.reply(f'Chega {str(MensagemMaisRecente.contact)}, tais fora da black belt por {diasdeban} dias.')
            time.sleep(0.2)
            MensagemMaisRecente.reply('sabe por que irmao?')
            time.sleep(1)
            MensagemMaisRecente.reply(f'porque a gente ja teve essa conversa, {str(MensagemMaisRecente.contact)}, e mesmo assim você continua a tentar justificar aquilo que eu não pedi, tais maluco né porra')

#cumprimentos
for i in cumprimento:
    if i in str(MensagemMaisRecente.text):
        mensagemrandom = random.randrange(0,2)
        
        if mensagemrandom == int(0):
            if i == 'oi' or i == 'eae':
                MensagemMaisRecente.reply(f'{str(MensagemMaisRecente.contact)}, to irritado, caso vc me irrite nesse próximo jogo é ban da black belt velho.')
            else:
                MensagemMaisRecente.reply(f'Bom(a) {i}, {str(MensagemMaisRecente.contact)}, n vem de mimimi hoje não que eu to irritado')
        elif mensagemrandom == int(1):
            if i == 'oi' or i == 'eae':
                MensagemMaisRecente.reply(f'{str(MensagemMaisRecente.contact)}, tais banido da black belt.')
                time.sleep(0.5)
                MensagemMaisRecente.reply('sabes por que?')
                time.sleep(0.1)
                MensagemMaisRecente.reply('pq vc ja tava vendo a live sabendo que eu to irritado, então fica na sua, tomaste já o seu ban de 24 horas.')
            else:
                MensagemMaisRecente.reply(f'Bom(a) {i} é o caralho irmao, tais louco? tais com mongolice?')
                time.sleep(0.7)
                MensagemMaisRecente.reply('seu cocô do caralho, do meu saco,repetente de ovo!')
        elif mensagemrandom == int(2):
            if i == 'oi' or i == 'eae':
                MensagemMaisRecente.reply(f'{str(MensagemMaisRecente.contact)}, oi é o caralho irmao, tais banido 24 horas')
            else:
                MensagemMaisRecente.reply(f'Bom(a) {i} é o caralho irmao, tais louco? tais com mongolice?')
                time.sleep(0.7)
                MensagemMaisRecente.reply('seu cocô do caralho, do meu saco,repetente de ovo!')
for i in nao:
    if i in str(MensagemMaisRecente.text):
        anosdeban = {1,2}
        if anosdeban == int(2):
            anosdeban = 'permanentemente'
        else:
            anosdeban = 'por 1 ano'
        mensagemrandom = random.randrange(0,1)
        if mensagemrandom == int(0):
            MensagemMaisRecente.reply(f'na moral de boa velho, não tais querendo obedecer né? tais banido {anosdeban}')
        if mensagemrandom == int(1):
            MensagemMaisRecente.reply(f'não? tais tentando me deixar maluco??? tais banido {anosdeban}')
ntais = random.randrange(0,15)
MensagemMaisRecente.reply(str(tais[int(ntais)]))





