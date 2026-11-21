func islandPerimeter(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    perimeter := 0

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1 {
                // Check Up
                if r == 0 || grid[r-1][c] == 0 {
                    perimeter++
                }
                // Check Down
                if r == rows-1 || grid[r+1][c] == 0 {
                    perimeter++
                }
                // Check Left
                if c == 0 || grid[r][c-1] == 0 {
                    perimeter++
                }
                // Check Right
                if c == cols-1 || grid[r][c+1] == 0 {
                    perimeter++
                }
            }
        }
    }

    return perimeter
}
