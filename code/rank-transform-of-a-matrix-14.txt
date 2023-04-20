/**
 * @author      : archit
 * @GitHub      : archit-1997
 * @Email       : architsingh456@gmail.com
 * @file        : rankTransformOfAMatrix.cpp
 * @created     : Tuesday Aug 10, 2021 20:43:28 IST
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    int findParent(vector<int> &parent,int x){
        while(parent[x]!=x){
            parent[x]=parent[parent[x]];
            x=parent[x];
        }
        return x;
    }

    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        int row=matrix.size(),col=matrix[0].size();

        //answer vector
        vector<vector<int>> ans(row,vector<int>(col));
    
        //map to store the values : using map so that the sorted order is maintained
        map<int,vector<pair<int,int>>> elements;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++)
                elements[matrix[i][j]].push_back({i,j});
        }

        //we will store the ranks in a vector
        //size is row+col to maintain in a same vector
        //initially all ranks will be 0
        vector<int> rank(row+col,0);

        for(auto element : elements){
            //creating a parent array for the current element
            vector<int> parent(row+col,0);
            //parent[i]=i
           iota(parent.begin(),parent.end(),0);

            for(auto it : element.second){
                int x=it.first,y=it.second;
                //find the parent of x and y
                int px=findParent(parent,x);
                int py=findParent(parent,y+row);

                //we will connect the row with the column
                //make column's parent as the row's parent
                parent[px]=py;
                //we need to find the max rank out of the two and then assign this to the parent's rank so that the
                //parent is updated with the max rank
                rank[py]=max(rank[px],rank[py]);
            }

            //now we need to find the ranks and then fill in the answer matrix
            vector<int> curr=rank;
            for(auto it : element.second){
                int x=it.first,y=it.second;
                int px=findParent(parent,x);
                //the value of ans[x][y] will be max rank : which is the rank of the parent+1
                ans[x][y]=rank[px]+1;
                //we also neeed to update the rank of x and y with the max rank of the parent +1
                curr[x]=rank[px]+1;
                curr[y+row]=rank[px]+1;
            }
            swap(rank,curr);
        }

        // now we just need to return the answer matrix
        return ans;
        
    }
};

