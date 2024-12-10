from sqlalchemy import create_engine
from sqlalchemy.sql import text

class DBConnectionHanlder:
    def __init__(self):
        self.__connection_string = '{}:///{}'.format(
            'sqlite',
            'database.db'
        )
        self.__engine = None
        self.connection = None
    
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)
        print('Banco de Dados conectado.')

    def execute_sql(self, query:text, **kwargs) -> None:
        self.connection.begin()
        try:
            self.connection.execute(query)
            self.connection.commit()
            print('Comando executado com sucesso!')
        except Exception as error:
            self.connection.rollback()
            print('Comando com erro!')
            raise error

    def __enter__(self):
        self.connection = self.__engine.connect()
        return self.connection

    def __exit__(self, *_):
        self.connection.close()

    def get_engine(self):
        return self.__engine

db_connection_handler = DBConnectionHanlder()