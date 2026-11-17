func sumOfMultiples(n int) int {
	sumDivisibleBy := func(k int) int {
		m := n / k
		return k * m * (m + 1) / 2
	}

	return sumDivisibleBy(3) + sumDivisibleBy(5) + sumDivisibleBy(7) -
		sumDivisibleBy(15) - sumDivisibleBy(21) - sumDivisibleBy(35) +
		sumDivisibleBy(105)
}
