
bool check_eqations(int **arr, int a, int b, int exp)
{
    for (int j = 0; j < 26 && exp == '='; j++)
            if (arr[a][j] && arr[b][j] && arr[a][j] != arr[b][j])
                return (0);
        for (int j = 0; j < 26 && exp == '!'; j++)
            if (arr[a][j] && arr[b][j] && arr[a][j] == 1 && arr[a][j] == arr[b][j])
                return (0);
        if (exp == '=')
            arr[a][b] = arr[b][a] = 1;
        if (exp== '!')
            arr[a][b] = arr[b][a] = -1;
        for (int j = 0; j < 26; j++)
        {
            if (exp == '=')
            {
                if (arr[b][j])
                    arr[a][j] = arr[b][j];
                if (arr[a][j])
                    arr[b][j] = arr[a][j];
            }
            else
            {
                if (arr[b][j] == 1)
                    arr[a][j] == -1;
                if (arr[a][j] == 1)
                    arr[b][j] == -1;
            }
        }
    return (1);
}

bool equationsPossible(char ** eq, int s){
    int **arr = (int**) malloc(sizeof(int *) * 26);
    
    for (int i = 0; i < 26; i++)
    {
        arr[i] = (int*) malloc(sizeof(int) * 26);
        for (int j = 0; j < 26; j++)
            arr[i][j] = i == j;
    }
    for (int i = 0; i < s; i++)
    {
        if (!check_eqations(arr, eq[i][0] - 'a', eq[i][3] - 'a', eq[i][1]))
            return (0);
        for (int j = i - 1; j >= 0; j--)
            if (!check_eqations(arr, eq[j][0] - 'a', eq[j][3] - 'a', eq[j][1]))
                return (0);
    }
    return (1);
}