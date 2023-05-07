#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstdlib>

using namespace std;

void Slice_year_dimension(int arr[10][10][10], int a, int b, int c)
{
    ofstream outfile_2;
    outfile_2.open("Sliced_operation_year.csv");
    int year, i, j, k;

    const char* years[10]={"2017","2018","2019","2020","2021"};
    const char* states[10]={"Assam","Kerela","Goa"};
    const char* quater_val[10]={"q1","q2","q3","q4"};

    cout<<"Enter the Year along which you want to slice"<<endl;
    for(i=0;i<a;i++)
    {
        cout<<i+1<<"  -- "<<years[i]<<endl;
    }
    cin>>year;

    cout<<"Sliced array is"<<endl;
    cout<<"*********************************************"<<endl;
    cout<<endl;
    for(j=0;j<b;j++)
    {
        cout<<states[j]<<endl;
        outfile_2<<states[j]<<endl;
        for(k=0;k<c;k++)
        {
            cout<<quater_val[k]<<"\t";
            cout<<arr[year-1][j][k]<<"\n";

            outfile_2<<quater_val[k]<<",";
            outfile_2<<arr[year-1][j][k]<<endl;
        }
        cout<<endl;
        outfile_2<<endl;
    }
    outfile_2.close();
}
void Slice_state_dimension(int arr[10][10][10], int a, int b, int c)
{
    ofstream outfile_3;
    outfile_3.open("Sliced_operation_state.csv");
    int state, i, j, k;

    const char* years[10]={"2017","2018","2019","2020","2021"};
    const char* states[10]={"Assam","Kerela","Goa"};
    const char* quater_val[10]={"q1","q2","q3","q4"};

    cout<<"Enter the Year along which you want to slice"<<endl;
    for(i=0;i<b;i++)
    {
        cout<<i+1<<"  -- "<<states[i]<<endl;
    }
    cin>>state;

    cout<<"Sliced array is"<<endl;
    cout<<"*********************************************"<<endl;
    cout<<endl;
    for(i=0;i<a;i++)
    {
        cout<<years[i]<<endl;
        outfile_3<<years[i]<<endl;
        for(k=0;k<c;k++)
        {
            cout<<quater_val[k]<<"\t";
            cout<<arr[i][state-1][k]<<"\n";

            outfile_3<<quater_val[k]<<",";
            outfile_3<<arr[i][state-1][k]<<endl;
        }
        cout<<endl;
        outfile_3<<endl;
    }
    outfile_3.close();
}
void Slice_quater_dimension(int arr[10][10][10], int a, int b, int c)
{
    ofstream outfile_4;
    outfile_4.open("Sliced_operation_quater.csv");
    int quater, i, j, k;

    const char* years[10]={"2017","2018","2019","2020","2021"};
    const char* states[10]={"Assam","Kerela","Goa"};
    const char* quater_val[10]={"q1","q2","q3","q4"};

    cout<<"Enter the Year along which you want to slice"<<endl;
    for(i=0;i<a;i++)
    {
        cout<<i+1<<"  -- "<<quater_val[i]<<endl;
    }
    cin>>quater;

    cout<<"Sliced array is"<<endl;
    cout<<"*********************************************"<<endl;
    cout<<endl;
    for(i=0;i<a;i++)
    {
        cout<<years[i]<<endl;
        outfile_4<<years[i]<<endl;
        for(j=0;j<b;j++)
        {
            cout<<states[j]<<"\t";
            cout<<arr[i][j][quater-1]<<"\n";

            outfile_4<<states[j]<<",";
            outfile_4<<arr[i][j][quater-1]<<endl;
        }
        cout<<endl;
        outfile_4<<endl;
    }
    outfile_4.close();
}


int main()
{
    ofstream outfile;
    outfile.open("Data_cube_csv_2.csv");

    int arr[10][10][10], i, j, k, a, b, c, options=0, state, quarter, att, year;
    int s_no, semester, attribute;

    const char* years[10]={"2017","2018","2019","2020","2021"};
    const char* states[10]={"Assam","Kerela","Goa"};
    const char* quater_val[10]={"q1","q2","q3","q4"};

    cout<<"Enter the dimension of the array"<<endl;
    cout<<"*************************************************************"<<endl;
    cout<<"Enter the size of the year dimensions"<<endl;
    cin>>a;
    cout<<"Enter the number of the state dimensions"<<endl;
    cin>>b;
    cout<<"Enter the number of the quater dimensions"<<endl;
    cin>>c;

    for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                for(k=0;k<c;k++)
                {

                    cout<<"Enter the data corresponding to : "<<quater_val[k]<<"  of state: "<<states[j]<<"  in year: "<<years[i]<<endl;
                    cin>>arr[i][j][k];

                }
            }
        }

    outfile<<"Data Representation"<<endl;
    for(i=0;i<a;i++)
    {
        cout<<years[i]<<endl;
        outfile<<years[i]<<endl;

        for(j=0;j<b;j++)
        {
            cout<<states[j]<<endl;
            outfile<<states[j]<<endl;

            for(k=0;k<c;k++)
            {
                cout<<quater_val[k]<<"\t";
                outfile<<quater_val[k]<<",";
                cout<<arr[i][j][k]<<"\t";
                outfile<<arr[i][j][k]<<",";
                cout<<endl;
                outfile<<endl;
            }
            cout<<endl;
            outfile<<endl;
        }
        cout<<endl;
        outfile<<endl;
    }
    outfile.close();

    do{
    cout<<"Enter a operation you want to perform"<<endl;
    cout<<"****************************************************"<<endl;
    cout<<"1. Slice year dimension whise \n2. Slice state dimension wise \n3. Slice quater dimension wise \n"<<endl;
    cin>>options;

    switch(options)
    {

    case 1:
        Slice_year_dimension(arr,a,b,c);
        break;
    case 2:
        Slice_state_dimension(arr,a,b,c);
        break;
    case 3:
        Slice_quater_dimension(arr,a,b,c);
        break;
    case 4:
        exit(0);
        break;
    default:
        cout<<"Please enter a valid option";
        break;

    }
    }while(options!=4);


}

