class Box {
    int l, b, h;
    
    public:
        Box() {
            l = 0, b = 0, h = 0;
        }
        Box(int nl, int nb, int nh) {
            l = nl, b = nb, h = nh;
        }
        Box(const Box& box) {
            l = box.getLength();
            b = box.getBreadth();
            h = box.getHeight();
        }
    
        int getLength() const {return l;}
        int getBreadth() const {return b;}
        int getHeight() const {return h;}
    
        long long CalculateVolume() {
            long long ret = l;
            ret *= b;
            ret *= h;
            return ret;
        }
        bool operator<(const Box& box) {
            bool ret = false;
            if (l < box.getLength())
                ret = true;
            else if (l == box.getLength() && b < box.getBreadth())
                ret = true;
            else if (l == box.getLength() && l == box.getBreadth() && h < box.getHeight())
                ret = true;
           return ret; 
        }
        friend std::ostream& operator<<(ostream& out, const Box& B);
};

std::ostream& operator<<(std::ostream& out, const Box& box) {
    out << box.getLength() << ' ' << box.getBreadth() << ' ' << box.getHeight();
    return out;  
}
// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);

// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

