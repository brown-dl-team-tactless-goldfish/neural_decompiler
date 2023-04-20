char* longestCommonPrefix(char* strs[], int strsSize)
{
	if (strsSize == 0)
		return "";

	if (strsSize == 1)
		return strs[0];

	int len = 0;
	int min = strlen(strs[0]);
	int c = 0;
	char *min_str[1];

	for (int i = 0; i < strsSize - 1; i++) {
		min = strlen(strs[i]) <= min ? strlen(strs[i]) : min;
		if(min == strlen(strs[i]))
			min_str[0] = strdup(strs[i]);
	}

	for (; c < min; c++)
	{
		for (int s = 0; s < strsSize - 1; s++)
		{
			char* jj = strs[s + 1];
			if (strs[s][c] == strs[s + 1][c])
			{
				continue;
			}
			else
			{
				char* prefix = strdup(strs[0]);
				prefix[c] = '\0';
				return prefix;

			}
		}
	}
	return min_str[0];
}