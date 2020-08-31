impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut cn = 0;
        if (x < 0) {
            cn = -x;
        } else {
            cn = x;
        }
        let mut t = 0;
        while cn > 0 {
            let dt = cn - (cn/10) * 10;
            if (2147483647 - dt) / 10 < t{
                return 0;
            }
            t = t * 10 + dt;
            cn = cn/10;
        }
        if (x < 0){
            return -t
        } else {
            return t
        }
    }
}
