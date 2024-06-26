
requirements.txt:
	touch requirements.txt
	echo "pydantic" >> requirements.txt

requirements-dev.txt:
	touch requirements-dev.txt
	echo "pytest" >> requirements-dev.txt
	echo "ruff" >> requirements-dev.txt

.PHONY: update
update: .venv requirements.txt requirements-dev.txt
	@. .venv/bin/activate \
	&& pip install -r requirements.txt \
	&& pip install -r requirements-dev.txt

.venv:
	@echo "Create .venv"
	@python3 -m venv .venv
	make update
