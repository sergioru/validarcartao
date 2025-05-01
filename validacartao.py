import re

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def get_card_brand(card_number):
    card_number = str(card_number)
    patterns = {
        "Visa":        r"^4\d{15}$",
        "MasterCard":  r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$",
        "American Express": r"^3[47]\d{13}$",
        "Diners Club": r"^3(0[0-5]|[68]\d)\d{11}$",
        "Discover":    r"^6(011\d{12}|5\d{14}|4[4-9]\d{13})$",
        "EnRoute":     r"^(2014|2149)\d{11}$",
        "JCB":         r"^(352[89]\d{12}|35[3-8]\d{13})$",
        "Voyager":     r"^8699\d{11}$",
        "HiperCard":   r"^(606282\d{10}(\d{3})?)$",
        "Aura":        r"^50\d{14,17}$"  # Simplificado para cobrir prefixo 50 e comprimento de 15 a 18 dígitos
    }
    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand
    return "Desconhecida"

def validar_cartao(numero):
    valido = luhn_check(numero)
    bandeira = get_card_brand(numero)
    return valido, bandeira

# Exemplo de uso:
numero = input("Digite o número do cartão: ").replace(" ", "")
valido, bandeira = validar_cartao(numero)
if valido:
    print(f"Cartão válido. Bandeira: {bandeira}")
else:
    print("Cartão inválido.")