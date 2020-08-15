/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int* array = malloc(sizeof(int)*2);
    int i,j,k;
    k = 0;
    for (i = 0; i < numsSize; i++)
    {
        array[0] = i;
        int tmp = target - *(nums + i);
        for(j = i + 1; j < numsSize; j++)
        {
            if ( *(nums + j) == tmp)
            {
                array[1] = j;
                k = 1;
                break;
            }
        }
        if (k == 1)
        {
            break;
        }
    }
    return array;
}
