.DEFAULT: help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: black isort flake8 pyright ## Check codebase with black, isort, flake8 and pyright

.PHONY: lint-fix
lint-fix:
	@ poetry run black ./src
	@ poetry run isort ./src

.PHONY: black
black:
	@ poetry run black --verbose --check -- ./src

.PHONY: isort
isort:
	@ poetry run isort ./src --check-only

.PHONY: flake8
flake8:
	@ poetry run flake8 --verbose ./src

.PHONY: pyright
pyright:
	@ poetry run pyright ./src

.PHONY: test
test: ## Runs all tests
	@ poetry run pytest

.PHONY: generate-markdown
generate-markdown: ## Generate validators.md documentation
	python3 ./utils/generate_docs.py
