package main

import (
	"context"
	"fmt"
	"os"

	"github.com/jackc/pgx/v4/pgxpool"
	log "github.com/sirupsen/logrus"

	"application/app"
	"application/db"
)

func main() {
	dsn := fmt.Sprintf("postgresql://%s:%s@%s:%s/%s", "postgres", "3ja6mz80q", "localhost", "5432", "postgres")
	dbc, err := pgxpool.Connect(context.Background(), dsn)
	if err != nil {
		log.WithError(err).Error("failed connect to database")
		os.Exit(1)
	}

	query := db.New(dbc)
	h := app.New(query)
	h.Start()
}
