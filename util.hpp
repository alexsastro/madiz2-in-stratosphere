#ifndef util_hpp__
#define util_hpp__

#include <vector>
#include <string>
using namespace std;
#define uchar unsigned char

struct Mat
{
    unsigned rows,cols;
    vector<vector<uchar>> at;
};

class point
{
    public:
    int x,y;
    point(int &ys,int &xs)
    {
        x=xs;
        y=ys;
    }
    point()
    {
        x=0;y=0;
    }
    point operator+(point const &obj)
    {
        point res;
        res.x=x+obj.x;
        res.y=y+obj.y;
        return res;
    }
};

uchar pixel(Mat &img,int &i,int &j);

uchar pixel(Mat &img,point &p);

void spixel(Mat &img,point &p,uchar value);

float mean(Mat &img);

void EnchanceBrightness(Mat &img,float factor);

vector<uchar> filter_pixels(Mat &img, float factor);

Mat zero_Mat(unsigned height, unsigned width);

Mat load_gray_image(string pth);

Mat copy_im(Mat img);

#endif