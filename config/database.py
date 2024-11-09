from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        try:
            connection_string = self.__get_connection_strings()

            self.engine = create_engine(
                connection_string,
                poolclass=QueuePool,
                pool_size=10,
                max_overflow=20,
                pool_pre_ping=True,
                pool_use_lifo=True,
                pool_timeout=60,
                pool_recycle=1800
            )

            if not database_exists(self.engine.url):
                create_database(self.engine.url)

            self.session_factory = sessionmaker(bind=self.engine)
            self.session = scoped_session(self.session_factory)

        except Exception as e:
            raise Exception(f'Error en conexion Base de datos: {e}')

    def __get_connection_strings(self):
        """
        Devuelve la cadena de conexión con el nombre de la base de datos
        """
        user = os.getenv('USER_DB')
        password = os.getenv('PASSWORD_DB')
        host = os.getenv('SERVER_DB')
        db_name = os.getenv('NAME_DB')

        string_conexion = f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}"
        # string_conexion = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"
        return string_conexion

    def get_session(self):
        return self.session

    def close_session(self):
        if self.session:
            self.session.close()
            self.session.remove()
