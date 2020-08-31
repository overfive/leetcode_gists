void swap(char *a, char *b)
{
    char t = *a;
    *a = *b;
    *b = t;
}

char* reverseString(char* s) {
    int l = strlen(s);
    if(l == 0)
        return "";
    for(int i = 0; i< l/2; i++)
    {
        swap(&s[i], &s[l-1-i]);
    }
    return s;
}
