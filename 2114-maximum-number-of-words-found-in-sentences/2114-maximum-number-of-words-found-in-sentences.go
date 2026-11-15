package main

import "strings"

func mostWordsFound(sentences []string) int {
	previous := 0
	current := 0

	for _, c := range sentences {
		current = len(strings.Fields(c))
		if current > previous {
			previous = current
		}
	}

	return previous
}
