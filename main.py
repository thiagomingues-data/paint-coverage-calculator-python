# Paint Store Calculator
# Calculates paint consumption and cost based on area

area = float(input('Informe o tamanho da área a ser pintada em m²: '))

# Rule: 1 liter covers 6 m²
litros_tinta = area / 6

# Container sizes
lata = 18
galao = 3.6

# Prices
p_lata = 80
p_galao = 25

print("\nÁrea:", area, "m²")
print(f"Litros necessários: {litros_tinta:.2f}")

# -----------------------------
# 1. Only 18L cans (latas)
# -----------------------------
qtd_latas = int(litros_tinta // lata) + 1
valor_latas = qtd_latas * p_lata

print("\nSomente latas (18L):")
print(qtd_latas, "lata(s)")
print("Valor: R$", valor_latas)

# -----------------------------
# 2. Only 3.6L gallons (galões)
# -----------------------------
qtd_galoes = int(litros_tinta // galao) + 1
valor_galoes = qtd_galoes * p_galao

print("\nSomente galões (3.6L):")
print(qtd_galoes, "galão(ões)")
print("Valor: R$", valor_galoes)

# -----------------------------
# 3. Optimized mix (10% safety margin)
# -----------------------------
litros_tinta_margem =litros_tinta* 1.10
print(f'{litros_tinta_margem:.2f} litros, adicionando uma margem de 10%')
print()

# quantidade inicial de latas
latas = litros_tinta_margem // 18

# litros que ainda faltam
restante = litros_tinta_margem % 18

# quantidade de galões
galoes = restante // 3.6

if restante % 3.6 != 0:
    galoes += 1

# compara os preços
if galoes * 25 < 80:
    preco = latas * 80 + galoes * 25
else:
    latas += 1
    galoes = 0
    preco = latas * 80

print(f'Latas : {latas:.0f}')
print(f'Galões: {galoes:.0f}')
print(f'Preço : R$ {preco:.2f}')
