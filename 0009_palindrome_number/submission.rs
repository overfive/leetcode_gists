impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if(x < 0) {
            return false
        } else {
            let mut cn = x;
            let mut t = 0;
            while cn > 0 {
                t = t * 10 + cn - (cn/10) * 10;
                cn = cn/10;
            }
            return t==x
        }
    }
}
