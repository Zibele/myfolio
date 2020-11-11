package main

import (
	"net/http"
)

func main() {
	fs := http.FileServer(http.Dir("../../ui/static/"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))
	http.HandleFunc("/", HomeHandler)
	http.HandleFunc("/Items", ItemsHandler)
	http.ListenAndServe("localhost:8080", nil)
}
