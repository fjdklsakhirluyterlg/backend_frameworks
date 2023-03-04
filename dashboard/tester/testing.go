package main

import "fmt"

func main(){
	servers := [...]string{"http://127.0.0.1:5080"}

	for i, val := range servers{
		fmt.Println(i, val)
	}
}