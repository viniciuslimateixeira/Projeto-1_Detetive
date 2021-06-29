# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.

from random import randint
from time import sleep
from operator import itemgetter
from rich.console import Console
console = Console()
resultados = list()
rodada = 0 # contador de rodadas
vit_jogador1 = vit_jogador2 = vit_jogador3 = vit_jogador4 = 0 # contador de vitórias de cada jogador
def linhas(linha): # função para adicionar linha de formatação
    l = '-=' * linha
    return l

console.print('''[bold green]
𝓑𝓮𝓶 𝓿𝓲𝓷𝓭𝓸 𝓪𝓸 𝓳𝓸𝓰𝓸 𝓭𝓮 𝓭𝓪𝓭𝓸𝓼❗ 𝓥𝓪𝓶𝓸𝓼 𝓳𝓸𝓰𝓪𝓻❓❗[/bold green]
''') 
rodadas = int(input('''
𝓠𝓾𝓪𝓷𝓽𝓪𝓼 𝓻𝓸𝓭𝓪𝓭𝓪𝓼 𝓽𝓮𝓻𝓪́ 𝓸 𝓷𝓸𝓼𝓼𝓸 𝓳𝓸𝓰𝓸❓ 
''')) # Usuário define quantas rodadas terá o jogo
for c in range(0,rodadas): # armazena os números jogados no dicionário, de acordo com a quantidade de rodadas definida anteriormente
    jogo = {'jogador1': randint(1,6),
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)}
    rodada += 1 # quantifica o número de rodadas
    for k, v in jogo.items(): # Mostra o que cada jogador tirou em determinada jogada
        print(f''' 
        Na rodada {rodada}:
        O {k} tirou {v}.
        ''')
        sleep(2)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Mostra de maneira decrescentes os números tirados no jogo, mostrando o vencedor de cada rodada
    vencedor = ranking[0]
    jogador_venc = vencedor[0]
    console.print(f' [bold red] O vencedor é {jogador_venc}[/bold red]')
    print(f'\n{linhas(20)}\n')
    if jogador_venc == 'jogador1': # Define o número de vitórias de cada jogador
        vit_jogador1 += 1
    elif jogador_venc == 'jogador2':
        vit_jogador2 += 1
    elif jogador_venc == 'jogador3':
        vit_jogador3 += 1
    elif jogador_venc == 'jogador4':
        vit_jogador4 += 1
vitorias = [vit_jogador1, vit_jogador2, vit_jogador3, vit_jogador4] # Armazena o número de vitórias de cada jogador
for i, v in enumerate(vitorias): # Mostra o número de vitórias de cada jogador
    print(f'O jogador {i + 1} venceu {v} rodadas')
    sleep(1)
print(f'\n{linhas(20)}\n')
campeao = max(vitorias) # variável usada em conjunto com a funcão if, para definir o grande campeão
if campeao == vit_jogador1:
    console.print('''[bold red]
    𝕆 𝕁𝕆𝔾𝔸𝔻𝕆ℝ 𝟙 𝔼́ 𝕆 𝔾ℝ𝔸ℕ𝔻𝔼 ℂ𝔸𝕄ℙ𝔼𝔸̃𝕆!!! 🏆🏆🏆[/bold red] 
    ''')
elif campeao == vit_jogador2:
    console.print('''[bold red]
    𝕆 𝕁𝕆𝔾𝔸𝔻𝕆ℝ 𝟚 𝔼́ 𝕆 𝔾ℝ𝔸ℕ𝔻𝔼 ℂ𝔸𝕄ℙ𝔼𝔸̃𝕆!!! 🏆🏆🏆[/bold red] 
    ''')
elif campeao == vit_jogador3:
    console.print('''[bold red]
    𝕆 𝕁𝕆𝔾𝔸𝔻𝕆ℝ 𝟛 𝔼́ 𝕆 𝔾ℝ𝔸ℕ𝔻𝔼 ℂ𝔸𝕄ℙ𝔼𝔸̃𝕆!!! 🏆🏆🏆[/bold red] 
    ''')
else:
    console.print('''[bold red]
    𝕆 𝕁𝕆𝔾𝔸𝔻𝕆ℝ 𝟜 𝔼́ 𝕆 𝔾ℝ𝔸ℕ𝔻𝔼 ℂ𝔸𝕄ℙ𝔼𝔸̃𝕆!!! 🏆🏆🏆[/bold red] 
    ''')

    

    

    

      
             


