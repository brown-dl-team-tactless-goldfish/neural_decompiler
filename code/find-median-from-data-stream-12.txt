class MedianFinder {
    priority_queue<int> maxheap;
    priority_queue<int,vector<int>,greater<int>> minheap;
    double med;
    
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(maxheap.empty()){ // agar maxheap empty hai vo phla element hai use push krdo
            maxheap.push(num);
            med = num;
        }else{
            if(maxheap.size() > minheap.size()){
                if(num < med){   // vo maxheap ka hissa hai use vahan daalo 
                    minheap.push(maxheap.top()); // maxheap ka top element ab min heap ka hissa hai
                    maxheap.pop(); // kyunki median se chota element agya hai ek
                    maxheap.push(num); 
                }else{
                    minheap.push(num); // else vo minheap me aega agr vo median jo ki maxheap ka top 
                    // element hai usse bada hai
                }
                med = (maxheap.top() + minheap.top())/2.0;
            }else if(maxheap.size() == minheap.size()){
                if(num < med){
                    maxheap.push(num);   // vo maxheap ka hissa hai kyuki vo median se kamm hai
                    med = maxheap.top();
                }else{
                    minheap.push(num);
                    med = minheap.top();
                }
            }else{ // agr minheap badi hai maxheap se
                if(num > med){
                    maxheap.push(minheap.top());
                    minheap.pop();
                    minheap.push(num);
                }else{
                    maxheap.push(num);
                }
                 med = (maxheap.top() + minheap.top())/2.0;
            }
        }
    }
    
    double findMedian() {
        return med;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */