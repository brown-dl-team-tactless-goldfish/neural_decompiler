int heap_cap_add(int* cap, int* heap, int *element_num, int element)
{
	int cur_num = 0;
	int tmp = 0;
    int n_idx = 0;
	
	*element_num = *element_num + 1;
	cur_num = *element_num;
	heap[cur_num] = element;
	
	while (1) {
		if (cur_num == 1) {
			break;
		}
        n_idx = cur_num/2;
		if (cap[heap[cur_num]] < cap[heap[n_idx]]) {
			tmp = heap[cur_num];
			heap[cur_num] = heap[n_idx];
			heap[n_idx] = tmp;
			cur_num = n_idx;
		} else {
			break;
		}
	}
	
	return 0;
}

int heap_cap_pop(int* cap, int* heap, int *element_num, int *pop_element)
{
	int cur_idx = 1;
	int cur_total = 0;
	int tmp = 0;
	int min_idx = 0;
    int i = 0;
    int n_idx = 0;
	
	if (*element_num == 0) {
        *pop_element = 0;
        return 0;
    }

	*pop_element = heap[1];
	heap[1] = heap[*element_num];
	*element_num = *element_num - 1;
	cur_total = *element_num;
	while (1) {
        n_idx = cur_idx*2;
		if (n_idx > cur_total) {
			break;
		}
        if (n_idx == cur_total) {
            if (cap[heap[cur_idx]] > cap[heap[n_idx]]) {
                min_idx = n_idx;
                tmp = heap[cur_idx];
                heap[cur_idx] = heap[min_idx];
                heap[min_idx] = tmp;
                cur_idx = min_idx; 
            } 
            break;
            
        }
		
		if (cap[heap[cur_idx]] > cap[heap[n_idx]] || cap[heap[cur_idx]] > cap[heap[n_idx + 1]]) {
			min_idx = (cap[heap[n_idx + 1]] < cap[heap[n_idx]])?n_idx + 1:n_idx;
			tmp = heap[cur_idx];
			heap[cur_idx] = heap[min_idx];
			heap[min_idx] = tmp;
			cur_idx = min_idx;
		} else {
            break;
        }
	}

	return 0;
}

int heap_add(int* heap, int *element_num, int element)
{
	int cur_num = 0;
	int tmp = 0;
    int n_idx = 0;
	
	*element_num = *element_num + 1;
	cur_num = *element_num;
	heap[cur_num] = element;
	
	while (1) {
		if (cur_num == 1) {
			break;
		}
        n_idx = cur_num/2;
		if (heap[cur_num] > heap[n_idx]) {
			tmp = heap[cur_num];
			heap[cur_num] = heap[n_idx];
			heap[n_idx] = tmp;
			cur_num = n_idx;
		} else {
			break;
		}
	}
	
	return 0;
}

int heap_pop(int* heap, int *element_num, int *pop_element)
{
	int cur_idx = 1;
	int cur_total = 0;
	int tmp = 0;
	int max_idx = 0;
    int i = 0;
    int n_idx = 0;
	
	if (*element_num == 0) {
        *pop_element = 0;
        return 0;
    }

	*pop_element = heap[1];
	heap[1] = heap[*element_num];
	*element_num = *element_num - 1;
	cur_total = *element_num;
	while (1) {
        n_idx = cur_idx*2;
		if (n_idx > cur_total) {
			break;
		}
        if (n_idx == cur_total) {
            if (heap[cur_idx] < heap[n_idx]) {
                max_idx = n_idx;
                tmp = heap[cur_idx];
                heap[cur_idx] = heap[max_idx];
                heap[max_idx] = tmp;
                cur_idx = max_idx; 
            } 
            break;
            
        }
		
		if (heap[cur_idx] < heap[n_idx] || heap[cur_idx] < heap[n_idx + 1]) {
			max_idx = (heap[n_idx + 1] > heap[n_idx])?n_idx + 1:n_idx;
			tmp = heap[cur_idx];
			heap[cur_idx] = heap[max_idx];
			heap[max_idx] = tmp;
			cur_idx = max_idx;
		} else {
            break;
        }
	}

	return 0;
}

int findMaximizedCapital(int k, int w, int* profits, int profitsSize, int* capital, int capitalSize){
    int i = 0, j = 0;
    int table[100001] = {0};
    int cap_table[100001] = {0};
    int table_num = 0;
    int cap_table_num = 0;
    int output = 0;
    int cur_w = w;
    int tmp = 0;
    int tmp_j = 0;
    int tmp_max = 0;
    int l = 0;
 

    // sort
    for (i = 0; i < profitsSize; i++) {
        heap_cap_add(capital, cap_table, &cap_table_num, i);
    }


    for (i = 0; i < k; i++) {
        while (1) {
            if (capital[cap_table[1]] > cur_w || cap_table_num == 0) {
                break;
            }
            heap_cap_pop(capital, cap_table, &cap_table_num, &tmp);
            heap_add(table, &table_num, profits[tmp]);
        }
        heap_pop(table, &table_num, &tmp);
        cur_w += tmp;
    }

    output = cur_w;

    return output;
}