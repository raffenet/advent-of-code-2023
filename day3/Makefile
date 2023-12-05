CFLAGS=-Wall -fsanitize=address -g -O1 -fno-omit-frame-pointer

all: day3 day3-2 run

day3: day3.c

day3-2: day3-2.c

run: day3 day3-2
	-./day3
	-./day3-2

clean:
	-rm -rf *.dSYM day1
