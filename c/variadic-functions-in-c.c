
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) < (b) ? (b) : (a))

int sum(int count, ...) {
    va_list ap;
    int sum;
    
    va_start (ap, count);           /* Initialize the argument list. */
    
    sum = 0;
    for (int i = 0; i < count; i++)
        sum += va_arg (ap, int);    /* Get the next argument value. */
    
    va_end (ap);                    /* Clean up. */
    return sum;
}

int min(int count, ...) {
    va_list ap;
    int minimum = MAX_ELEMENT;
    
    va_start (ap, count);           /* Initialize the argument list. */
    
    for (int i = 0; i < count; i++) {
        int next_el;
        
        next_el = va_arg (ap, int);
        minimum = _min(minimum, next_el);
    }
    
    va_end (ap);                    /* Clean up. */
    return minimum;
}

int max(int count, ...) {
    va_list ap;
    int maximum = MIN_ELEMENT;
    
    va_start (ap, count);           /* Initialize the argument list. */
    
    for (int i = 0; i < count; i++) {
        int next_el;
        
        next_el = va_arg (ap, int);
        maximum = _max(maximum, next_el);
    }
    
    va_end (ap);                    /* Clean up. */
    return maximum;
}