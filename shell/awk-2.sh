awk '
    {
        result = 1
        for ( i = 1; i < NF; i++ ) {
            if ($i < 50 && $i >= 0) {
                result = 0;
                break;
            }
        }
        printf("%s : ", $1);
        if (result)
            printf("Pass\n");
        else
            printf("Fail\n");
    }
'