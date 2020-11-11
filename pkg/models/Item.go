package models

import (
	r "io/ioutil"
	"path/filepath"
)

//Pic holds picture information
type Pic struct {
	Name string
}

//GetItems returns all images found
func GetItems(dir string) ([]Pic, []string, error) {

	items := make([]Pic, 0)
	names := make([]string, 0)

	files, err := r.ReadDir(dir)
	if err != nil {
		return nil, nil, err
	}

	for _, file := range files {
		names = append(names, filepath.Ext(file.Name()))
		if filepath.Ext(file.Name()) == ".jpg" || filepath.Ext(file.Name()) == ".png" || filepath.Ext(file.Name()) == ".gif" {
			items = append(items, Pic{Name: file.Name()})
		}

	}

	return items, names, nil

}
