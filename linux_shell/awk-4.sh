awk '
    {
        if (++newline % 2)
            printf("%s;", $0)
        else
            printf("%s\n", $0)
    }
'