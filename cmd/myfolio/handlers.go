package main

import (
	"bytes"
	"html/template"
	"log"
	h "net/http"
	"os"
	"path/filepath"
	"time"

	"github.com/Zibele/myfolio/pkg/models"
)

const (
	pagesPath     = "C:/Users/Zibele/Desktop/goprojects/github.com/Zibele/myfolio/web/static/public"
	resourcesPath = "C:/Users/Zibele/Desktop/goprojects/github.com/Zibele/myfolio/web/resources"
)

var (
	homeTemp = template.Must(template.ParseFiles("../../ui/html/home.html", "../../ui/html/base.html"))

	//gouserTemp = template.Must(template.Parse(filepath.join(path, "user.html")))
)

//HomeHandler writes to homepage request
func HomeHandler(w h.ResponseWriter, r *h.Request) {
	var b bytes.Buffer
	err := homeTemp.ExecuteTemplate(&b, "home.html", &models.Portfolio{Author: models.Author{Name: "Zibele", Profession: "Fullstack Software Developer"}})
	if err != nil {
		log.Fatal(err)
	}
	b.WriteTo(w)
}

//ItemsHandler basic functional handler test
func ItemsHandler(writer h.ResponseWriter, r *h.Request) {
	funcMap := template.FuncMap{"fdate": formatDate, "joinPath": filepath.Join, "wD": workingDirectory}
	templ := template.New("items.html").Funcs(funcMap)
	templ, err := templ.ParseFiles("../../ui/html/items.html", "../../ui/html/base.html")
	if err != nil {
		log.Fatal(err)
	}
	items, names, err := models.GetItems("../../ui/static/img/")
	if err != nil {
		log.Fatal(err)
	}
	templ.Execute(writer, &DataStruct{Items: items, Names: names, Size: len(items)})
}

func formatDate(d time.Time, format string) string {
	return d.Format(format)
}

func workingDirectory() string {
	path, err := os.Getwd()
	if err != nil {
		log.Println(err)
	}
	return path
}

//DataStruct stores date layout
type DataStruct struct {
	Items []models.Pic
	Names []string
	Size  int
}
