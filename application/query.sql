-- name: GetTrainImagesFromLimb :many
SELECT img FROM limb_train
WHERE info = $1;

-- name: GetTestImagesFromLimb :many
SELECT img FROM limb_test
WHERE info = $1;

-- name: GetTrainImagesFromPerelimb :many
SELECT img FROM perelimb_train
WHERE info = $1;

-- name: GetTestImagesFromPerelimb :many
SELECT img FROM perelimb_test
WHERE info = $1;

-- name: InputTrainImagesToLimb :exec
INSERT INTO limb_train (
    img, info
) VALUES (
  $1, $2
);

-- name: InputTestImagesToLimb :exec
INSERT INTO limb_test (
    img, info
) VALUES (
  $1, $2
);

-- name: InputTrainImagesToPerelimb :exec
INSERT INTO perelimb_train (
    img, info
) VALUES (
  $1, $2
);

-- name: InputTestImagesToPerelimb :exec
INSERT INTO perelimb_test (
    img, info
) VALUES (
  $1, $2
);

