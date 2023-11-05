package app

import (
	"context"

	"application/db"
)

func (h *Handler) CheckUser(u db.User) (bool, error) {
	users, err := h.q.GetUsers(context.Background())
	if err != nil {
		return false, err
	}

	for _, user := range users {
		if user.Login == u.Login && user.Password == u.Password {
			return true, nil
		} 
	}

	return false, nil
}