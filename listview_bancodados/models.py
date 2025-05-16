from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///lista.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIOS'
    id_funcionario = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, index=True)
    cargo = Column(String(50), nullable=False, index=True)
    salario = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return '<Funcionarios: Nome: {} Cargo: {} Salario: {}>'.format(self.nome, self.cargo, self.salario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_funcionarios = {
            'id do fucionário': self.id_funcionario,
            'nome': self.nome,
            'Cargo': self.cargo,
            'salario': self.salario
        }

        return dados_funcionarios

class Livro(Base):
    __tablename__ = 'LIVROS'
    id_livro = Column(Integer, primary_key=True)
    titulo = Column(String(80), nullable=False, index=True)
    autor = Column(String(50), nullable=False, index=True)
    descricao = Column(String(200), nullable=False, index=True)
    categoria = Column(String(30), nullable=False, index=True)


    def __repr__(self):
        return '<Livros: Titulo: {} Autor: {} Descricao: {} Categoria: {}>'.format(self.titulo, self.autor, self.descricao, self.categoria)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_livros = {
            'Id do livro': self.id_livro,
            'Titulo': self.titulo,
            'Autor': self.autor,
            'Categoria': self.categoria,
            'Descrição': self.descricao
        }

        return dados_livros

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
