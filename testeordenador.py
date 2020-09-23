import ordenador
import pytest
import contatempo

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = contatempo.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = contatempo.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bubblesort(l_aleat)
        assert self.esta_ordenada(l_aleat)
