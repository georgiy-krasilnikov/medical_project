package app

import (
	"context"
	"fmt"
	"os"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"

	"application/db"
)

type Handler struct {
	a fyne.App
	q *db.Queries
}

func New(q *db.Queries) *Handler {
	return &Handler{
		a: app.New(),
		q: q,
	}
}

func (h *Handler) Start() error {
	w, err := h.MainWindow()
	if err != nil {
		return err
	}
	w.ShowAndRun()
	return nil
}

func (h *Handler) LoadImagesToDB(ctx context.Context, dirName string) error {
	dir, err := os.ReadDir(dirName)
	if err != nil {
		return err
	}

	for _, file := range dir {
		b, err := os.ReadFile(dirName+"/"+file.Name())
		if err != nil {
			return err
		}

		s := strings.SplitAfterN(file.Name(), ".", 2)[0]

		if err:= h.q.InputTestImagesToPerelimb(ctx, db.InputTestImagesToPerelimbParams{
			Img: b,
			Info: s[:len(s)-1],
		}); err != nil {
			return err
		}
	}
	
	return nil
}

// func (h *Handler) InputTestImagesToLimb(ctx context.Context, dirName string) error {
// 	dir, err := os.ReadDir(dirName)
// 	if 
// 	b, err := os.ReadFile("app/"+fileName)
// 	if err != nil {
// 		return err
// 	}

// 	if err:= h.q.InputTestImagesToLimb(ctx, db.InputTestImagesToLimbParams{
// 		Img: b,
// 		Info: "bolen",
// 	}); err != nil {
// 		return err
// 	}
// 	return nil
// }

func (h *Handler) GetImages(ctx context.Context) error {
	img, err := h.q.GetTestImagesFromLimb(ctx, "bolen")
	if err != nil {
		return err
	}

	f, err := os.Create("file.bmp") //Создаём пустой png
  	if err != nil {
    	fmt.Println(err)
  	}

  	f.Write(img[0]) //Записываем байты
  	f.Close() //Закрываем файл

	return nil
}


