package models

//Company holds company related information
type Company struct {
	Title      string
	Subscribed bool
	Places     []string
}

// NewCompany creates a new instance of company
func NewCompany(title string, subscribed bool, places ...string) *Company {
	return &Company{
		Title:      title,
		Subscribed: subscribed,
		Places:     places,
	}
}
