double get_volume(triangle tr) {
    double p, a, b, c;
    a = (double) tr.a;
    b = (double) tr.b;
    c = (double) tr.c;
    p = (a + b + c)/2;
    
    /* don't return sqrt() as it doesn't change the order */
    return p*(p - a)*(p - b)*(p - c);
}

int cmp_func(const void *a, const void *b) {
    triangle *ia = (triangle *) a;
    triangle *ib = (triangle *) b;
    
    return (int)(get_volume(*ia) - get_volume(*ib));
}

void sort_by_area(triangle *tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    qsort((void *) tr, n, sizeof(triangle), cmp_func);
}