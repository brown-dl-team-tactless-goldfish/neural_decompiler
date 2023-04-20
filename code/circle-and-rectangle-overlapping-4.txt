

bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2){
    int xParam = xCenter;
    int yParam = yCenter;
    
    if(xCenter<=x1){
        xParam = x1;
    }
    else if(xCenter>=x2){
        xParam = x2;
    }
    else{
        xParam = xCenter;
    }
    if(yCenter<=y1){
        yParam = y1;
    }
    else if(yCenter>=y2){
        yParam = y2;
    }
    else{
        yParam = yCenter;
    }
    
    int xDistance = xCenter-xParam;
    int yDistance = yCenter-yParam;
    
    int total = sqrt((xDistance*xDistance) + (yDistance*yDistance));
    
    return total<=radius;
    
}