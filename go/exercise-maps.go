package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	word_count := make(map[string]int)
	for _, word := range strings.Fields(s) {
		_, ok := word_count[word]
		switch {
			case ok:
				word_count[word] += 1
			default:
				word_count[word] = 1
		}
	}
	return word_count
}

func main() {
	wc.Test(WordCount)
}
