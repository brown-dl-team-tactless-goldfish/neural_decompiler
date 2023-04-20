using ll=long long;
class segmentTree {
private:
	vector<ll> segTree;
	vector<bool> lazy;
    void propogateDown(ll ind,ll low,ll high){
		if (lazy[ind]) {
			segTree[ind] = (high-low+1)-segTree[ind];
			if (low != high) {
				//propogate the lazy update downwards
				//for the remaining nodes to get updated
				lazy[2 * ind + 1] = !lazy[2 * ind + 1];
				lazy[2 * ind + 2] = !lazy[2 * ind + 2];
			}
			lazy[ind] = 0;
		}
    }
public:
	segmentTree(vector<int> &arr) {
		ll n = arr.size();
		segTree.resize(4 * n + 1);
		lazy.resize(4* n + 1);
		build(0,0,n-1,arr);
	}
	void build(ll ind, ll low, ll high, vector<int> &arr) {
		if (low == high) {
			segTree[ind] = arr[low];
			return;
		}
		ll mid = low + (high - low) / 2;
		build(2 * ind + 1, low, mid, arr);
		build(2 * ind + 2, mid + 1, high, arr);
		segTree[ind] = segTree[2 * ind + 1] + segTree[2 * ind + 2];
	}

	void rangeUpdate(ll ind, ll low, ll high, ll l, ll r) {
		if (low > high) {
			return;
		}
		// apply any pending lazy updates
        propogateDown(ind,low,high);
		// no overlap
		if (low > r || high < l) {
			return;
		}
		// complete overlap
		if (low >= l && high <= r) {
			segTree[ind] = (high-low+1)-segTree[ind];
			if (low != high) {
				//propogate the lazy update downwards
				//for the remaining nodes to get updated
				lazy[2 * ind + 1] = !lazy[2 * ind + 1];
				lazy[2 * ind + 2] = !lazy[2 * ind + 2];
			}
			return;
		}
		// partial overlap
		ll mid = (low + high) >> 1;
		rangeUpdate(2 * ind + 1, low, mid, l, r);
		rangeUpdate(2 * ind + 2, mid + 1, high, l, r);
		segTree[ind] = segTree[2 * ind + 1] + segTree[2 * ind + 2];
	}

	ll query(ll ind, ll low, ll high, ll l, ll r) {
		if (low > r || high < l) {
			return 0;
		}
        // apply any pending lazy updates
		propogateDown(ind,low,high);
		if (low >= l && high <= r) {
			return segTree[ind];
		}
		
		ll mid = (low + high) >> 1;
		ll left = query(2 * ind + 1, low, mid, l, r);
		ll right = query(2 * ind + 2, mid + 1, high, l, r);
		return left + right;
	}
};

class Solution {
public:
    vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        segmentTree st(nums1);
        ll sum=accumulate(begin(nums2),end(nums2),0LL);
        vector <ll> ans;
        for(auto query:queries){
            ll q=query[0];
            ll l=query[1];
            ll r=query[2];
            if(q==1){
                st.rangeUpdate(0,0,nums1.size()-1,l,r);
            }
            else if(q==2){
                ll temp=st.query(0,0,nums1.size()-1,0,nums1.size()-1);
                sum+=(1LL*l*temp);
            }
            else ans.push_back(sum);
        }
        return ans;
    }
};