package main

func isValid(s string) bool {
	stack := []rune{}

	for _, c := range s {
		switch c {
		case '(':
			stack = append(stack, ')')
		case '{':
			stack = append(stack, '}')
		case '[':
			stack = append(stack, ']')
		default:
			// Check if stack is empty or if the top element doesn't match
			if len(stack) == 0 || stack[len(stack)-1] != c {
				return false
			}
			// Pop the top element from the stack
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
