package main

import (
	"fmt"
	"golang.org/x/tour/tree"
)

func Walk(t *tree.Tree, ch chan int) {
	if t.Left != nil {
		Walk(t.Left, ch)
	}
	ch <- t.Value
	if t.Right != nil {
		Walk(t.Right, ch)
	}
}

func Same(t1, t2 *tree.Tree) bool {
	ch1 := make(chan int)
	ch2 := make(chan int)

	defer close(ch1)
	defer close(ch2)

	go Walk(t1, ch1)
	go Walk(t2, ch2)

	for i := 0; i < 10; i++ {
		v1, ok1 := <-ch1
		v2, ok2 := <-ch2
		switch {
		case !ok1:
			return false
		case !ok2:
			return false
		case v1 != v2:
			return false
		}
	}

	return true
}

func main() {
	
	// Test Walk
	ch := make(chan int, 10)
	Walk(tree.New(1), ch)
	for v := range ch {
		fmt.Printf("%v,",v)	
	}
	//close(ch)
	fmt.Println("")
	
	// Test Same
	fmt.Printf("true = %v\n", Same(tree.New(1), tree.New(1)))
	fmt.Printf("false = %v\n", Same(tree.New(1), tree.New(2)))
}
