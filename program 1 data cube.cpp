#include<iostream>
#include<fstream>

using namespace std;
    int main()
    {
        ofstream outfile;
        outfile.open("Data_Cube_csv.csv");

        int arr[3][3][3], i, j, k, a, b, c, s_no, semester, attribute;
        const char* col_val[10] = {"S_No", "Age", "Studying_habbit"};


        cout<<"Enter the dimensions\n"<<endl;
        cout<<"***********************************************"<<endl;
        cout<<"Enter the size of the semester dimension"<<endl;
        cin>>a;
        cout<<"Enter the size of the student dimension"<<endl;
        cin>>b;
        cout<<"Enter the size of the attribute dimension"<<endl;
        cin>>c;

        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                for(k=0;k<c;k++)
                {

                    cout<<"Enter the "<<col_val[k]<<"of student:"<<j+1<<"in sem - "<<i+1<<endl;
                    cin>>arr[i][j][k];

                }
            }
        }

        cout<<"Values in the datacube"<<endl;
        cout<<"Enter the serial number of the student:"<<endl;
        cin>>s_no;
        cout<<"Enter the semester"<<endl;
        cin>>semester;
        cout<<"Enter the attribute you want to fetch"<<endl;
        for(i=0;i<3;i++)
        {
            cout<<i+1<<col_val[i]<<"\n";
        }
        cin>>attribute;


        if(attribute<1)
        {
            cout<<"Enter a valid attribute"<<endl;
        }
        else
        {
            cout<<col_val[attribute-1]<<arr[semester-1][s_no-1][attribute-1]<<endl;
            outfile<<col_val[attribute-1]<<","<<arr[semester-1][s_no-1][attribute-1]<<endl;

        }
        outfile.close();

    }
