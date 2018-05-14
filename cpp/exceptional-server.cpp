try {
    Server s;
    int ret = s.compute(A, B);
    cout << ret << endl;
} 
catch (bad_alloc& error) {
    cout << "Not enough memory" << endl;
}
catch (exception& error) {
    cout << "Exception: " << error.what() << endl;
}
catch (...) {
    cout << "Other Exception" << endl;
}