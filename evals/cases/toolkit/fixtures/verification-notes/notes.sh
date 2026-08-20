#!/bin/sh
set -eu

if [ -z "${NOTES_DATA_DIR:-}" ]; then
  printf '%s\n' 'NOTES_DATA_DIR is required' >&2
  exit 2
fi

case "${1:-}" in
  doctor)
    test -d "$NOTES_DATA_DIR"
    test -w "$NOTES_DATA_DIR"
    printf 'ready:%s\n' "$NOTES_DATA_DIR"
    ;;
  create)
    test "$#" -eq 3
    mkdir -p "$NOTES_DATA_DIR"
    printf '%s\t%s\n' "$2" "$3" >> "$NOTES_DATA_DIR/notes.tsv"
    printf 'created:%s\n' "$2"
    ;;
  list)
    if [ -f "$NOTES_DATA_DIR/notes.tsv" ]; then
      cat "$NOTES_DATA_DIR/notes.tsv"
    fi
    ;;
  *)
    printf '%s\n' 'usage: notes.sh doctor | create <title> <body> | list' >&2
    exit 2
    ;;
esac
