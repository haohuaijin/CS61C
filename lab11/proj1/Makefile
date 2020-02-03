CC = gcc
CFLAGS = -lm -g

Mandelbrot: ComplexNumber.o Mandelbrot.o MandelFrame.o
	$(CC) -o MandelFrame ComplexNumber.o Mandelbrot.o MandelFrame.o $(CFLAGS)

MandelMovie: ComplexNumber.o Mandelbrot.o MandelMovie.o ColorMapInput.o
	$(CC) -o $@ ComplexNumber.o Mandelbrot.o MandelMovie.o ColorMapInput.o $(CFLAGS)

colorPalette: ColorMapInput.o colorPalette.o
	$(CC) -o $@ ColorMapInput.o colorPalette.o $(CFLAGS)

testA:	Mandelbrot
	./MandelFrame 2 1536 -0.7746806106269039 -0.1374168856037867 1e-5 100 student_output/student_output.txt
	python verify.py testing/partA.txt student_output/student_output.txt

testASimple:	Mandelbrot
	./MandelFrame 2 1536 5 3 5 2 student_output/student_output.txt
	python verify.py testing/partASimple.txt student_output/student_output.txt

memcheckA:	Mandelbrot
	valgrind --tool=memcheck --leak-check=full --dsymutil=yes --track-origins=yes ./MandelFrame 2 1536 -0.7746806106269039 -0.1374168856037867 1e-5 100 student_output/student_output.txt

testB1Small: colorPalette
	./colorPalette minicolormap.txt student_output 100 50
	python verify.py student_output/colorpaletteP3.ppm testing/B1SmallP3.ppm
	python verify.py student_output/colorpaletteP6.ppm testing/B1SmallP6.ppm

testB1Big: colorPalette
	./colorPalette defaultcolormap.txt student_output 100 1
	python verify.py student_output/colorpaletteP3.ppm testing/B1BigP3.ppm
	python verify.py student_output/colorpaletteP6.ppm testing/B1BigP6.ppm


memcheckB1: colorPalette
	valgrind --tool=memcheck --leak-check=full --dsymutil=yes --track-origins=yes ./colorPalette defaultcolormap.txt student_output 100 1

testB2:  MandelMovie
	./MandelMovie 2 1536 -0.561397233777 -0.643059076016 2 1e-7 5 100 student_output/partB defaultcolormap.txt
	python verify.py testing/testB student_output/partB

memcheckB2: MandelMovie
	valgrind --tool=memcheck --leak-check=full --dsymutil=yes --track-origins=yes ./MandelMovie 2 1536 -0.561397233777 -0.643059076016 2 1e-7 5 100 student_output/partB defaultcolormap.txt

testB2Small:  MandelMovie
	./MandelMovie 2 1536 5 3 8 2 3 2 student_output/testBSmall defaultcolormap.txt
	python verify.py testing/testBSmall student_output/testBSmall

memcheckB2Small: MandelMovie
	valgrind --tool=memcheck --leak-check=full --dsymutil=yes --track-origins=yes ./MandelMovie 2 1536 5 3 8 2 3 2 student_output/testBSmall defaultcolormap.txt

BigTest:  MandelMovie
	printf "WARNING: This is a very big test that could take close to two hours to finish; if you want to have this run in the background try nohup make BigTest to run this in the backround and use top to check progress. Only do this if you are confident in your solution"
	./MandelMovie 2 1536 -0.561397233777 -0.643059076016 2 1e-7 576 400 student_output/BigTest defaultcolormap.txt
	python verify.py testing/BigTest student_output/BigTest

%.o: %.c
	$(CC) -c $< $(CFLAGS)

clean:
	rm -rf *.o
