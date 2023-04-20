
var TimeLimitedCache = function() {
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    

    if(this.keys == undefined){
        this.keys = [key];
    }else{
        if(this.keys.includes(key)){

        }else{
            let arr = this.keys;
            arr.push(key);
            this.keys = arr;
        }
      //  console.log(this.keys)
    }

    if(this[key]){
        clearTimeout(this[key].timeoutid);
        if(this[key].value!=undefined){
            this[key] = {
            value:value,
             expireAt :function(){
                 let localid = setTimeout(()=>{
                     this.value = undefined;
                 },duration);
                 return localid;
             },
             isExpired:false,
         }
         this[key].timeoutid = this[key].expireAt();
        }
       // console.log('ket after exists '+key, ' ',value,' ',this[key],' ',Date.now())

        return true;
    }
    this[key] = {
        value:value,
        isExpired:false,
        expireAt :function(){
                 let localid = setTimeout(()=>{
                     this.value = undefined;
                 },duration)
                 return localid;
             },
    }
    this[key].timeoutid = this[key].expireAt();
    return false

};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    
    if(this[key]){
        if(this[key].value == undefined){    
            return -1;
        }
        return this[key].value;
    }
    return -1;

};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let c = 0;
       this.keys.forEach((x,index)=>{
           if(this[x].value!=undefined){
               c++;
           }
        })
        return c;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */