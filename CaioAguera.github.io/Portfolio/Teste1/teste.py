hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))
hora_termino = int(input("Digite a hora de término: "))
minuto_termino = int(input("Digite o minuto de término: "))

if minuto_termino < minuto_inicio:
    minuto_termino += 60
    hora_termino -= 1
if hora_termino < hora_inicio:
    hora_termino += 24

duracao_minuto = minuto_termino - minuto_inicio
duracao_hora = hora_termino - hora_inicio
duracao = duracao_hora * 60 + duracao_minuto

print(f"A duração é de {duracao} minutos.")