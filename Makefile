COM_COLOR   = \033[0;34m
OBJ_COLOR   = \033[0;36m
OK_COLOR    = \033[0;32m
ERROR_COLOR = \033[0;31m
WARN_COLOR  = \033[0;33m
NO_COLOR    = \033[m

OK_STRING    = "[OK]"
ERROR_STRING = "[ERROR]"
WARN_STRING  = "[WARNING]"

build: format

test: migrate
	@echo "--> Running tests"
	@python manage.py test --parallel
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

format: migrate
	@echo "--> Formating"
	@autopep8 --ignore=E501 -a -i $(shell find `pwd` -name "*.py")
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

migrate:
	@echo "--> Migrations"
	@python manage.py makemigrations
	@python manage.py migrate
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

populateDB:
	@echo "--> Populating database"
	@python manage.py loaddata users pointsEau
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

clean:
	@echo "--> Clean"
	@rm -rf $(shell find `pwd` -name "__pycache__")
# Clean database migration files
	@rm -f $(shell find `pwd` -type f -name "[0-9]*_initial.py")
	@rm -f $(shell find `pwd` -type f -name "db.sqlite3")
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

.PHONY: build migrate format test populateDB