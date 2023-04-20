long long pickGifts(int* gifts, int giftsSize, int k) {

    register unsigned short i, j, x;
	register unsigned long long sum = 0;
	for(i = 0; i < k; i++) {
        register unsigned int largest = 0, index = 0;
		for(j = 0; j < giftsSize; j++) {
			if(gifts[j] > largest) {
				largest = gifts[j];
				index = j;
			}
		}
		gifts[index] = floor(sqrt(gifts[index]));
	}
	for(x = 0; x < giftsSize; x++)
		sum += gifts[x];

	return sum;
}