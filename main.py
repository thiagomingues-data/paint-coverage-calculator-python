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
litros_com_folga = litros_tinta * 1.10

qtd_latas_mix = int(litros_com_folga // lata)
resto = litros_com_folga % lata

qtd_galoes_mix = int(resto // galao)
if resto % galao != 0:
    qtd_galoes_mix += 1

valor_total_mix = (qtd_latas_mix * p_lata) + (qtd_galoes_mix * p_galao)

print("\nMistura otimizada (10% folga):")
print(qtd_latas_mix, "lata(s) e", qtd_galoes_mix, "galão(ões)")
print("Valor total: R$", valor_total_mix)
