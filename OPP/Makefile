

OBJ = main.o opp.o
CC  = gcc
OUT = a.out

$(OUT): $(OBJ)
	$(CC) -o $(OUT) $(OBJ)

main.o: main.c opp.o

opp.o : opp.c


clean:
	rm $(OBJ) $(OUT) -rf
