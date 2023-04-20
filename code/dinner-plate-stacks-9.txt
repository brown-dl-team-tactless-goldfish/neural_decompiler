class FenwickTree
{
    vector<int> tree;
    int sum=0;
    public:
    void add(int i,int val)
    {
        sum+=val;
        while(i<tree.size())
        {
            tree[i]+=val;
            i+=(i&(-i));
        }
    }
    FenwickTree()
    {
        tree.resize(1);
    }
    FenwickTree(vector<int>& arr)
    {
        tree.resize(arr.size()+1);
        for(int i=0;i<arr.size();++i)
            add(i+1,arr[i]);
    }
    int query(int i)
    {
        if(i>=tree.size())
            return INT_MAX;
        int ret=0;
        while(i)
        {
            ret+=tree[i];
            i=(i&(i-1));
        }
        return ret;
    }
    void append(int val)
    {
        int n=tree.size();
        int parent=(n&(n-1));
        sum+=val;
        tree.push_back(sum-query(parent));
    }
};
class DinnerPlates 
{
    int limit,c=0;
    FenwickTree *ptr;
    vector<vector<int>> st;
    int n;
    int binarySearchLeft()
    {
        int start=0,end=st.size()-1,temp=st.size();
        while(start<=end)
        {
            int q=start+(end-start)/2;
            if(ptr->query(q+1)<(q+1)*limit)
                if(q>0&&ptr->query(q)<(q)*limit)
                    end=q-1;
                else return q;
            else start=q+1;
        }
        return -1;
    }
    int binarySearchRight()
    {
        ++c;
        int start=0,end=st.size()-1,temp=st.size();
        while(start<=end)
        {
            int q=start+(end-start)/2;
            if((long)n-ptr->query(q)>0)
                if(q+1<temp&&(long)n-ptr->query(q+1)>0)
                    start=q+1;
                else return q;
            else end=q-1;
        }
        return -1;
    }
public:
    DinnerPlates(int capacity) 
    {
        limit=capacity;
        ptr=new FenwickTree();
        n=0;
    }
    
    void push(int val)
    {
        int index=binarySearchLeft();
        ++n;
        if(index!=-1)
        {
            st[index].push_back(val);
            ptr->add(index+1,1);
        }
        else
        {
            st.push_back({val});
            ptr->append(1);
        }
    }
    
    int pop() 
    {
        int index=binarySearchRight();
        if(index!=-1)
        {
            int ret=st[index].back();
            st[index].pop_back();
            ptr->add(index+1,-1);
            --n;
            return ret;
        }
        else return -1;
    }
    
    int popAtStack(int index) 
    {
        if(index<st.size()&&st[index].size())
        {
            int ret=st[index].back();
            st[index].pop_back();
            ptr->add(index+1,-1);
            --n;
            return ret;
        }
        else return -1;
    }
};
/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates* obj = new DinnerPlates(capacity);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAtStack(index);
 */