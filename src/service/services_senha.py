from datetime import datetime
from uuid import uuid4
import random
from src.repositories.senha.repository_senha import SenhaRepo


class SenhaServiceFapi:
    repo = SenhaRepo

    # Inserindo dados no db (Funcionando)

    @classmethod
    def insert_one_senha(cls, qtd_caractere, apelido):
        letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
        letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"
        simbolos = "[]{}()*#;/.-_%"
        ape_senha = apelido
        tamanho_senha = qtd_caractere
        length = tamanho_senha

        # Criando a senha com todos os caracteres
        todos = letras_minusculas + letras_maiusculas + numeros + simbolos

        senha = "".join(random.sample(todos, length))

        unique_id = str(uuid4())
        criado_em = datetime.now()

        dict_insert = {
            "unique_id": unique_id,
            "criado_em": criado_em,
            "apelido_senha": ape_senha,
            "senha_criada": senha,
            "qtd_caractere": tamanho_senha,
        }

        cls.repo.insert_senha(dict_insert, ape_senha)
        return f'Senha Gerada {dict_insert}'

    # Lendo um dado

    @classmethod
    def get_one(cls, unique_id):
        collection = cls.repo.get_collection()
        senha_skip = collection.find({"unique_id": unique_id}, {"_id": False})
        raw_data = list(senha_skip)

        new_data = []

        for senha in raw_data:
            senha_nova = {
                "unique_id": senha["unique_id"],
                "senha_criada": senha["senha_criada"],
                "apelido_senha": senha["apelido_senha"],
                "qtd_caractere": senha["qtd_caractere"],
                "criado_em": senha["criado_em"],
            }
            new_data.append(senha_nova)

        return_obj = {"Dados": new_data}

        return return_obj

    # Lendo todos os dados do banco (Funcionando)
    @classmethod
    def get_all(cls):
        collection = cls.repo.get_collection()
        senha_skip = collection.find({}, {"_id": False})
        raw_data = list(senha_skip)

        new_data = []

        for senha in raw_data:
            senha_nova = {
                "unique_id": senha["unique_id"],
                "senha_criada": senha["senha_criada"],
                "apelido_senha": senha["apelido_senha"],
                "qtd_caractere": senha["qtd_caractere"],
                "criado_em": senha["criado_em"],
            }
            new_data.append(senha_nova)

        return_obj = {"Dados": new_data}

        return return_obj

    # Delete Trainer (Funcionando)

    @classmethod
    def delete_trainer(cls, unique_id):
        data = {"unique_id": unique_id}
        dt = cls.repo.del_one_senha(data)
        return f"{dt} Dados deletado."
