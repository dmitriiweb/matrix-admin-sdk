.PHONY: test
test:
	pytest --cov=matrix_admin_sdk -vv tests/
	flake8 matrix_admin_sdk tests/
	mypy matrix_admin_sdk --implicit-reexport
	black matrix_admin_sdk tests/
	isort matrix_admin_sdk tests/

.PHONY: docs-serve
docs-serve:
	mkdocs serve

.PHONY: docs-publish
docs-publish:
	mkdocs mkdocs gh-deploy --force

.PHONY: publish
publish:
	poetry build
	poetry publish
