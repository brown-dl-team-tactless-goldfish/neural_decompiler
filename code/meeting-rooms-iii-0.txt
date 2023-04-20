int comp(const int** a, const int** b){
    return (*(int**)a)[0] - (*(int**)b)[0];
}

int mostBooked(int n, int** meetings, int meetingsSize, int* meetingsColSize){
    qsort(meetings,meetingsSize,sizeof(int*),comp);
    const number = n;
    long long used_time[number];
    int used_count[number];
    int meet_point = 0;
    for (int i = 0 ; i < n ; i++){
        used_time[i] = 0;
        used_count[i] = 0;
    }
    int room_num;
    while (meet_point < meetingsSize){
        long long fast = LONG_MAX;
        for (int i = 0 ; i < n ; i++){
            if (used_time[i] <= meetings[meet_point][0]){
                used_time[i] = meetings[meet_point][0];
                room_num = i;
                break;
            }
            if (fast > used_time[i]){
                fast = used_time[i];
                room_num = i;
            }
        }
        used_time[room_num] += meetings[meet_point][1] - meetings[meet_point][0];
        used_count[room_num]++;
        meet_point++;
    }
    
    int max = 0;
    int ans = 0;
    for (int i = 0 ; i < n ; i++){
        if (max < used_count[i]){
            max = used_count[i];
            ans = i;
        }
    }
    return ans;
}