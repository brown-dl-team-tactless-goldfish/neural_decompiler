typedef struct xypts
{
    int x; 
    int y;
}xypts_t;


bool same(xypts_t* pt1, xypts_t* pt2)
{
    return ((pt1->x == pt2->x) && (pt1->y == pt2->y));
}

bool isBoomerang(int** points, int pointsSize, int* pointsColSize){

    xypts_t pts[3]; 
    for(int i=0; i<pointsSize; i++)
    {
        pts[i].x = points[i][0];
        pts[i].y = points[i][1];
    }
    
    //see if points are distinct
    if(
        (same(&pts[0], &pts[1]) == false) &&
        (same(&pts[0], &pts[2]) == false) &&
        (same(&pts[1], &pts[2]) == false)
      )
    {
        /*Area of triangle = |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|*/
        
        int a = (pts[0].x*(pts[1].y - pts[2].y));
        int b = (pts[1].x*(pts[2].y - pts[0].y));
        int c = (pts[2].x*(pts[0].y - pts[1].y));
        
        int area =  a + b + c; 
        
        if (area == 0)
        {
            return false; 
        }
        return true; 
    }
    return false;
}