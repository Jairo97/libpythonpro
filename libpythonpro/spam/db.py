class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        self.contador += 1
        usuario.id = self.contador
        self.usuarios.append(usuario)

    def roll_back(self):
        self.usuarios.clear()

    def fechar(self):
        pass

    def listar(self):
        return self.usuarios


class Conexao:
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
