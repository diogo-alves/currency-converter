APP_NAME = 'currency-converter'
PACKAGE_MANAGER = poetry
RUNNER = ${PACKAGE_MANAGER} run
TESTS_DIR = .

## @ Help
.PHONY: help
help: ## Exibe esta lista de comandos
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


## @ Dependencies
.PHONY: install
install: ## Instala as dependências do projeto
	@ echo "Instalando dependências do projeto..."
	${PACKAGE_MANAGER} install

.PHONY: run
run: ## Executa a aplicação localmente
	@ echo "Executando a aplicação..."
	uvicorn main:app --reload


.PHONY: linters
lint: ## Executa linters
	@ echo "Executando linters..."
	${RUNNER} pre-commit run --all-files


.PHONY: test docker-test
test: ## Executa testes localmente
	@ echo "Executando testes..."
	${RUNNER} pytest ${TESTS_DIR} -v
docker-test: ## Executa testes no docker
	@ echo "Executando testes..."
	docker-compose exec web pytest ${TESTS_DIR} -v


.PHONY: docker-build docker-run docker-start docker-stop docker
docker-build: ## Cria imagem docker com a aplicação
	@ echo "Iniciando serviços docker..."
	@docker image build -t ${APP_NAME}:1.0 .
docker-run: ## Executa a aplicação em um container docker
	@ echo "Executando container docker..."
	docker container run -d -p 8000:80 --name ${APP_NAME} --rm ${APP_NAME}:1.0
docker-stop: ## Para a execução do container docker
	@ echo "Parando container docker..."
	docker container stop ${APP_NAME}
docker-start: ## Inicia o container docker existente
	@ echo "Iniciando container docker existente..."
	docker container stop ${APP_NAME}
docker: docker-build docker-run ## Inicia criação da imagem e execução do container docker
