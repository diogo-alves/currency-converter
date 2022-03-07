# Conversor de Moedas

 [![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/diogo-alves/currency-converter/blob/main/LICENSE) [![ci](https://github.com/diogo-alves/currency-converter/actions/workflows/ci.yaml/badge.svg)](https://github.com/diogo-alves/currency-converter/actions/workflows/ci.yaml) [![codecov](https://codecov.io/gh/diogo-alves/currency-converter/branch/main/graph/badge.svg)](https://codecov.io/gh/diogo-alves/currency-converter)

Uma API REST para conversão de moedas com base na cotação do dólar americano (USD)


## Preview

Este projeto pode ser acessado diretamente no [Heroku](https://fastapi-currency-converter.herokuapp.com/docs).

[![currency-converter](https://i.imgur.com/BPeCKY8.png)](https://fastapi-currency-converter.herokuapp.com/docs)


## Uso

A API suporta conversões entre as seguintes moedas:
- USD
- BRL
- EUR
- BTC
- ETH

Uma requisição válida deve fornecer como parâmetros:

* `from` -  a moeda de origem
* `to` - a moeda final
* `amount` - o valor a ser convertido

### Exemplo de Requisição

    http://localhost:8000/v1/conversion?from=USD&to=BRL&amount=10


### Exemplo de Retorno
```json
{
    "result": 50.879149999999996
}
```

## Documentação (OpenAPI)

- Swagger UI: [```(http://localhost:8000/docs```](http://localhost:8000/docs)
- Redoc: [```http://localhost:8000/redoc```](http://localhost:8000/redoc)


## Executando a Aplicação

### Pré-requisitos

- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Make](https://www.gnu.org/software/make/)¹

¹ **NOTA**: A maioria das distribuições linux já disponibiliza o `Make` por padrão. Usuários Windows podem realizar o download [aqui](http://gnuwin32.sourceforge.net/packages/make.htm).

### Configuração

1. Clone este repositório:

```shell
git clone git@github.com:diogo-alves/currency-converter.git
```

2. Acesse a pasta do repositório:

```shell
cd currency-converter
```

3. Instale as dependências do projeto:

```shell
make install
```

4. Copie o arquivo```.env.example```, renomeie sua cópia para ```.env``` e informe os valores das variáveis de ambiente. Para gerar a chave da API de cotações clique [aqui](https://openexchangerates.org/signup/free) e faça seu cadastro.

## Execução

### Local

```shell
make run
```

### Em Ambiente Docker

```shell
make docker
```


## Testes

```shell
make test
```
ou

```shell
make docker-test
```

## Linters

```shell
make lint
```


## Outros Comandos Disponíveis

Para ver a lista de todos os comandos utilitários disponíveis:
```shell
make help
```


## Licença

Este projeto está sob os termos da licença [MIT](./LICENSE).
