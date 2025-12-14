#Lista de convidados para festa
convidados = ["Ana", "Bruno", "Carla", "Elen", "Clara"]
print(f"O convidadado {convidados[2]} não poderá comparecer à festa.")
print("Pessoal consegui uma mesa maior, provavelmente convidarei mais pessoas.")
convidados.insert(0, "João")
convidados.insert(3, "Mariana")
convidados.append("Breno")
print("Infelizmente só vou conseguir convidar duas pessoas para a festa.")
del convidados[0:5]
popped_convidados = convidados.pop()
print(f"Desculpe {popped_convidados.title()}, mas não poderei convidá-los para a festa.")
print(f"Pessoal, tive alguns imprevistos, porém vocês ainda estão convidados {convidados}.")
quantidade= len(convidados)
print(quantidade)
del convidados[0]
del convidados[0]
print(quantidade:int)