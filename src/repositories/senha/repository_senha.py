from src.infrastructures.mongo.infrastructure import MongoInfrastructure


class SenhaRepo:
    infrastructure = MongoInfrastructure
    db = "gerador_de_senhas"
    collection = "gerador_senhas"

    # Definindo a collection
    @classmethod
    def get_collection(cls):
        infra = cls.infrastructure.get_client()
        database = infra[cls.db]
        collection = database[cls.collection]
        return collection

    # Inserindo no db
    @classmethod
    def insert_senha(cls, inserindo_senha, apelido_sen):
        collection = cls.get_collection()
        return collection.insert_one(inserindo_senha, apelido_sen)

    # Lendo um dado
    @classmethod
    def get_one_senha(cls, find_one_senha):
        collection = cls.get_collection()
        return collection.find_one(find_one_senha)

    # Lendo todos
    @classmethod
    def get_all_password(cls):
        collection = cls.get_collection()
        senha_skip = collection.find({})
        resultado = list(senha_skip)
        return resultado

    # Deletando um dado
    @classmethod
    def del_one_senha(cls, deletar):
        collection = cls.get_collection()
        delete_onee = collection.delete_one(deletar)
        return delete_onee
