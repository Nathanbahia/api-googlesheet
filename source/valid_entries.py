def data_valida(data):
    if len(data) == 10:        
        if data[2] == '/' and data[5] == '/':
            if 1 <= int(data[:2]) <= 31:
                if int(data[:2]) > 28 and int(data[3:5]) == 2:                    
                    return False
                if 1 <= int(data[3:5]) <= 12:
                    if 2020 <= int(data[6:]) <= 2025:
                        return str(data)
                    else:
                        print("ano inválido")
                else:
                    print("mes invalido")
            else:
                print("dia invalido")
        else:
            print("barras")
    else:
        print("tamanho invalido")
    return False


def hora_valida(hora):
    if len(hora) == 5:
        if 0 <= int(hora[:2]) <= 23:        
            if 0 <= int(hora[3:]) <= 59:
                if hora[2] == ":":
                    return str(hora)
                else:
                    print("sem ponto")
            else:
                print("minutos inválidos")
        else:
            print("hora invalida")
    else:
        print("tamanho invalido")
    return False
