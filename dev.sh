cleanup() {
  echo "Stopping and cleaning images..."
  docker compose down --rmi local
}

trap cleanup INT TERM EXIT

docker compose up server client