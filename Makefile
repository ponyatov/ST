# \ var
MODULE  = $(notdir $(CURDIR))
OS      = $(shell uname -s)
NOW     = $(shell date +%d%m%y)
REL     = $(shell git rev-parse --short=4 HEAD)
BRANCH  = $(shell git rev-parse --abbrev-ref HEAD)
CORES   = $(shell grep processor /proc/cpuinfo| wc -l)
AUTHOR  = "Dmitry Ponyatov"
EMAIL   = "dponyatov@gmail.com"
# / var

# \ dir
CWD     = $(CURDIR)
BIN     = $(CWD)/bin
DOC     = $(CWD)/doc
LIB     = $(CWD)/lib
SRC     = $(CWD)/src
TMP     = $(CWD)/tmp
CAR     = $(HOME)/.cargo/bin
# / dir

# \ tool
CURL    = curl -L -o
PY      = $(shell which python3)
PIP     = $(shell which pip3)
PEP     = $(shell which autopep8)
PYT     = $(shell which pytest)
RUSTUP  = $(CAR)/rustup
CARGO   = $(CAR)/cargo
RUSTC   = $(CAR)/rucstc
# / tool

# \ src
Y   += $(MODULE).metaL.py metaL.py
Y   += $(MODULE).py test_$(MODULE).py
P   += config.py
S   += $(Y)
R   += $(shell find src -type f -regex ".+.rs$$")
S   += $(R) Cargo.toml
# / src

# \ all

.PHONY: py
py: $(PY) $(MODULE).py
	$(MAKE) test_py format
	$^ $@

.PHONY: rs
rs: $(R)
	$(CARGO) test && $(CARGO) fmt && $(CARGO) run

.PHONY: meta
meta: $(PY) $(MODULE).metaL.py
	$^
	$(MAKE) format

# \ test
.PHONY: test
test: test_py test_rs

.PHONY: test_py
test_py: $(PYT) test_$(MODULE).py
	$^

.PHONY: test_rs
test_rs: $(R)
	$(CARGO) test
# / test

format: tmp/format_py
tmp/format_py: $(Y)
	$(PEP) --ignore=E26,E302,E305,E401,E402,E701,E702 --in-place $?
	touch $@

watch:
	$(CARGO) watch -w Cargo.toml -w src -x test -x fmt -x run
# / all

# \ doc

.PHONY: doxy
doxy:
	rm -rf docs ; doxygen doxy.gen 1>/dev/null
	rm -rf target/doc ; $(CARGO) doc --no-deps && cp -r target/doc docs/rust

.PHONY: doc
doc: doc/BlueBook.pdf doc/ALittleSmalltalk.pdf doc/PERQ.pdf
doc/BlueBook.pdf:
	$(CURL) $@ http://stephane.ducasse.free.fr/FreeBooks/BlueBook/Bluebook.pdf
doc/ALittleSmalltalk.pdf:
	$(CURL) $@ https://github.com/ponyatov/budd/releases/download/060120-c1c7/ALittleSmalltalk.pdf
doc/PERQ.pdf:
	$(CURL)	$@ http://www.wolczko.com/msc.pdf
# / doc

# \ install
.PHONY: install update
install: $(OS)_install doc $(RUSTUP)
	$(MAKE) update
update: $(OS)_update
	$(MAKE) Python_update
	$(RUSTUP) update && $(CARGO) update

.PHONY: Python_update
Python_update:
	$(PIP) install --user -U pip pytest autopep8
	$(PIP) install --user -U -r requirements.txt

.PHONY: Linux_install Linux_update
Linux_install Linux_update:
ifneq (,$(shell which apt))
	sudo apt update
	sudo apt install -u `cat apt.txt apt.dev`
endif

.PHONY: Msys_install Msys_update
Msys_install:
	pacman -S git make python3 python3-pip
Msys_update:

$(RUSTUP):
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# / install

# \ merge
MERGE  = Makefile README.md .gitignore apt.dev apt.txt apt.msys doxy.gen $(S)
MERGE += .vscode bin doc lib src tmp
MERGE += requirements.txt

.PHONY: ponymuck
ponymuck:
	git push -v
	git checkout $@
	git pull -v

.PHONY: dev
dev:
	git push -v
	git checkout $@
	git pull -v
	git checkout ponymuck -- $(MERGE)
	$(MAKE) doxy ; git add -f docs

.PHONY: release
release:
	git tag $(NOW)-$(REL)
	git push -v --tags
	$(MAKE) ponymuck

.PHONY: zip
ZIP = $(TMP)/$(MODULE)_$(BRANCH)_$(NOW)_$(REL).src.zip
zip:
	git archive --format zip --output $(ZIP) HEAD
	$(MAKE) doxy ; zip -r $(ZIP) docs
# / merge
