func reverseWords(s string) string {
    word := strings.Fields(s)
    var result strings.Builder
    for i := len(word) - 1; i >= 0; i-- {
      if i == 0 {
          result.WriteString(word[i])
      } else {
          result.WriteString(word[i] + " ")
      }
    }
    return result.String()
}