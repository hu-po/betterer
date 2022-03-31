package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (rot13 rot13Reader) Read(b []byte) (x int, err error) {
	x, err = rot13.r.Read(b)
	for i := 0; i < x; i++ {
		switch {
			case b[i] >= 'A' && b[i] <= 'M':
				b[i] += 13
			case b[i] >= 'a' && b[i] <= 'm':
				b[i] += 13
			default:
				b[i] -= 13
		}
	}
	return x, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
