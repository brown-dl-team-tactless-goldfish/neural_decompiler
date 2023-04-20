class LFUCache {
    // inorder to "get" in O(1) time, we need an unordered_map<int, int>
    // inorder to implement "LRU", we need a linked list, which stores 'frequency' for later use
    // inorder to implement "LFU", we need a map structure that maps frequency to the first list node that has that frequency
    // when we need to evict someone, just evict the last one in the list, but may need to update the frequency map
    unordered_map<int, int> key_val_map;
    unordered_map<int, int> key_freq_map;
    unordered_map<int, list<int>::iterator> key_list_map;
    unordered_map<int, list<int>::iterator> frequency_map;
    list<int> queue;    // stores the keys
    int _capacity;
    
    void update(int key, int freq) {
        if (frequency_map.find(freq + 1) == frequency_map.end()) {
            // there was no this frequency, we should insert it in front of the frequency_map[freq]
            frequency_map[freq+1] = queue.insert(frequency_map[freq], key);
        }
        else {
            // there was this frequency, insert it in front of the frequency_map[freq+1]
            frequency_map[freq+1] = queue.insert(frequency_map[freq+1], key);
        }
        // delete the old one, may need to update frequency_map
        if (*(frequency_map[freq]) == key) {
            auto iter = frequency_map[freq];
            iter++;
            if (iter != queue.end() && key_freq_map[*iter] == freq)
                frequency_map[freq] = iter;
            else 
                frequency_map.erase(freq);
        }
        queue.erase(key_list_map[key]);
        key_list_map[key] = frequency_map[freq+1];
    }
    
    void deleteLFU() {
        int del_key = queue.back();
        int del_freq = key_freq_map[del_key];
        if (key_list_map[del_key] == frequency_map[del_freq])
            frequency_map.erase(del_freq);
        queue.pop_back();
        key_val_map.erase(del_key);
        key_freq_map.erase(del_key);
    }
    
public:
    LFUCache(int capacity) {
        _capacity = capacity;
    }
    
    int get(int key) {
        auto it = key_val_map.find(key);
        if (it != key_val_map.end()) {
            // change the frequency and move it to the front of nodes that have that frequency
            int freq = key_freq_map[key]++;
            update(key, freq);
            return key_val_map[key];
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (_capacity <= 0)
            return;
        auto it = key_val_map.find(key);
        if (it == key_val_map.end()) {
            // insert a new key, may need to evict old entry
            if (queue.size() == _capacity) {
                deleteLFU();
            }
            key_val_map[key] = value;
            key_freq_map[key] = 1;
            auto iter = frequency_map.find(1) == frequency_map.end() ? queue.end() : frequency_map[1];
            frequency_map[1] = queue.insert(iter, key);
            key_list_map[key] = frequency_map[1];
        }
        else {
            key_val_map[key] = value;
            int freq = key_freq_map[key]++;
            update(key, freq);
        }
    }
};