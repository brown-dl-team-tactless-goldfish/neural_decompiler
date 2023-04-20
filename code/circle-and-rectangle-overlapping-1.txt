bool checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2){
    int tx = x_center;
    int ty = y_center;
    
    
    if(x_center<x1) tx = x1; // left
    else if(x_center>x2) tx = x2; //right
    else tx = x_center; // between y1 and y2
    if(y_center<y1) ty = y1; //bottom
    else if(y_center>y2) ty = y2; //top
    else ty = y_center; //between x1 and x2
    
    
    int disx = x_center - tx;  
    int disy = y_center - ty;
    int distance = sqrt((disx * disx) + (disy * disy)); //distance formula
    
    
    return distance <= radius;
}