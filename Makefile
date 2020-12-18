NAME = nsi
PDF = $(NAME).pdf
PANDOC = pandoc -s -N --template=template.tex


SRC = metadata.yml \
      $(sort $(wildcard content/*.md))

$(PDF): $(SRC)
	$(PANDOC) $(SRC) -o $(PDF)