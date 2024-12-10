import bcrypt

class HandlerPasswordHash:
    def gerar_hash(senha:str):
        return bcrypt.hashpw(senha, bcrypt.gensalt())
    
    def verificar_senha(senha:str, hash):
        return bcrypt.checkpw(senha, hash)