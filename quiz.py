# SISTEMINHA DE PERGUNTAS E RESPOSTAS - QUIZ
# PARA DESENVOLVER ESSE PROGRAMA, UTILIZEI A ESTRUTURA DE DADOS DICIONÁRIO

import time

print('|-------------------------------------------|')
print('|                                           |')
print('|       PERGUNTAS & RESPOSTAS - QUIZ        |')
print('|                                           |')
print('|-------------------------------------------|')
print()
print('OBS.: ATIVE A OPÇÃO "CAPS LOOK" DO SEU TECLADO.')

perguntas = {
    'Pergunta 1': {
        'pergunta': '\nQUAL É A CIDADE MAIS RICA DO MUNDO?',
        'alternativas': {'A': 'SHANGAY', 'B': 'BERLIM', 'C': 'NEW YORK', 'D': 'PARIS'},
        'resposta': 'C'
    },
    'Pergunta 2': {
        'pergunta': '\nEM QUAL CIDADE JESUS NASCEU?',
        'alternativas': {'A': 'JERUSALÉM', 'B': 'BELÉM', 'C': 'SAMARIA', 'D': 'UR DOS CALDEUS'},
        'resposta': 'B'
    },
    'Pergunta 3': {
        'pergunta': '\nQUAL É A MAIOR CIDADE DA MUNDO?',
        'alternativas': {'A': 'TÓQUIO', 'B': 'SÃO PAULO', 'C': 'NEW YORK', 'D': 'LONDRES'},
        'resposta': 'A'
    },
    'Pergunta 4': {
        'pergunta': '\n3 x 4 DIVIDIDO POR 2?',
        'alternativas': {'A': '4', 'B': '7', 'C': '5', 'D': '6'},
        'resposta': 'D'
    },
    'Pergunta 5': {
        'pergunta': '\nNITERÓI, CAMPINAS, UBERLÂNDIA E RIO DE JANEIRO, ESTÃO LOCALIZADAS EM QUAL REGIÃO BRASILEIRA?',
        'alternativas': {'A': 'CENTRO-OESTE', 'B': 'SUDESTE', 'C': 'NORDESTE', 'D': 'SUL'},
        'resposta': 'B'
    },
    'Pergunta 6': {
        'pergunta': '\nA QUEM PERTENCE A FRASE: "FOI SEM QUERER QUERENDO"?',
        'alternativas': {'A': 'MAZAROPPI', 'B': 'SÉRGIO MALANDRO', 'C': 'CHAVES', 'D': 'DIDI'},
        'resposta': 'C'
    },
    'Pergunta 7': {
        'pergunta': '\nDE ACORDO COM A BÍBLIA, QUANTOS ERAM OS REIS MAGOS?',
        'alternativas': {'A': '4', 'B': '3', 'C': '2', 'D': '5'},
        'resposta': 'B'
    },
    'Pergunta 8': {
        'pergunta': '\nO QUE É UMA OMELETE?',
        'alternativas': {'A': 'EMPADA', 'B': 'TORTA', 'C': 'SALADA', 'D': 'OVO FRITO'},
        'resposta': 'D'
    },
    'Pergunta 9': {
        'pergunta': '\nCOMPLETE A FRASE: "FILHO DE PEIXE..."?',
        'alternativas': {'A': 'NADA NA LAGOA', 'B': 'VIVE MOLHADO', 'C': 'PEIXINHO É', 'D': 'MORA NO RIO'},
        'resposta': 'C'
    },
    'Pergunta 10': {
        'pergunta': '\nEM QUAL ANO O BRASIL FOI DESCOBERTO?',
        'alternativas': {'A': '1500', 'B': '1650', 'C': '1430', 'D': '2009'},
        'resposta': 'A'
    }
}

print('')

resposta_certa = 0

for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')

    #print('Alternativas: ')
    for rk, rv in pv["alternativas"].items():
        print(f'({rk}): {rv}')

    sua_resposta = input('RESPONDA: ')

    if sua_resposta == pv['resposta']:
        time.sleep(2)
        print('\033[1;32;40mRESPOSTA CERTA!\033[m')
        resposta_certa += 1
    else:
        time.sleep(2)
        print('\033[1;31;40mRESPOSTA ERRADA!\033[m')
    time.sleep(2)
    print('\n**********************************************')

    print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = resposta_certa / qtd_perguntas * 100

if porcetagem_acerto >= 70:
    print('\033[1;32;40mMEUS PARABÉNS, VOCÊ SABE MESMO!\033[m')
    print(f'PORCENTAGEM DE ACERTOS: {porcetagem_acerto}%')
else:
    print('\033[1;31;40mNOSSA, VOCÊ ERROU BASTANTE!\033[m')
    print(f'PORCENTAGEM DE ACERTOS: {porcetagem_acerto}%')