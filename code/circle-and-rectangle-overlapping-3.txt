// this program checks if circle and rectangle over lap ( share at least 1 point in an X Y system)
//x_center , y_center - circle cords, x1,y1 - left most lowest most point rectangle points
// x2,y2 - right most highest cords of the rectangle
bool checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2){
// first we check if center of the cirlce is inside the rectangle if so we return true(clearly they share points)
    if((x_center>= x1 && x_center<=x2) && (y_center>=y1 && y_center<=y2) ) return true;
    // there are cases where the center of the cirlce is not inside the rectangle and 
	//still share points
    // we need to check these cases and return the right answer!
    
    // center of circle is left from rectangle but in rectangle Y axis range of(y1,y2)
    else if(x_center<x1 && (y_center>=y1 && y_center<=y2)) { 
        if((x_center+radius)>=x1) return true;
    }
    // center of circle is right from rectangle but in rectangle Y axis range of(y1,y2)
    else if(x_center >x2 && (y_center>=y1 && y_center<=y2)) { 
        if((x_center-radius)<=x2) return true;
    }
    // center of circle is below lowest points in rectangle but in between X1 and X2 AIXS
    else if(y_center < y1 && (x_center>=x1 && x_center<=x2)) {
        if((y_center+radius) >= y1) return true;
    }
    // center of circle is above highest points in rectangle but in between X1 and X2 AIXS
    else if(y_center > y2 && (x_center >= x1 && x_center<=x2)) {
        if((y_center-radius)<=y2) return true;
    }
    // center of circle is below and right side of the rectangle
    // we check if the radius can reach the right most and low most point of the rectangle if so 
	//then they share at least 1 point if its equal to radius and if the radius is even bigger it 
	//may have many points
    else if(x_center>x2 && (y_center<y1)) {
        double Pythagorean = pow(x_center-x2,2) + pow(y1-y_center,2);
        Pythagorean = sqrt(Pythagorean);
        printf("%lf %d",Pythagorean,radius);
        if(Pythagorean<=radius) return true; 
    }
    // Center of circle is above  the right most and top most cord of the rectangle ( x2,y2) and also right of 
	//the rectangle
    // we check if the radius can reach the right most and top most cord of the rectangle(x2,y2) if so
	//they share at least 1 point if not more(if the radius is even bigger)
    else if(x_center>x2 && (y_center>y2)) {
        double Pythagorean = pow(x_center-x2,2) + pow(y_center-y2,2);
        Pythagorean = sqrt(Pythagorean);
        printf("%lf %d",Pythagorean,radius);
        if(Pythagorean<=radius) return true; 
    }
    // center of circle is above and also to th eleft of the top most left most cord 
	//in the rectangle we need to check if its radius can reach that point or 
	//if the radius is even bigger in that case it may share more than 1 point with the rectangle
    else if(x_center<x1 && (y_center > y2)) {
        double Pythagorean = pow(x_center-x1,2) + pow(y_center-y2,2);
        Pythagorean = sqrt(Pythagorean);
        printf("%lf %d",Pythagorean,radius);
        if(Pythagorean<=radius) return true; 
    }
    // center of circle is below and left to the lowest and left most point of the rectangle (x1,y1)
    // we need to check if its radius can reach that point or if the radius can reach even more in 
	//that case it  will share more than one point
    else if(x_center<x1 && y_center<y1) {
        double Pythagorean = pow(x1-x_center,2) + pow(y1-y_center,2);
        Pythagorean = sqrt(Pythagorean);
        printf("%lf %d",Pythagorean,radius);
        if(Pythagorean<=radius) return true; 
    }
    return false;
}