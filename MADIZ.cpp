#include "obr.hpp"
#include "util.hpp"
#include "serv.hpp"
#include <omp.h>
#include <iostream>
#include <vector>
#include <tuple>
#include <stdio.h>
#include <string>
#define str to_string
#define uchar unsigned char
using namespace std;


void scan(Mat &image,vector<string>&s,vector<int> &csts, vector<bool> &fxs,int i)
{
    Mat imgs;
    float averange;
    vector<uchar> pixel_brightness, group_brightness;
    imgs=copy_im(image);
    tie(averange, pixel_brightness, group_brightness)=count_pixels(imgs,csts[i],fxs[i]);
    int cgroups=count_groups(image,averange);
    s[i]=";"+str(averange)+";"+str(pixel_brightness.size())+';'+str(group_brightness.size())+";"+str(cgroups);
}


int main(int argc, char** argv)
{
	Mat image;
	image = load_gray_image(argv[1]);
    //namedWindow("Display Image", WINDOW_AUTOSIZE);
	//imshow("Display Image", image);
    //waitKey(0);
    
    auto t=start_time();

    //cout<<image.rows<<' '<<image.cols<<'\n';
    vector<int> csts = vector<int> { 7, 9, 11, 15, 17,(int)mean(image)/32,80};
    vector<bool> fxs = vector<bool> {false,false,false,false,false,false,true};
    string sn=str(is_overexposed(image)); //row for save to csv file
    vector<string> s = vector<string>(7);
    #pragma omp parallel for
    for (int i=0;i<7;i++)
    {
        scan(image,s,csts,fxs,i);
    }

    get_time(t,"main");
    
    cout<<sn;
    for (int i=0;i<7;i++)
    {
        cout<<s[i];
    }
    cout<<'\n';
    process_mem_usage();
    return 0;
}