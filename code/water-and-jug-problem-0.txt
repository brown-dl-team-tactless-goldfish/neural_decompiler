int gcd(int x, int y){
    if(y == 0)
        return x ;
    return gcd(y, x% y) ;
}
bool canMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity){
    if(targetCapacity == 0)
        return true ;
    int g = gcd(jug1Capacity, jug2Capacity) ;
    
    return (jug1Capacity + jug2Capacity >= targetCapacity) && (targetCapacity%g == 0) ;
}