func gcdOfStrings(str1 string, str2 string) string {
    if str1+str2 != str2+str1{
        return ""
    }
    //  
    gcdlength := gcd(len(str2), len(str1))
    return str1[:gcdlength]
}

func gcd(a, b int) int{
    for b != 0{
        a, b = b, a%b
    }
    return a
}