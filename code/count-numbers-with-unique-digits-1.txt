int countNumbersWithUniqueDigits(int n){
	int choices[] = {9, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	int ans=1, product =  1;
	int k=n<=10?n:10;

	for(int i=0;i<k;i++){
		product*=choices[i];
		ans+=product;
	}
	return ans;
}