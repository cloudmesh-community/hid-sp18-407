.PHONY: book images

FILE=abstract
#FLAGS=-interaction nonstopmode -halt-on-error -file-line-error
#FLAGS=-interaction nonstopmode  -file-line-error
FLAGS=-shell-escape
CLOUD=cloud
FLAGS=-shell-escape -output-directory=dest -aux-directory=dest


DEFAULT=$(CLOUD)

LATEX=pdflatex

#LATEX=pdfflatex
#LATEX=pydflatex -k


all: dest
	latexmk $(FLAGS) -pvc -view=pdf $(FILE)


pdflatex:
	pdflatex abstract
	bibtex abstract
	pdflatex abstract
	pdflatex abstract

clean:
	rm -f	*.pdf *.bbl *.log *.blg *.aux *.out *.idx *.run.xml *.bcf
	rm -rf dest

dest:
	mkdir dest

view:
	open abstract.pdf
