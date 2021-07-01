from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Guilherme', 500.0)
        self.yuri = Usuario('Yuri', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.leilao = Leilao('Celular')

        #formas de nomear uma função de testes, para escolher um desses 2 casos (tem outros)a propria equipe da empresa q escolhe
        #test_quando_adicionado_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance -Primeiro a situação dps o resultado
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self): #Primeiro a resultado dps o situação
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(100.0, self.leilao.menor_valor)
        self.assertEqual(150.0, self.leilao.maior_valor)

    def test_nao_deve_permitir_propor_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.maior_valor)
        self.assertEqual(150.0, self.leilao.menor_valor)

    def test_deve_retornar_o_maior_valor_e_o_menor_valor_quando_o_leilao_tiver_apenas_tres_lances(self):
        vini = Usuario('Vinicius', 500.0)
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        self.assertEqual(200.0, self.leilao.maior_valor)
        self.assertEqual(100.0, self.leilao.menor_valor)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)