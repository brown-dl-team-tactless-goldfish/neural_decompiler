#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
private:
    inline pair<int, int> get_interval(int x, int y, int rad, int row) {
        assert(abs(y - row) <= rad); // We do not support doing rows in which no circle elements are present

        // Can be improved by knowing which row you are in specifically, which should narrow down
        // your compute to O(1) here instead of O(log(r))
        int x_lo = min(x - rad - 1, -1); // You can prove this point is NEVER in the circle
        int x_hi = x;                    // You can prove this point is ALWAYS in the circle
        int rad2 = rad * rad;
        while (x_lo + 1 < x_hi) {
            assert(0 <= x_hi && x_hi <= 100);

            // This is an x_hi-inclusive BS
            int x_mid = x_hi - (x_hi - x_lo) / 2;
            assert(0 <= x_mid && x_mid <= 100);

            // Distance displacements
            int dx = x_mid - x;
            int dy = row - y;
            if (dx * dx + dy * dy > rad2) x_lo = x_mid; // x_mid Definately NOT in the circle
            else x_hi = x_mid;                          // x_mid Definately in the circle
        }
        assert(0 <= x_hi && x_hi <= 100);

        int x_start = x_hi;
        int x_end = x + (x - x_hi);
        // DEBUG
        // cout << "interval in row " << row << " for circle " << x << " " << y << " " << rad << " is " << x_start << " " << x_end << "\n"; 
        return pair<int, int>(x_start, x_end);
    }
    inline void insert_interval(unordered_map<int, vector<pair<int, int>>>& intervals_rows, int row, pair<int, int> interval) {
        // You could use BS here but I got a little lazy and I'm also not sure it matters asymptotically unless
        // you have some sort of faster way to insert/move around inside the array (i.e. a linkedlist type structure)
        assert(intervals_rows[row].size() >= 1);
        vector<pair<int, int>>& old_intervals = intervals_rows[row];
        vector<pair<int, int>>  new_intervals;
        int i = 0;
        while (i < old_intervals.size() && old_intervals[i].first < interval.first) { new_intervals.push_back(old_intervals[i]); i++; }

        assert(i == new_intervals.size());
        if (i > 0 && interval.first <= new_intervals[new_intervals.size() - 1].second) {
            int prev_second = new_intervals[new_intervals.size() - 1].second;
            new_intervals[new_intervals.size() - 1].second = max(prev_second, interval.second);
        } else new_intervals.push_back(interval);

        while (i < old_intervals.size() && old_intervals[i].first <= new_intervals[new_intervals.size() - 1].second) {
            int prev_second = new_intervals[new_intervals.size() - 1].second;
            new_intervals[new_intervals.size() - 1].second = max(prev_second, old_intervals[i].second);
            i++;
        }
        while (i < old_intervals.size()) { new_intervals.push_back(old_intervals[i]); i++; }

        intervals_rows[row] = new_intervals;
    }
public:
    int countLatticePoints(vector<vector<int>>& circles) {
        unordered_map<int, vector<pair<int, int>>> intervals;
        // O(crlog(r)), possible with some high school math to turn into O(cr) if
        // there are c circles and each has max radius r
        for (vector<int>& circle: circles) {
            int x = circle[0]; int y = circle[1]; int rad = circle[2];
            for (int row = y - rad; row <= y + rad; row++) {
                pair<int, int> interval = get_interval(x, y, rad, row);
                if (intervals.find(row) == intervals.end()) {
                    intervals[row] = vector<pair<int, int>>(1, interval);
                } else {
                    // DEBUG
                    // cout << "circle " << x << " " << y << " " << rad << " and row " << row << "\n";
                    insert_interval(intervals, row, interval);
                }
            }
        }

        // Parallalizeable and good for cache
        // Inclusive intervals of all the points inside a circle
        int count = 0;
        for (auto& _ir : intervals) {
            vector<pair<int, int>>& interval_row = _ir.second;
            for (pair<int, int>& interval : interval_row) {
                assert(interval.first <= interval.second);

                int x1 = interval.first; int x2 = interval.second;
                count += x2 - x1 + 1; // It's inclusive on both sides
            }
        }
        return count;
    }
};