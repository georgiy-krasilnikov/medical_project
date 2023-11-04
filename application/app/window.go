package app

import (
	"net/url"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

var (
	icon, _ = fyne.LoadResourceFromPath("images/icon.png")
	size = fyne.NewSize(800, 600)
	img = canvas.NewImageFromFile("images/w.jpg")
)

func (h *Handler) MainWindow() (fyne.Window, error) {
	w := h.a.NewWindow("Центр Терапевтической Офтальмологии")
	w.SetIcon(icon)
	w.Resize(size)

	
	text := widget.NewLabel("Интеллектуальная система распознавания\nналичия патологии состояния\nмикроциркуляции человека")
	text.Alignment = fyne.TextAlignCenter
	text.TextStyle = fyne.TextStyle{Bold: true}

	url, err := url.Parse("https://oftal.ru/")
	if err != nil {
		return nil, err
	}

	link := widget.NewHyperlinkWithStyle("Посетить сайт", url, fyne.TextAlignCenter, fyne.TextStyle{Bold: true})
	
	w.SetContent(container.NewGridWithColumns(3,
		img, img, img, 
		img, canvas.NewImageFromFile("images/logo.png"), img,
		img, text, img, 
		img, widget.NewButton("Войти", func() {
			w.Close()
			h.Authentication()
		}), img,
		img, link, img))


	return w, nil
}

func (h *Handler) Authentication() (fyne.Window, error) {
	w := h.a.NewWindow("Вход в систему")
	w.SetIcon(icon)
	w.Resize(fyne.NewSize(300, 300))

	login, password := widget.NewEntry(), widget.NewPasswordEntry()
	label1, label2 := widget.NewLabel("Введите логин:"), widget.NewLabel("Введите пароль:")
	label1.Alignment, label2.Alignment = fyne.TextAlignCenter, fyne.TextAlignCenter
	w.SetContent(container.NewVBox(
		label1,
		login,
		label2,
		password,
		),
	)

	w.Show()


	return nil, nil
}

