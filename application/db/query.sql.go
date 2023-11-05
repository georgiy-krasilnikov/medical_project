// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.20.0
// source: query.sql

package db

import (
	"context"
)

const getTestImagesFromLimb = `-- name: GetTestImagesFromLimb :many
SELECT img FROM limb_test
WHERE info = $1
`

func (q *Queries) GetTestImagesFromLimb(ctx context.Context, info string) ([][]byte, error) {
	rows, err := q.db.Query(ctx, getTestImagesFromLimb, info)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items [][]byte
	for rows.Next() {
		var img []byte
		if err := rows.Scan(&img); err != nil {
			return nil, err
		}
		items = append(items, img)
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getTestImagesFromPerelimb = `-- name: GetTestImagesFromPerelimb :many
SELECT img FROM perelimb_test
WHERE info = $1
`

func (q *Queries) GetTestImagesFromPerelimb(ctx context.Context, info string) ([][]byte, error) {
	rows, err := q.db.Query(ctx, getTestImagesFromPerelimb, info)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items [][]byte
	for rows.Next() {
		var img []byte
		if err := rows.Scan(&img); err != nil {
			return nil, err
		}
		items = append(items, img)
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getTrainImagesFromLimb = `-- name: GetTrainImagesFromLimb :many
SELECT img FROM limb_train
WHERE info = $1
`

func (q *Queries) GetTrainImagesFromLimb(ctx context.Context, info string) ([][]byte, error) {
	rows, err := q.db.Query(ctx, getTrainImagesFromLimb, info)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items [][]byte
	for rows.Next() {
		var img []byte
		if err := rows.Scan(&img); err != nil {
			return nil, err
		}
		items = append(items, img)
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getTrainImagesFromPerelimb = `-- name: GetTrainImagesFromPerelimb :many
SELECT img FROM perelimb_train
WHERE info = $1
`

func (q *Queries) GetTrainImagesFromPerelimb(ctx context.Context, info string) ([][]byte, error) {
	rows, err := q.db.Query(ctx, getTrainImagesFromPerelimb, info)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items [][]byte
	for rows.Next() {
		var img []byte
		if err := rows.Scan(&img); err != nil {
			return nil, err
		}
		items = append(items, img)
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getUsers = `-- name: GetUsers :many
SELECT id, login, password FROM users
`

func (q *Queries) GetUsers(ctx context.Context) ([]User, error) {
	rows, err := q.db.Query(ctx, getUsers)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items []User
	for rows.Next() {
		var i User
		if err := rows.Scan(&i.ID, &i.Login, &i.Password); err != nil {
			return nil, err
		}
		items = append(items, i)
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const inputTestImagesToLimb = `-- name: InputTestImagesToLimb :exec
INSERT INTO limb_test (
    img, info
) VALUES (
  $1, $2
)
`

type InputTestImagesToLimbParams struct {
	Img  []byte
	Info string
}

func (q *Queries) InputTestImagesToLimb(ctx context.Context, arg InputTestImagesToLimbParams) error {
	_, err := q.db.Exec(ctx, inputTestImagesToLimb, arg.Img, arg.Info)
	return err
}

const inputTestImagesToPerelimb = `-- name: InputTestImagesToPerelimb :exec
INSERT INTO perelimb_test (
    img, info
) VALUES (
  $1, $2
)
`

type InputTestImagesToPerelimbParams struct {
	Img  []byte
	Info string
}

func (q *Queries) InputTestImagesToPerelimb(ctx context.Context, arg InputTestImagesToPerelimbParams) error {
	_, err := q.db.Exec(ctx, inputTestImagesToPerelimb, arg.Img, arg.Info)
	return err
}

const inputTrainImagesToLimb = `-- name: InputTrainImagesToLimb :exec
INSERT INTO limb_train (
    img, info
) VALUES (
  $1, $2
)
`

type InputTrainImagesToLimbParams struct {
	Img  []byte
	Info string
}

func (q *Queries) InputTrainImagesToLimb(ctx context.Context, arg InputTrainImagesToLimbParams) error {
	_, err := q.db.Exec(ctx, inputTrainImagesToLimb, arg.Img, arg.Info)
	return err
}

const inputTrainImagesToPerelimb = `-- name: InputTrainImagesToPerelimb :exec
INSERT INTO perelimb_train (
    img, info
) VALUES (
  $1, $2
)
`

type InputTrainImagesToPerelimbParams struct {
	Img  []byte
	Info string
}

func (q *Queries) InputTrainImagesToPerelimb(ctx context.Context, arg InputTrainImagesToPerelimbParams) error {
	_, err := q.db.Exec(ctx, inputTrainImagesToPerelimb, arg.Img, arg.Info)
	return err
}
