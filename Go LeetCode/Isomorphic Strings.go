func isIsomorphic(s string, t string) bool {
    table := make(map[byte]byte)
    unique := make(map[byte]bool)
    for i := 0; i < len(s); i++ {
        if _, ex := unique[t[i]]; ex {
            table[s[i]] = t[i]
            unique[t[i]] = true
            continue
        } else {
            if table[s[i]] == t[i]{
                continue
                } else {return false}
    }
    return true
}