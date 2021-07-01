from src.leilao.excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira: float):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor: float):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido('Não pode propor valor inferior ao valor da carteira')
            
        lance = Lance(self, valor)
        leilao.propoe(lance)
        
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_eh_valido(self, valor: float):
        return self.__carteira >= valor


class Lance:

    def __init__(self, usuario: Usuario, valor: float):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str):
        self.descricao = descricao
        self.__lances = []
        self.menor_valor = 0.0
        self.maior_valor = 0.0

    def propoe(self, lance: Lance):#hint type que não deixa ele estatico mas sim com a ideia do que queremos
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_valor = lance.valor

            self.maior_valor = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self.usarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))

    def usarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuario não pode dar dois lances seguidos!')

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor tem que ser superior ao valor anterior!')


    def _tem_lances(self):
        return self.__lances
