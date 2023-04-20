

int minCostToMoveChips(int* position, int positionSize)
{
    int no_of_even_pos = 0;
    int no_of_odd_pos = 0;
    
    int i=0;
    for(i=0; i<positionSize; i++)
    {
        if(position[i]%2 == 0)
        {
            no_of_even_pos++;
        }
        else
        {
            no_of_odd_pos++;
        }
    }
    
    return no_of_even_pos < no_of_odd_pos ? no_of_even_pos : no_of_odd_pos;
}