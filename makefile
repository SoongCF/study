test : test.o
	gcc -o test test.o

test.o:test.c
	gcc -c test.c

.PHONY: clean
clean:
	-rm -f test *.o


