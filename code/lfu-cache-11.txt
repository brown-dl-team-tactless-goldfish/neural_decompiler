class LFUCache {
public:
	// Data structure: 
    // 1. A hashmap that map frequence to a doubly linked list, the list stores <key, value> pair and recently used order
    // 2. A hashmap that map key to <freq, list iterator> pair
    unordered_map<int, list<pair<int, int>>> freqs;
    unordered_map<int, pair<int, list<pair<int, int>>::iterator>> keys;
	
    int capacity;
    int minFreq;
    
    LFUCache(int capacity) : capacity(capacity), minFreq(0) {
    }
    
    int get(int key) {
        if (keys.count(key)) {
            // Get value 
            int freq = keys[key].first;
            auto it = keys[key].second;
            int value = it->second;
            
			// Update frequency and maintain least recently used order
            freqs[freq].erase(it);
            freqs[freq+1].push_back({key, value});
            
            keys[key].first = freq+1;
            keys[key].second = --freqs[freq+1].end();
            
			// Update minFreq
            if (freqs[minFreq].size() == 0) {
                minFreq++;
            }
            
            return value;
            
        } else {
            return -1;
        }
    }
    
    void put(int key, int value) {
        if (capacity <= 0) return;
        
        if (get(key) != -1) {
            // Update value. 
			// Note: frequency is already updated in get() function call last line.
            auto it = keys[key].second;
            it->second = value;
            
        } else {
            if (keys.size() == capacity) {
                // remove least frequently and least recently used key
                auto it = freqs[minFreq].begin();
                int removeKey = it->first;
                freqs[minFreq].erase(it);
                
                keys.erase(removeKey);
            }
            
            minFreq = 1;
            freqs[minFreq].push_back({key, value});
            
            keys[key].first = minFreq;
            keys[key].second = --freqs[minFreq].end();
            
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */