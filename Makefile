VENV_DIR = .venv
VENV = $(VENV_DIR)/bin/activate

$(VENV):
	python3 -m venv .venv
	. $(VENV) && pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf $(VENV)

run: $(VENV)
	. $(VENV) && python3 run.py

