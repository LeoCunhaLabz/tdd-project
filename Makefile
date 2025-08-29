run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

precommit-reset:
	@rm -rf ~/.cache/pre-commit
	@poetry run pre-commit clean
	@poetry run pre-commit install --install-hooks
