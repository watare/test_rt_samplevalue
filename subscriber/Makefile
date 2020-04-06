
CC=gcc
CFLAGS=-Wall -O -pthread -lm
LDFLAGS=-static
LIBPATH = -L../libiec61850-1.3.3/build/
LIB = -liec61850
EXEC = sv_subscriber
#EXEC = goose_publisher
INCLUDE = -I../inc

all: $(EXEC)
$(EXEC): src/sv_subscriber_v2.c
#$(EXEC): src/sv_subscriber_phasor_extract.c
			$(CC) $(INCLUDE)  src/sv_subscriber_v2.c -o $(EXEC) $(CFLAGS) $(LIBPATH) $(LIB)
#			$(CC) $(INCLUDE) src/sv_subscriber_phasor_extract.c -o $(EXEC) $(CFLAGS) $(LIBPATH) $(LIB)


#only goose publisher

#$(EXEC): src/goose_publisher.c
#				$(CC) $(INCLUDE)  src/goose_publisher.c -o $(EXEC) $(CFLAGS) $(LIBPATH) $(LIB)

clean:
	rm  -rf obj/



