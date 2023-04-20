function createCounter(n: number): () => number {
    let c = n;
    return function () {
        let ret = c;
        c = ++c;
        return ret;
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */