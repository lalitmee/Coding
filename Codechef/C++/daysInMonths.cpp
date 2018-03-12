#include <bits/stdc++.h>
using namespace std;
int main()
{
        int t;
        cin >> t;
        while (t--)
        {
                int w;
                cin >> w;
                string s;
                cin >> s;
                int arr[7];
                for (int i = 0; i < 7; i++)
                        arr[i] = 0;
                int a;
                for (int i = 0; i < 7; i++)
                        arr[i] = 4;
                a = w % 7;
                if (s == "mon")
                        for (int i = 0; i < a; i++)
                                arr[i]++;
                else if (s == "tues")
                        for (int i = 1; i < a + 1; i++)
                                arr[i]++;
                else if (s == "wed")
                        for (int i = 2; i < a + 2; i++)
                                arr[i]++;
                else if (s == "thurs")
                        for (int i = 3; i < a + 3; i++)
                                arr[i]++;
                else if (s == "fri")
                        for (int i = 4; i < a + 4; i++)
                                arr[i]++;
                else if (s == "sat")
                {   for (int i = 5; i < a + 5; i++)
                            arr[i]++;
                    if (w == 31)
                            arr[0]++; }
                else if (s == "sun")
                {   for (int i = 6; i < a + 6; i++)
                            arr[i]++;
                    if (w == 30)
                            arr[0]++;
                    else if (w == 31)
                    {   arr[0]++;
                arr[1]++;}}

                for (int i = 0; i < 7; i++)
                        cout << arr[i] << " ";
                cout << endl;
        }
}
