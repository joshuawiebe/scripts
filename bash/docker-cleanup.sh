#!/usr/bin/env bash
# File: bash/docker-cleanup.sh
# Usage: ./docker-cleanup.sh [--volumes]
# By default prunes containers, images, and networks. Volumes if --volumes flag is given.

PRUNE_CMD="docker system prune -f"
if [[ "$1" == "--volumes" ]]; then
  PRUNE_CMD+=" --volumes"
fi

echo "Running: $PRUNE_CMD"
$PRUNE_CMD
echo "Docker cleanup complete."
