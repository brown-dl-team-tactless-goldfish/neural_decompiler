int group_size[100001];
int* group[100001];
int visit[100001];
int dfs_group[100001];
int dfs_size;

void dfs(int tmp)
{
	int i;
	for(i = 0; i < group_size[tmp]; i++)
	{
		if(visit[group[tmp][i]] == 0)
		{
			visit[group[tmp][i]] = 1;
			dfs_group[dfs_size++] = group[tmp][i];
			dfs(group[tmp][i]);
		}
	}	
}

int Hamm(int *src, int *tgt, int src_size)
{
    int cnt = 0;
    for (int i = 0; i < src_size; i++)
    {
        cnt += (src[i] != tgt[i]);
    }
    return cnt;
}

int compare_function(void const *a, void const *b) {
    return *(int *)a - *(int *)b;
}

int count_allow_ham(int* src,int* dst,int src_size)
{
	int ans = src_size;
    int i = 0, j = 0;
    while (i < src_size && j < src_size)
    {
        if (src[i] == dst[j])
        {
            ans--; 
            i++;
            j++;
        }
        else if(src[i] < dst[j])
        {
            i++;
        }
        else if (src[i] > dst[j])
        {
            j++;
        }
    }
    return ans;
}

int minimumHammingDistance(int* source, int sourceSize, int* target, int targetSize, int** allowedSwaps, int allowedSwapsSize, int* allowedSwapsColSize){
	int i,j,answer = 0;
	memset(dfs_group, 0, sizeof(dfs_group));
	memset(group_size, 0, sizeof(group_size));
	memset(visit, 0, sizeof(visit));
	dfs_size = 0;
	
	//calculate array size
	for(i = 0; i < allowedSwapsSize; i++)
	{
		group_size[allowedSwaps[i][0]]++;
		group_size[allowedSwaps[i][1]]++;
	}
	//malloc array size
	for(i = 0; i < 100001; i++)
	{
		if(group_size[i])
		{
			group[i] = malloc(sizeof(int) * (group_size[i]));
		}
	}
	
	memset(group_size, 0, sizeof(group_size));
	for(i = 0; i < allowedSwapsSize; i++)
	{
		group_size[allowedSwaps[i][0]]++;
		group_size[allowedSwaps[i][1]]++;	

		group[allowedSwaps[i][0]][group_size[allowedSwaps[i][0]] - 1] = allowedSwaps[i][1];
		group[allowedSwaps[i][1]][group_size[allowedSwaps[i][1]] - 1] = allowedSwaps[i][0];
	}
	/*
	for(i = 0; i < 100001; i++)
	{
		if(group_size[i] != 0)
		{
			for(j = 0; j < group_size[i]; j++)
			{
				printf("*group : %d : %d ",i,group[i][j]);
			}
			printf("\n");
		}
	}
	printf("\n");
	*/
	//determine swap  HERE
	for(i = 0; i < 100001; i++)
	{
		if(visit[i] == 0 && group_size[i])
		{
			visit[i] = 1;
			dfs_group[dfs_size++] = i;
			dfs(i);
			int src[100001],dst[100001],src_size = 0, dst_size =0;
			for(j = 0; j < dfs_size; j++)
			{ 
				src[src_size++] = source[dfs_group[j]];
				dst[dst_size++] = target[dfs_group[j]];
			}
			qsort(src, src_size, 4, compare_function);
			qsort(dst, dst_size, 4, compare_function);	
			answer += count_allow_ham(src, dst, src_size);
			dfs_size = 0;
		}
	}
	
	int tmp[100000];
	int tmp_size = 0;
	memset(tmp,0,sizeof(tmp));
	for (i = 0; i < 100001; i++)
	{
		if (visit[i] == 0 && i < sourceSize)
		{
			tmp[tmp_size++] = i;
		}
	}
	if (tmp_size)
	{
		int src[100001], dst[100001];
		int src_size= 0, dst_size =0;
		for (int j = 0; j < tmp_size; j++)
		{
			src[src_size++] = (source[tmp[j]]);
			dst[dst_size++] = (target[tmp[j]]);
		}
		answer += Hamm(src, dst, src_size);
	}
	
	for(i = 0; i < 100001; i++)
	{
		if(group_size[i] != 0)
		free(group[i]);
	}
	return answer;
}