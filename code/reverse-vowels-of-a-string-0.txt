bool isVowel(char c)
{
	if ((c == 'A' || c == 'a') ||
		(c == 'E' || c == 'e') ||
		(c == 'I' || c == 'i') ||
		(c == 'O' || c == 'o') ||
		(c == 'U' || c == 'u'))
		return true;

	return false;
}

char *reverseVowels(char *s)
{
	if (s == NULL)
		return NULL;

	int i = 0;
	int j = strlen(s) - 1;

	while (i < j)
	{
		if (!isVowel(s[i]))
			i++;
		if (!isVowel(s[j]))
			j--;

		if (isVowel(s[i]) && isVowel(s[j]))
		{
			char temp = s[i];
			s[i] = s[j];
			s[j] = temp;

			i++;
			j--;
		}
	}

	return s;
}