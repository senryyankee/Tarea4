data_targets = Datos.dat
image_targets1 = t_1.png t_2.png
image_targets2 = planetas.png

Resultados_hw3.pdf : Resultados_hw3.tex $(image_targets) planetas.png
	pdflatex $< && rm *.aux *.log

planetas.png : Plots_planetas.py
	python $<

$(image_targets) : onda.py $(data_targets)
	python $<

$(data_targets) : a.out
	./a.out

a.out : planetas.c
	gcc -lm -g canal_ionico.c

clean :
	rm *.dat *.png a.out *.pdf
