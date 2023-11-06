package app

import (
	"application/db"
	"fmt"
	// "io"
	"net/url"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

var (
	icon, _ = fyne.LoadResourceFromPath("images/icon.png")
	//size = fyne.NewSize(500, 400)
	img = canvas.NewImageFromFile("images/w.jpg")
)

func (h *Handler) MainWindow() (fyne.Window, error) {
	w := h.a.NewWindow("Центр Терапевтической Офтальмологии")
	w.SetIcon(icon)
	
	url, err := url.Parse("https://oftal.ru/")
	if err != nil {
		return nil, err
	}
	
	link := widget.NewHyperlinkWithStyle("Посетить сайт", url, fyne.TextAlignCenter, fyne.TextStyle{Bold: true})
	w.SetContent(container.New(layout.NewGridLayout(3),
		img, img, img, 
		img, canvas.NewImageFromFile("images/logo.png"), img,
		img, widget.NewLabelWithStyle("Интеллектуальная система\nраспознавания наличия\nпатологии состояния\nмикроциркуляции человека", fyne.TextAlignCenter, fyne.TextStyle{Bold: true}), img, 
		img, widget.NewButton("Войти", func() {
			w.Close()
			h.Authentication()
		}), img,
		img, link, img))


	return w, nil
}

func (h *Handler) Authentication() {
	w := h.a.NewWindow("Вход в систему")
	w.SetIcon(icon)
	w.Resize(fyne.NewSize(300, 200))

	login, password := widget.NewEntry(), widget.NewPasswordEntry()
	label1, label2 := widget.NewLabel("Введите логин:"), widget.NewLabel("Введите пароль:")
	label1.Alignment, label2.Alignment = fyne.TextAlignCenter, fyne.TextAlignCenter
	w.SetContent(container.NewVBox(
		label1,
		login,
		label2,
		password,
		widget.NewButton("Войти", func() {
			ok, err := h.CheckUser(db.User{
				Login: login.Text,
				Password: password.Text,
			})

			if err != nil || !ok {
				
				if err := h.Classification(); err != nil {
					fmt.Print(err)
				}
				// dialog.ShowInformation("Вас нет в системе!", "Отказано в доступе", w)
			} else {
				h.Classification()
			}
		}),
	))

	w.Show()
}

func (h *Handler) Classification() error {
	w := h.a.NewWindow("Классификация")
	w.SetIcon(icon)
	btn := widget.NewButton("Выбрать", func() {
		dialog.NewFileSave(func(uc fyne.URIWriteCloser, err error) {
			// data, _ := io.ReadAll(uc)
			// fmt.Println(data)
		}, w)})
	w.SetContent(container.NewGridWithColumns(3,
		img, widget.NewLabelWithStyle("Выберите изображение:", fyne.TextAlignCenter, fyne.TextStyle{}), img,
		img, btn, img,
	))
	w.Show()

	return nil
}
