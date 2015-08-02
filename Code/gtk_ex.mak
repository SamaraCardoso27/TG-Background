TARGET=gtk_ex

FTRSCANL_DLIB=./libScanAPI.so

CC=gcc

# GTK 2.0+
LDLIBS=`pkg-config --libs gtk+-2.0 gthread-2.0` -lstdc++
CFLAGS=-Wall -D_UNIX -I./ `pkg-config --cflags gtk+-2.0 gthread-2.0`       

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(CC) $(TARGET).o -o $(TARGET) -I./ $(FTRSCANL_DLIB)  $(LDLIBS)

$(TARGET).o: $(TARGET).c
	$(CC) -c $(TARGET).c $(CFLAGS)

clean:
	rm -f $(TARGET)
	rm -f $(TARGET).o
